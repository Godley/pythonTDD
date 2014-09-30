class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def GetKey(self):
        return self.key

    def GetValue(self):
        return self.value

    def Next(self):
        return self.next

    def append(self, node):
        self.next = node
