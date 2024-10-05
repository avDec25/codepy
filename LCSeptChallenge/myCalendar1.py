import bisect


class MyCalendar:
    def __init__(self):
        self.ranges = [(-1, -1), (float('inf'), float('inf'))]

    # def isOverlapping(self, x_s, x_e, y_s, y_e):
    #     return x_s < y_e and y_s < x_e

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.ranges, (start, end))

        if start < self.ranges[index - 1][1]:
            return False

        if self.ranges[index][0] < end:
            return False

        self.ranges.insert(index, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
