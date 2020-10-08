from collections import deque

class Stack:
    _size = None
    _items = None

    # constructor
    def __init__(self):
        self._size = 0
        self._items = deque()

    # push operation
    def push(self, item) -> None:
        self._items.append(item)
        self._size += 1

    # pop operation
    def pop(self):
        if self._size == 0:
            raise Exception('Cannot pop from empty stack')

        self._size -= 1
        return self._items.pop()
            
    # peek
    def peek(self):
        if self._size == 0:
            raise Exception('Stack is empty')
        val = self._items.pop()
        self._items.append(val)
        return val
    
    # isEmpty operation
    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def get_size(self):
        return self._size

def reverseString(string: str) -> str:
    
    stack = Stack()
    strList = list(string)

    for c in strList:
        stack.push(c)

    for i in range(len(strList)):
        strList[i] = stack.pop()

    return "".join(strList)


if __name__ == "__main__":
    myStack = Stack()