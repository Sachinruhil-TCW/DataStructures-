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
        print
        "% d pushed to stack" % (data)

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.head.data

    # Driver program to test above class


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print "% d popped from stack" % (stack.pop())