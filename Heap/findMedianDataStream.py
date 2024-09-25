# find median from a running data stream
from heapq import heappop, heappush


def stream_median(a):
    max_heap = []
    min_heap = []
    for e in a:
        # fresh element: push in max-heap
        heappush(max_heap, -e)

        # try to keep diff in heap-lengths by 1
        # that is why we transfer, it will help us keep median(s) in sight/top
        heappush(min_heap, -heappop(max_heap))

        # prevent next time addition of element making the len diff by 2
        # we keep the left one i.e. the max heap as bigger always or equal
        if len(max_heap) < len(min_heap):
            heappush(max_heap, -heappop(min_heap))

        if len(max_heap) == len(min_heap):
            print((min_heap[0] - max_heap[0]) / 2, end=", ")
        else:
            print(-max_heap[0], end=", ")


if __name__ == '__main__':
    A = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    stream_median(A)
