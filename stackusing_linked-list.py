class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # Constructor to initialize the head of linked list
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.head
        self.head = newNode
        

    def pop(self):
        if (self.isEmpty()):
            return "Stack is Empty"
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.data



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print "% d is removed from stack" % (stack.pop())