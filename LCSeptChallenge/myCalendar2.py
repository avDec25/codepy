class MyCalendarTwo:

    def __init__(self):
        self.hash = []

    def isOverlapping(self, x_s, x_e, y_s, y_e):
        return x_s < y_e and y_s < x_e

    def hasOverlapped(self, s, e):
        overlapped = 0
        for x, y in self.hash:
            if self.isOverlapping(x, y, s, e):
                overlapped += 1
                if overlapped == 2:
                    return True
        return False

    def book(self, start: int, end: int) -> bool:
        for x, y in self.hash:
            if self.isOverlapping(x, y, start, end):
                # overlapping sub-interval
                new_s, new_e = max(start, x), min(end, y)
                if self.hasOverlapped(new_s, new_e):
                    return False
        self.hash.append((start, end))
        return True
