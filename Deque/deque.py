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
        elif self.tail is None:
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
        elif ex_head.next is not None:
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

    def get_front(self):
        return self.head.data

    def get_back(self):
        return self.tail.data

    def to_list(self):
        output = list()
        curr = self.head
        while curr is not None:
            output.append(curr.data)
            curr = curr.next
        return output

    def is_empty(self):
        if self.head is None:
            print('Deque is Empty')
        else:
            print('Deque is not Empty')
        return

    def clear(self):
        self.head = None
        return

    def search_element(self, el):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            if el == curr.data:
                return el, count

            curr = curr.next


if __name__ == '__main__':
    dq = Deque()
    dq.is_empty()

    dq.push_front(1)
    dq.push_front(2)
    dq.push_front(6)
    dq.push_front(5)
    dq.push_front(2)

    print(dq.search_element(5))
