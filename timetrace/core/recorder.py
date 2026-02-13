import sys


class ExecutionRecorder:
    def __init__(self):
        self.timeline = []
        self.step_count = 0
        self.call_stack = []

    def trace(self, frame, event, arg):

        if event == "call":
            self.call_stack.append(frame.f_code.co_name)
            self.step_count += 1

            snapshot = {
                "step": self.step_count,
                "event": "call",
                "file": frame.f_code.co_filename,
                "line": frame.f_lineno,
                "function": frame.f_code.co_name,
                "locals": dict(frame.f_locals),
                "stack": list(self.call_stack)
            }

            self.timeline.append(snapshot)
            return self.trace

        elif event == "line":
            self.step_count += 1

            snapshot = {
                "step": self.step_count,
                "event": "line",
                "file": frame.f_code.co_filename,
                "line": frame.f_lineno,
                "function": frame.f_code.co_name,
                "locals": dict(frame.f_locals),
                "stack": list(self.call_stack)
            }

            self.timeline.append(snapshot)
            return self.trace

        elif event == "return":
            self.step_count += 1

            # Pop first (function is exiting)
            if self.call_stack:
                popped_function = self.call_stack.pop()
            else:
                popped_function = None

            snapshot = {
                "step": self.step_count,
                "event": "return",
                "file": frame.f_code.co_filename,
                "line": frame.f_lineno,
                "function": frame.f_code.co_name,
                "locals": dict(frame.f_locals),
                "return_value": arg,
                "stack": list(self.call_stack)  # stack AFTER pop
            }

            self.timeline.append(snapshot)
            return self.trace

        return self.trace

    def run(self, func):
        sys.settrace(self.trace)
        try:
            func()
        finally:
            sys.settrace(None)

    def get_timeline(self):
        return self.timeline
