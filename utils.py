import heapq

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self._queue_ = []

    def push(self, item, priority):
        heapq.heappush(self._queue_, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue_)

    def isEmpty(self):
        if len(self._queue_) == 0:
            return True
        return False

    def checkExistence(self, item):
        for pri, i in self._queue_:
            if i.all() == item.all():
                return True
        return False

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        flag = 0
        update_path = True
        for pri,i in self._queue_:
            if i.all() == item.all():
                flag = 1
                if priority <= pri:
                    self._queue_.remove((pri, i))
                    self.push(item, priority)
                elif priority > pri:
                    update_path = False
        if flag == 0:
            self.push(item, priority)
        return update_path

