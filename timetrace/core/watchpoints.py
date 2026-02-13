class WatchpointManager:
    def __init__(self):
        self.watch_vars = set()

    def add(self, var_name):
        self.watch_vars.add(var_name)

    def remove(self, var_name):
        self.watch_vars.discard(var_name)

    def list_all(self):
        return list(self.watch_vars)

    # THIS is the missing method
    def check(self, prev_state, curr_state):
        for var in self.watch_vars:
            prev_val = prev_state.locals.get(var)
            curr_val = curr_state.locals.get(var)

            if prev_val != curr_val:
                return var

        return None
