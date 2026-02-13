import json
from timetrace.core.models import ExecutionEvent


class Timeline:
    def __init__(self):
        self.events = []

    # -----------------------------
    # Add Event
    # -----------------------------
    def add(self, event):
        self.events.append(event)

    # -----------------------------
    # Get Event
    # -----------------------------
    def get(self, index):
        return self.events[index]

    def __len__(self):
        return len(self.events)

    # -----------------------------
    # Convert to Dict (for JSON)
    # -----------------------------
    def to_dict(self):
        return [event.to_dict() for event in self.events]

    # -----------------------------
    # Save Timeline
    # -----------------------------
    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    # -----------------------------
    # Load Timeline (STATIC)
    # -----------------------------
    @staticmethod
    def load(path):
        with open(path, "r") as f:
            data = json.load(f)

        timeline = Timeline()
        for item in data:
            timeline.events.append(ExecutionEvent.from_dict(item))

        return timeline
