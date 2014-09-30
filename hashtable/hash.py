from LinkedList import LinkedList

class HashTable(object):
    def __init__(self, size):
        self.size=size
        self.table = [LinkedList(None)]*self.size

    def hash(self, key):
        return sum([ord(k) for k in key])%self.size
    def add(self,key, value):
        index = self.hash(key)
        self.table[index].add(key, value)

    def get(self, key):
        index = self.hash(key)
        return self.table[index].find(key)


    def Display(self):
        return None
