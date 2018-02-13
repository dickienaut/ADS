class Stack(object):
    def __init__(self):
        self._data = []

    def length(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self._data)

    def peek(self):
        return self._data[-1]

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()
