class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return not bool(len(self.data))

    # 삭제 없이 단순히 맨 앞의 data 값을 리턴
    def get_front(self):
        return self.data[0]

    # 삭제 없이 단순히 맨 뒤의 data 값을 리턴
    def get_rear(self):
        return self.data[-1]

    def __repr__(self):
        return ''.format(self.data)


q = Queue()
q.enqueue(1)  # None, q.data => [1]
q.enqueue(q, 2)
q.enqueue(2)  # None, q.data => [1, 2]
q.get_front()  # 1
q.get_rear()   # 2
q.dequeue()   # 1, q.data => [2]
q.dequeue()   # 2, q.data => []