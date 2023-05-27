"""
Создайте очередь, в которой буду реализованы операции на добавление элементов
в конец очереди, удаление первого элемента и вычисление размера очереди
с сложностью алгоритма `О(1)`.
"""


class Deque:
    def __init__(self):
        self.deque = []

    def enqueue(self, item):
        self.deque.append(item)
        return self.deque

    def dequeue(self):
        if len(self.deque) == 0:
            return None
        self.deque = self.deque[1:]
        return self.deque

    def get_size(self):
        return len(self.deque)
