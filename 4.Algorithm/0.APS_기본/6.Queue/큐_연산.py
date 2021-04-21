# enQuene(item) : 큐의 뒤쪽에 원소 삽입
# deQueue() : 큐 앞쪽에 원소 삭제하고 반환 # front 자리가 한칸 뒤로감
# createQueue() : 공백 상태 큐를 생성
# isEmpty() : 큐가 공백상태인지 확인 # front와 rear 자리가 같음
# isFull() : 큐가 포화상태인지 확인
# Qpeek() : 큐의 앞쪽에서 원소를 삭제없이 반환

# 큐의 앞쪽 (front = -1로 초기화하는데 이것은 맨 뒷값이 아닌 0보다 앞의 인덱스)
# 큐의 뒤쪽 (rear = -1로 초기화)


def enQueue(item):
    global rear
    if isFull():
        pass
    else:
        rear += 1
        Q[rear] += item


def deQueue():
    global front
    if isEmpty():
        pass
    else:
        front += 1
        return Q[front]


def isEmpty():
    # return front == rear # T/F로 반환됨
    if front == rear:
        return True


def isFull():
    return rear == len(Q) - 1


def Qpeek():
    if isEmpty():
        pass
    else:
        return Q[front + 1]


# 원형 큐 : front와 rear을 0으로 초기화, 두 값이 같은 곳에 위치하지 않음
# front = (front + 1) / n
# rear = (rear + 1) / n
# 공백상태 : front = rear
# 포화상태 : (rear + 1) / n = front
