import sys
import runpy
import threading
import os
from types import FrameType
from typing import List

from timetrace.core.models import ExecutionEvent


class PythonAdapter:

    def __init__(self):
        self.timeline: List[ExecutionEvent] = []
        self.step = 0
        self.current_depth = 0
        self.target_file = None

    # --------------------------------------------------
    # RUN SCRIPT (FIXED + EXCEPTION SAFE)
    # --------------------------------------------------
    def run(self, script_path):

        self.target_file = os.path.abspath(script_path)
        self.timeline = []
        self.step = 0
        self.current_depth = 0

        # Inject script directory into sys.path
        script_dir = os.path.dirname(self.target_file)
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)

        # Enable tracing
        sys.settrace(self._trace)
        threading.settrace(self._trace)

        try:
            runpy.run_path(self.target_file, run_name="__main__")

        except Exception as e:
            # Capture final unhandled exception
            self.step += 1

            evt = ExecutionEvent(
                step=self.step,
                event_type="exception",
                filename=self.target_file,
                lineno=0,
                function_name="<top-level>",
                locals_snapshot={},
                depth=0,
                thread_id=0,
                exception=str(e),
            )

            self.timeline.append(evt)

        finally:
            sys.settrace(None)
            threading.settrace(None)

        return self.timeline

    # --------------------------------------------------
    # TRACE FUNCTION
    # --------------------------------------------------
    def _trace(self, frame: FrameType, event: str, arg):

        filename = os.path.abspath(frame.f_code.co_filename)

        # Only trace the target script file
        if filename != self.target_file:
            return self._trace

        if event not in ("call", "line", "return", "exception"):
            return self._trace

        # Depth handling
        if event == "call":
            self.current_depth += 1

        if event == "return":
            self.current_depth = max(0, self.current_depth - 1)

        self.step += 1

        # Safe locals snapshot
        try:
            locals_snapshot = {
                k: repr(v)
                for k, v in frame.f_locals.items()
            }
        except Exception:
            locals_snapshot = {}

        # Exception capture
        exception_text = None
        if event == "exception" and arg:
            exc_type, exc_value, _ = arg
            exception_text = f"{exc_type.__name__}: {exc_value}"

        evt = ExecutionEvent(
            step=self.step,
            event_type=event,
            filename=filename,
            lineno=frame.f_lineno,
            function_name=frame.f_code.co_name,
            locals_snapshot=locals_snapshot,
            depth=self.current_depth,
            thread_id=threading.get_ident(),
            exception=exception_text,
        )

        self.timeline.append(evt)

        return self._trace
