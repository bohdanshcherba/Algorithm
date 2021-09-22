class Deque:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_value):
        new_node = self.Node(new_value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        if self.tail is None:
            self.tail = new_node
        self.head = new_node

    def push_back(self, new_value):
        new_node = self.Node(new_value)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node

    def pop_front(self):
        ex_head = self.head
        if self.head is None:
            return
        if ex_head.next is not None:
            ex_head.next.prev = None
        else:
            self.tail = None
        self.head = ex_head.next
        return ex_head.data

    def pop_back(self):
        ex_tail = self.tail
        if self.tail is None:
            return
        if ex_tail.prev is not None:
            ex_tail.prev.next = None
        else:
            self.head = None
        self.tail = ex_tail.prev
        return ex_tail.data

    def deque_to_list(self):
        output = list()
        curr = self.head
        while curr is not None:
            output.append(curr.data)
            curr = curr.next
        return output


if __name__ == '__main__':
    dq = Deque()

    dq.push_front(5)
    dq.push_front(2)
    dq.push_front(1)
    print(dq.deque_to_list())

    dq.push_back(6)
    dq.push_back(8)
    print(dq.deque_to_list())


    dq.pop_back()
    dq.pop_front()
    print(dq.deque_to_list())
