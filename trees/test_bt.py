import unittest
from binary_tree import BinaryTree, Node

class TestBinTree(unittest.TestCase):
    def setUp(self):
        self.bin_tree = BinaryTree()

    def testAdd(self):
        self.bin_tree.Add(1)
        expected = Node(1)
        self.assertEqual(self.bin_tree.Find(1).getValue(), expected.getValue(), "find failed!")

    def testDelete(self):
        self.bin_tree.Add(5)

        self.bin_tree.Remove(5)
        self.assertEqual(self.bin_tree.Find(5), None, "delete failed!")

    def testFindLevelOne(self):
        self.bin_tree.Add(2)
        self.assertEqual(self.bin_tree.Find(2).getValue(), 2, "find failed!")

    def testFindTwoLevels(self):
        self.bin_tree.Add(3)
        self.bin_tree.Add(1)
        self.assertEqual(type(self.bin_tree.Find(3)), Node, "finding with 2 levels failed!")
        self.assertEqual(type(self.bin_tree.Find(1)), Node, "finding with 2 levels failed!")

    def testFindNonExisting(self):
        self.assertEqual(self.bin_tree.Find(40), None, "find a node not existing failed!")

    def testPreorder(self):
        data = [10,20,3,9,2,4,18,23,5]
        expected = [10,3,2,9,4,5,20,18,23]
        for i in data:
            self.bin_tree.Add(i)
        self.assertEqual(self.bin_tree.Preorder(), expected, "preorder function failed!")

    def testPostorder(self):
        data = [10,20,3,9,2,4,18,23,5]
        expected = [2,5,4,9,3,18,23,20,10]
        for i in data:
            self.bin_tree.Add(i)
        self.assertEqual(self.bin_tree.Postorder(), expected, "postorder function failed!")

    def testInorder(self):
        data = [10,20,3,9,2,4,18,23,5]
        expected = [2,3,4,5,9,10,18,20,23]

        for i in data:
            self.bin_tree.Add(i)

        self.assertEqual(self.bin_tree.inorder(),expected, "inorder function failed!")

    def testTreeHeight(self):
        data = [15,20,9,3,2,1,8]
        for i in data:
            self.bin_tree.Add(i)
        self.assertEqual(self.bin_tree.treeHeight(),5, "height function failed!")

if __name__ == "main":
    unittest.main()


