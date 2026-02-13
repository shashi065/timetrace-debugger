class ReplayEngine:
    def __init__(self, timeline):
        self.timeline = timeline
        self.current_index = 0

    def current(self):
        return self.timeline.get(self.current_index)

    def forward(self):
        if self.current_index < len(self.timeline) - 1:
            self.current_index += 1
            return self.current()
        return None

    def backward(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.current()
        return None

    def goto(self, index):
        if 0 <= index < len(self.timeline):
            self.current_index = index
            return self.current()
        return None
