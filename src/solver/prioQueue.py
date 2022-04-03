import copy
from heapq import heappush, heappop

#membuat prioqueue
class prioQueue:
    def __init__(self):
        self.heap = []
    def enqueue(self, k):
        heappush(self.heap, k)
    def dequeue(self):
        return heappop(self.heap)
    def empty(self):
        if self.heap:
            return False
        else:
            return True