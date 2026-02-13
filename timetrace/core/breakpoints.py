class BreakpointManager:
    def __init__(self):
        # Line-based breakpoints
        self.line_breakpoints = set()

        # Conditional breakpoints (expressions like "x == 5")
        self.conditional_breakpoints = set()

    # -----------------------------
    # Line Breakpoints
    # -----------------------------

    def add_breakpoint(self, line):
        self.line_breakpoints.add(line)

    def remove_breakpoint(self, line):
        self.line_breakpoints.discard(line)

    def list_breakpoints(self):
        return sorted(self.line_breakpoints)

    def is_breakpoint(self, line):
        return line in self.line_breakpoints

    # -----------------------------
    # Conditional Breakpoints
    # -----------------------------

    def add_condition(self, condition):
        self.conditional_breakpoints.add(condition)

    def remove_condition(self, condition):
        self.conditional_breakpoints.discard(condition)

    def list_conditions(self):
        return list(self.conditional_breakpoints)

    # 🔥 EDGE-TRIGGERED CONDITIONAL BREAKPOINT
    # Triggers only when condition changes from False → True
    def check_condition(self, prev_state, curr_state):
        for condition in self.conditional_breakpoints:
            try:
                prev_result = eval(
                    condition,
                    {"__builtins__": {}},
                    prev_state.locals if prev_state else {}
                )

                curr_result = eval(
                    condition,
                    {"__builtins__": {}},
                    curr_state.locals if curr_state else {}
                )

                # Trigger only on False → True transition
                if not prev_result and curr_result:
                    return condition

            except Exception:
                # Ignore invalid expressions safely
                pass

        return None
