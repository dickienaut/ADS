class Queue(object):
    def __init__(self):
        self._data = []

    def is_empty(self):
        return not bool(self._data)
        # return self._items == []

    def enqueue(self, item):
        self._data.insert(0, item)

    def dequeue(self):
        return self._data.pop()

    def length(self):
        return len(self._data)
