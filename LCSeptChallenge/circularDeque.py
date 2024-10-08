from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.total = k
        self.front = deque()
        self.rear = deque()

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.front.append(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.rear.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            if len(self.front) > 0:
                self.front.pop()
            else:
                self.rear.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            if len(self.rear) > 0:
                self.rear.pop()
            else:
                self.front.popleft()
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            if len(self.front) > 0:
                return self.front[-1]
            else:
                return self.rear[0]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            if len(self.rear) > 0:
                return self.rear[-1]
            else:
                return self.front[0]
        else:
            return -1

    def isEmpty(self) -> bool:
        return (len(self.front) + len(self.rear)) == 0

    def isFull(self) -> bool:
        return (len(self.front) + len(self.rear)) == self.total

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
