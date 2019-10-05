#stack data str.  uses LIFO or FILO order
# push, pop, peek or top,isempty all are O(n) operations as we are not looping


def createstack():
    stack = []
    return stack
def isempty(): # this will check whether the stack is empty or not if the length of stack is zero that means stack is empty
    return len(stack)==0
    
    # if len(stack)== 0:
    #     return True
    # else:
    #     return False

def push(stack, anyvalue): # we are just pushing the value in Stack
    stack.append(anyvalue)

def pop(stack): # to remove item from stack
    if len(stack)==0:
        return "Stack is Empty"
    return stack.pop()

def peek(stack):
    if len(stack)==0:
        return "stack is Empty"
    return stack[len(stack)-1]

stack = createstack()
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(pop(stack) + " popped from stack") 



