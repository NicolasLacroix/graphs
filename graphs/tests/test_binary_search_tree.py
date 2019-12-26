# encoding: utf-8

import unittest

from graphs.graph import BinarySearchTree


# TODO: improve this test case

class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.tree = BinarySearchTree()
        self.nodeA = 5
        self.nodeB = 3
        self.nodeC = 8
        self.branches = [BinarySearchTree(self.nodeA), BinarySearchTree(self.nodeB)]
        
    def testRaises(self):
        # tests parameters handling
        with self.assertRaises(TypeError):
            BinarySearchTree("")
            BinarySearchTree(.2)
            BinarySearchTree([])
            BinarySearchTree(())
            BinarySearchTree({})
        # tests duplicate nodes
        self.tree.addNode(100)
        with self.assertRaises(ValueError):
            self.tree.addNode(100)
        
    def testAddNode(self):
        self.tree.addNode(self.nodeA)
        self.assertEqual(self.nodeA, self.tree.root)
        self.tree.addNode(self.nodeB)
        self.assertEqual(self.nodeB, self.tree.leftChild.root)
        self.assertEqual(self.nodeB, self.tree.children[0].root)
    
    def testContainsNode(self):
        self.tree.addNode(self.nodeA)
        self.tree.addNode(self.nodeB)
        self.assertTrue(self.tree.containsNode(self.nodeA))
        self.assertTrue(self.tree.containsNode(self.nodeB))
        self.assertFalse(self.tree.containsNode(self.nodeC))
    
    def testGetMinDepth(self):
        minDepth = 2
        self.tree.addNode(50)
        for i in range(1, 5):
            self.tree.addNode(50-i)
        for i in range(1, 3):
            self.tree.addNode(50+i)
        self.assertEqual(0, BinarySearchTree().getMinDepth())
        self.assertEqual(0, BinarySearchTree(self.nodeA).getMinDepth())
        self.assertEqual(minDepth, self.tree.getMinDepth())
    
    def testGetMaxDepth(self):
        maxDepth = 10
        for i in range(9):
            self.tree.addNode(100 + i)
        for i in range(2):
            self.tree.addNode(200 + i)
        self.assertEqual(0, BinarySearchTree().getMaxDepth())
        self.assertEqual(0, BinarySearchTree(self.nodeA).getMaxDepth())
        self.assertEqual(maxDepth, self.tree.getMaxDepth())
    
    def testRemoveNode(self):
        self.tree.addNode(self.nodeA)
        self.tree.addNode(self.nodeB)
        self.tree.removeNode(self.nodeA)
        self.assertFalse(self.tree.containsNode(self.nodeA))
        self.tree.removeNode(self.nodeB)
        self.assertFalse(self.tree.containsNode(self.nodeB))
    
    def testEquals(self):
        # tests equals between different types
        self.assertFalse(self.tree.equals(None))
        self.assertFalse(self.tree.equals(True))
        self.assertFalse(self.tree.equals("a"))
        self.assertFalse(self.tree.equals(1))
        # tests equals with (node = None)
        self.assertTrue(self.tree.equals(BinarySearchTree()))
        # tests equals with (len(branches) == 0)
        self.tree.addNode(self.nodeA)
        self.assertTrue(self.tree.equals(self.branches[0]))
        self.assertFalse(self.tree.equals(self.branches[1]))
        # tests equals with (len(branches) > 0)
        self.tree.addNode(self.nodeB)
        self.tree.addNode(self.nodeC)
        self.branches[0].addNode(self.nodeB)
        self.branches[0].addNode(self.nodeC)
        self.assertTrue(self.tree.equals(self.branches[0]))
        self.branches[1].addNode(self.nodeA)
        self.branches[1].addNode(self.nodeC)
        self.assertFalse(self.tree.equals(self.branches[1]))
        # tests equals with different lengths of branches
        self.branches[0].addNode(1000)
        self.assertFalse(self.tree.equals(self.branches[0]))


if __name__ == '__main__':
    unittest.main()
