class Dequeue(object):
    def __init__(self):
        self._data = []

    def pop_left(self):
        return self._data.pop(0)

    def pop_right(self):
        return self._data.pop()

    def insert_left(self, item):
        self._data.insert(0, item)

    def insert_right(self, item):
        self._data.append(item)

    def length(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self._data)
