class Node(object):
    def __init__(self, value):
        self.children = [None]*2
        self.val = value

    def getValue(self):
        return self.val

    def getLeft(self):
        return self.children[0]

    def getRight(self):
        return self.children[1]

    def setLeft(self, n):
        self.children[0] = n

    def setRight(self, n):
        self.children[1] = n

class BinaryTree(object):
    def __init__(self):
        self.head = None

    def Preorder(self):
        nodes=[]
        recurse=self.PreorderR(nodes,self.head)
        return recurse

    def PreorderR(self,nodes,curr):
        if curr is None:
            return
        nodes.append(curr.getValue())
        self.PreorderR(nodes,curr.getLeft())
        self.PreorderR(nodes,curr.getRight())
        return nodes

    def Postorder(self):
        nodes=[]
        return self.PostorderR(nodes, self.head)

    def PostorderR(self,nodes,curr):
        if curr is None:
            return

        self.PostorderR(nodes,curr.getLeft())
        self.PostorderR(nodes,curr.getRight())
        nodes.append(curr.getValue())
        return nodes

    def inorder(self):
        return self.inorderR([],self.head)

    def inorderR(self,nodes,curr):
        if curr is None:
            return

        self.inorderR(nodes,curr.getLeft())
        nodes.append(curr.getValue())
        self.inorderR(nodes,curr.getRight())
        return nodes

    def treeHeight(self):
        return self.TreeHeight(self.head)

    def TreeHeight(self, node):
        if node is None:
            return 0
        return max(self.TreeHeight(node.getLeft()),self.TreeHeight(node.getRight()))+1


    def Add(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            self.AddR(self.head, val)

    def AddR(self, root, val):
        if root is None:
            return None
        else:
            current = root.getValue()
            if val < current:
                if root.getLeft() is None:
                    root.setLeft(Node(val))
                else:
                    self.AddR(root.getLeft(), val)
            if val > current:
                if root.getRight() is None:
                    root.setRight(Node(val))
                else:
                    self.AddR(root.getRight(), val)

    def Find(self, val):
        return self.FindR(self.head, val)

    def FindR(self, root, val):
        if root is None:
            return None
        else:
            current = root.getValue()
            if current == val:
                return root
            if current < val:
                return self.FindR(root.getRight(), val)
            elif current > val:
                return self.FindR(root.getLeft(), val)

    def Remove(self, val):
        return self.RemoveR(self.head, val, None)

    def RemoveR(self, root, val, parent):
        if parent is None:
            self.head = None
        else:

            current = root.getValue()
            if current == val:
                if current == parent.getLeft():
                    parent.setLeft(current.getLeft())
                elif current == parent.getRight():
                    parent.setRight(current.getRight())
            else:
                if current < val:
                    self.RemoveR(current.getRight(), val, current)
                elif current > val:
                    self.RemoveR(current.getLeft(), val, current)