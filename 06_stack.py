class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        # 어떻게 하면 될까요?


    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is Empty"
        delete_head = self.head
        self.head = self.head.next

        return delete_head

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?

        return self.head is None

stack = Stack()
stack.push(3)
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.pop().data)
print(stack.is_empty())