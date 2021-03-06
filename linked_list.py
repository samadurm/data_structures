class DLinkedList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            self.prev = None
    
    def __init__(self, head=None):
        head_node = None
        if head != None:
            head_node = self.Node(head)
        self.head = head_node
        self.tail = head_node

    def append(self, item):
        node = self.Node(item)

        # handle empty case 
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            if self.head == None:
                self.head = node
                self.tail = node

            # O(1) operation
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def prepend(self, item):
        node = self.Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
        else:   
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def remove_front(self):
        # case where head == None
        if self.head == None:
            raise Exception('Cannot remove from empty list')

        # case where head == tail
        if self.tail.prev == None:
            cur = self.head
            self.head = None
            self.tail = None

            return cur.item

        # general case O(1)
        cur = self.head
        self.head = self.head.next
        self.head.prev = None

        return cur.item

    def remove_last(self):
        # handle case where tail is empty or tail = head
        if self.tail == None:
            raise Exception('No tail to remove last node from')
        
        # case where tail = head
        if self.tail.prev == None:
            cur = self.tail

            self.head.next = None
            self.tail.next = None

            self.head = None
            self.tail = None

            return cur.item

        # handle general case: O(1)
        cur = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return cur.item

    def remove_at(self, index):
        # handle case where list is empty
        if self.head == None:
            raise Exception('Cannot remove from empty list')
        # handle case where removing first
        elif index == 0:
            cur = self.head
            if self.head.next != None:
                self.head.next.prev = None
            self.head = self.head.next
            return cur.item

        # handle general case, time complexity: O(N)
        cur = self.head
        i = 0
        while i < index:
            if cur == None:
                raise Exception('Reached end of list without finding index')
            cur = cur.next
            i += 1 
        # remove the item
        cur.prev.next = cur.next
        if cur.next != None: # if not the last item
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev # else last item, update the tail
        return cur.item

    def insert_at(self, index, item):
        # handle case where inserting to an empty list
        if self.head == None and index != 0:
            raise Exception('Cannot insert to that index in an empty list')
        
        node = self.Node(item)
        if index == 0 and self.head == None:
            self.head = node
            self.tail = node

        # handle case where first item is the head 
        elif index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else: 
            # general case O(N)
            cur = self.head
            i = 0

            while i < index:
                if i == index - 1:
                    break
                elif cur.next == None:
                    raise Exception('Reached end of list before index to insert')
                cur = cur.next
                i += 1
            
            # reach index, now insert the item

            # check if adding to end of list
            if cur.next == None:
                cur.next = node
                node.prev = cur
                self.tail = node
            else:
                cur.next.prev = node
                node.next = cur.next
                cur.next = node

    def get_value(self, index):
        # handle case where list is empty
        if self.head == None:
            return None

        # handle general case. Time complexity: O(N)
        cur = self.head
        i = 0

        while cur != None:
            if i == index:
                return cur.item

            cur = cur.next
        raise Exception('Supplied index is out of bounds of the list')

    def contains_item(self, item):
        # handle case where empty list
        if self.head == None:
            return False
        # see if you can find at head or tail
        if self.head.item == item or self.tail.item == item:
            return True

        cur = self.head
        while cur.next != None:
            if cur.item == item:
                return True
            cur = cur.next

        return False

    def remove_item(self, item):
        if self.head == None:
            raise Exception('Cannot remove from empty list')
        
        # see if its in the head node or tail node before removal
        if self.head.item == item:
            val = self.head.item 
            self.head = self.head.next
            return val
        elif self.tail.item == item:
            val = self.tail.item
            self.tail.prev.next = None
            return val

        cur = self.head
        while cur != None:
            if cur.item == item:
                val = cur.item
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return val
            cur = cur.next

    def print_list(self):
        if self.head == None:
            print('Empty list')
        else:
            cur = self.head

            while cur != None:
                print(cur.item, end=' ')
                cur = cur.next
            print('')

class LinkedList:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
 
    def __init__(self, item=None):
        if item == None:
            self.head = None
        else:
            self.head = self.Node(item)
    
    def append(self, item) -> None:
        node = self.Node(item)

        if self.head == None:
            self.head = node
        else:
            cur = self.head

            while cur.next != None:
                cur = cur.next        
            cur.next = node
    
    def prepend(self, item) -> None:
        node = self.Node(item)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def remove_front(self):
        if self.head == None:
            raise Exception('Cannot remove front of empty list')

        cur = self.head 
        self.head = self.head.next

        return cur.val

    def remove_last(self):
        # if no head
        if self.head == None:
            raise Exception('Cannot remove last item of empty list')

        # if just removing head node
        if self.head.next == None:
            cur = self.head
            self.head = None
            return cur

        # must traverse list to get last node
        cur = self.head.next
        prev = self.head
        while cur.next != None:
            cur = cur.next
            prev = prev.next

        # reached end of list, remove last node
        prev.next = None
        return cur.val

    def remove_at(self, index):
        if self.head == None:
            raise Exception('Cannot remove from an empty list')

        # removing head node
        if index == 0:
            cur = self.head
            self.head = self.head.next
            return cur.val

        # if we are not removing head and there is no node after head
        cur = self.head.next
        if cur == None:
            raise Exception('There is no node after head')

        prev = self.head
        i = 1

        # traverse the list to find the head node
        while i < index:
            # go to the next item if there is an item to go to
            if cur.next == None:
                raise Exception('Could not find index to remove')

            cur = cur.next
            prev = prev.next 

            i += 1

        prev.next = cur.next
        return cur.val

    def insert_at(self, index, item):
        if self.head == None and index != 0:
            raise Exception('List has no head')

        node = self.Node(item)
        if index == 0:
            node.next = self.head
            self.head = node

        else:
            cur = self.head
            i = 0

            while i < index:
                if i == index - 1:
                    break
                elif cur.next == None:
                    raise Exception('Reached end of list before index to insert')

                cur = cur.next
                i += 1

            node.next = cur.next
            cur.next = node

    def get_value(self, index):
        if self.head == None:
            return None
        cur = self.head
        i = 0
        while i < index:
            if cur == None:
                raise Exception('Reached end of list without finding index')
            cur = cur.next
            i += 1 
        return cur.val

    def print_list(self):
        if self.head == None:
            print("Empty list!")
        else:
            cur = self.head

            while cur != None:
                print(cur.val, end=' ')
                cur = cur.next
            print('')


if __name__ == "__main__":
    llist = DLinkedList()

    llist.append(3)
    llist.print_list()
    llist.prepend(5)
    llist.print_list()
    llist.append(8)
    llist.print_list()