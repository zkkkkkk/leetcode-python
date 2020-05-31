class MyCalendarTwo:

    def __init__(self):
        self.raw = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlap:
            if end > i and start < j:
                return False
        for i, j in self.raw:
            if end > i and start <j:
                self.overlap.append((max(i, start), min(end, j)))
        self.raw.append((start, end))


