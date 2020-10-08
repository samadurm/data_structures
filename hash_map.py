from linked_list import DLinkedList
import random

class HashMap:

    def __init__(self, size=None):
        self.size = size
        if self.size == None:
            self.size = 100
        self.buckets = [None] * self.size
        for i in range(self.size):
            self.buckets[i] = DLinkedList()
        
    def hash_function(self, key):
        return key % self.size

    def add(self, key):
        self.buckets[self.hash_function(key)].append(key)

    def contains(self, key):
        if self.buckets[self.hash_function(key)].contains_item(key):
            return True
        else:
            return False

    def delete(self, key):
        self.buckets[self.hash_function(key)].remove_item(key)

    def print_map(self):
        for i in range(len(self.buckets)):
            self.buckets[i].print_list()



if __name__ == "__main__":
    myMap = HashMap()

    for i in range(1000):
        myMap.add(random.randint(1, 1000))

    myMap.print_map()
