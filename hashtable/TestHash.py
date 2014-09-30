import unittest
import hash


class TestHash(unittest.TestCase):
    def setUp(self):
        self.hashSize=100
        self.hashtable=hash.HashTable(self.hashSize)

    def testHashSize(self):
        self.assertEqual(self.hashtable.size, self.hashSize, "hashtable size incorrect!")

    def testHashFunc(self):
        self.assertEqual(self.hashtable.hash("charlotte"),66,"hash function not working")

    def testAdd(self):
        self.hashtable.add("charlotte","chocolate")
        self.assertEqual(self.hashtable.get("charlotte"),"chocolate","add function not working: hashed person not found")

    def testCollision(self):
        self.assertEqual(self.hashtable.hash("charlotte"),self.hashtable.hash("clewesze"), "hashes don't match")
        self.hashtable.add("charlotte","chocolate")
        self.hashtable.add("clewesze", "cake")
        self.assertEqual(self.hashtable.get("charlotte"),"chocolate", "collision handled incorrectly")
        self.assertEqual(self.hashtable.get("clewesze"),"cake", "collision handled incorrectly")

    def testHashUnique(self):
        self.assertNotEqual(self.hashtable.hash("charlotte"), self.hashtable.hash("frances"), "unexpected hash collision found")


    def testDisplay(self):
        expected_length = 100

if __name__ == '__main__':
    unittest.main()