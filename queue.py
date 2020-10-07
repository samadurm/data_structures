import linked_list

class Queue:
    def __init__(self, front=None):
        self.values = linked_list.LinkedList()
        self.front = front
        self.back = front

    def enqueue(self, item):
        if self.front == None:
            self.values.append(item)
            self.front = item
        else:
            self.values.append(item)
        self.back = item

    def dequeue(self):
        if self.front == None:
            raise Exception('No items to dequeue')
        item = self.values.remove_front()
        self.front = self.values.get_value(0)
        return item

    def peek(self):
        return self.front

    def isEmpty(self):
        if self.front == None:
            return True
        return False

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    queue.enqueue(0)

    while not queue.isEmpty():
        print(queue.dequeue())

