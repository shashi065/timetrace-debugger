from timetrace.core.breakpoints import BreakpointManager
from timetrace.core.watchpoints import WatchpointManager
from timetrace.core.replay import ReplayEngine
from timetrace.core.diff import diff_states


class DebuggerCLI:
    def __init__(self, timeline):
        self.replay = ReplayEngine(timeline)
        self.breakpoints = BreakpointManager()
        self.watchpoints = WatchpointManager()

    # ---------------------------------
    # SHOW STACK
    # ---------------------------------
    def show_stack(self, state):
        print("\nCall Stack:")

        if not state.call_stack:
            print("  <empty>")
            return

        for i, func in enumerate(state.call_stack):
            indent = "  " * i
            print(f"{indent}{func}()")

    # ---------------------------------
    # DISPLAY TRANSITION
    # ---------------------------------
    def display_transition(self, previous, current):
        if current is None:
            return

        print(
            f"\nStep {current.step} | "
            f"{current.event_type.upper()} | "
            f"{current.file.split('\\')[-1]}:{current.line}"
        )

        if current.event_type == "call":
            print("Entering function")

        elif current.event_type == "return":
            print(f"Returning value -> {current.return_value}")

        elif current.event_type == "exception":
            print(f"Exception -> {current.info}")

        else:
            changes = diff_states(previous, current)
            print("Changes:")

            if changes:
                for var, (status, value) in changes.items():
                    if status == "REMOVED":
                        print(f"  {var} -> REMOVED")
                    else:
                        print(f"  {var} -> {status} = {value}")
            else:
                print("  No changes")

    # ---------------------------------
    # VARIABLE HISTORY
    # ---------------------------------
    def show_history(self, var_name):
        print(f"\nHistory of '{var_name}':\n")

        found = False

        for event in self.replay.timeline.events:
            if var_name in event.locals:
                print(f"[Step {event.step}] {var_name} = {event.locals[var_name]}")
                found = True

        if not found:
            print("  No history found.")

    # ---------------------------------
    # STEP OVER
    # ---------------------------------
    def step_over(self):
        current_event = self.replay.current()
        current_depth = current_event.depth

        while True:
            next_event = self.replay.forward()
            if not next_event:
                break
            if next_event.depth == current_depth:
                break

    # ---------------------------------
    # STEP OUT
    # ---------------------------------
    def step_out(self):
        current_event = self.replay.current()
        current_depth = current_event.depth

        while True:
            next_event = self.replay.forward()
            if not next_event:
                break
            if next_event.depth < current_depth:
                break

    # ---------------------------------
    # MAIN LOOP
    # ---------------------------------
    def start(self):
        print("\n--- Time Travel Debugger ---")
        print("n -> next")
        print("b -> back")
        print("si -> step into")
        print("so -> step over")
        print("su -> step out")
        print("p -> print state")
        print("g <step>")
        print("s -> stack")
        print("history <var> -> show variable history")
        print("break <line> -> set breakpoint")
        print("break if <condition> -> conditional breakpoint")
        print("bl -> list breakpoints")
        print("cb <line> -> clear breakpoint")
        print("watch <var> -> watch variable")
        print("wl -> list watchpoints")
        print("cw <var> -> clear watchpoint")
        print("c -> continue until breakpoint/watchpoint")
        print("q -> quit\n")

        while True:
            cmd = input("timetrace> ").strip()

            # ---------------------------------
            # STEP INTO
            # ---------------------------------
            if cmd == "si":
                prev = self.replay.current()
                curr = self.replay.forward()

                if curr:
                    self.display_transition(prev, curr)
                else:
                    print("Reached end of timeline.")

            # ---------------------------------
            # STEP OVER
            # ---------------------------------
            elif cmd == "so":
                prev = self.replay.current()
                self.step_over()
                curr = self.replay.current()

                if curr:
                    self.display_transition(prev, curr)
                else:
                    print("Reached end of timeline.")

            # ---------------------------------
            # STEP OUT
            # ---------------------------------
            elif cmd == "su":
                prev = self.replay.current()
                self.step_out()
                curr = self.replay.current()

                if curr:
                    self.display_transition(prev, curr)
                else:
                    print("Reached end of timeline.")

            elif cmd == "n":
                prev = self.replay.current()
                curr = self.replay.forward()

                if curr is None:
                    print("Reached end of timeline.")
                else:
                    self.display_transition(prev, curr)

            elif cmd == "b":
                curr = self.replay.current()
                prev = self.replay.backward()

                if prev is None:
                    print("At start of timeline.")
                else:
                    self.display_transition(curr, prev)

            elif cmd == "p":
                state = self.replay.current()
                print(f"\nStep {state.step}")
                print("Variables:")

                if state.locals:
                    for k, v in state.locals.items():
                        print(f"  {k} = {v}")
                else:
                    print("  No variables")

            elif cmd.startswith("g"):
                try:
                    _, step = cmd.split()
                    step = int(step) - 1

                    prev = self.replay.current()
                    curr = self.replay.goto(step)

                    if curr is None:
                        print("Invalid step.")
                    else:
                        self.display_transition(prev, curr)
                except:
                    print("Usage: g <step>")

            elif cmd == "s":
                self.show_stack(self.replay.current())

            elif cmd.startswith("history"):
                parts = cmd.split()

                if len(parts) != 2:
                    print("Usage: history <variable>")
                else:
                    self.show_history(parts[1])

            elif cmd == "q":
                break

            else:
                print("Unknown command.")
