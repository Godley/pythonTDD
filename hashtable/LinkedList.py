from Node import Node

class LinkedList(object):
    def __init__(self, node1):
        self.first = node1

    def printme(self):
        node1=self.first
        while node1 is not None:
            print node1.GetKey()
            print node1.GetValue()
            node1=node1.Next()

    def next(self):
        return self.first

    def add(self, key, value):
        last_node = self.first
        if last_node is None:
            self.first = Node(key, value)
            return 1
        while last_node is not None:
            current = last_node
            try:
                last_node = last_node.Next()
            except:
                break
        current.append(Node(key, value))
        return 1

    def find(self, key):
        elem = self.first
        if elem is None:
            return None
        elif elem.GetKey() == key:
            return elem.GetValue()
        while elem is not None:
            if elem.GetKey() == key:
                return elem.GetValue()
            else:
                elem=elem.Next()

