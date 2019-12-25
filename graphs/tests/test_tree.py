# encoding: utf-8

import unittest

from graphs.graph import Tree


class GraphTest(unittest.TestCase):
    
    def setUp(self):
        self.tree = Tree()
        self.nodeA = "a"
        self.nodeB = "b"
        self.nodeC = "c"
        self.branches = [Tree("a1"), Tree("a2")]
    
    def testAddNode(self):
        self.tree.addNode(self.nodeA)
        self.assertEqual(self.nodeA, self.tree.node)
        self.tree.addNode(self.nodeB)
        self.assertEqual(self.nodeB, self.tree.children[0].node)
        # self.assertEqual(Graph(self.nodeA), self.graph.graph) TODO: add equals for Graph
    
    def testContainsNode(self):
        self.tree.addNode(self.nodeA)
        self.tree.addNode(self.nodeB)
        self.assertTrue(self.tree.containsNode(self.nodeA))
        self.assertTrue(self.tree.containsNode(self.nodeB))
        self.assertFalse(self.tree.containsNode(self.nodeC))
        
    def testGetMinDepth(self):
        minDepth = 3
        for i in range(9):
            self.branches[0].addNode("a"+str(i))
        for i in range(2):
            self.branches[1].addNode("b"+str(i))
        self.assertEqual(0, Tree().getMinDepth())
        self.assertEqual(0, Tree("A").getMinDepth())
        self.tree.children = self.branches
        self.assertEqual(minDepth, self.tree.getMinDepth())
    
    def testGetMaxDepth(self):
        maxDepth = 10
        for i in range(9):
            self.branches[0].addNode("a" + str(i))
        for i in range(2):
            self.branches[1].addNode("b" + str(i))
        self.assertEqual(0, Tree().getMaxDepth())
        self.assertEqual(0, Tree("A").getMaxDepth())
        self.tree.children = self.branches
        self.assertEqual(maxDepth, self.tree.getMaxDepth())
    
    def testRemoveNode(self):
        self.tree.addNode(self.nodeA)
        self.tree.addNode(self.nodeB)
        self.tree.removeNode("a")
        self.assertFalse(self.tree.containsNode(self.nodeA))
        self.tree.removeNode("b")
        self.assertFalse(self.tree.containsNode(self.nodeB))
        self.tree.removeNode("c")
        
    def testEquals(self):
        # tests equals between different types
        self.assertFalse(self.tree.equals(None))
        self.assertFalse(self.tree.equals(True))
        self.assertFalse(self.tree.equals("a"))
        self.assertFalse(self.tree.equals(1))
        # tests equals with (node = None)
        self.assertTrue(self.tree.equals(Tree()))
        # tests equals with (len(branches) == 0)
        self.tree.addNode("a1")
        self.assertTrue(self.tree.equals(self.branches[0]))
        self.assertFalse(self.tree.equals(self.branches[1]))
        # tests equals with (len(branches) > 0)
        self.tree.addNode("b1")
        self.tree.addNode("c1")
        self.branches[0].addNode("b1")
        self.branches[0].addNode("c1")
        self.assertTrue(self.tree.equals(self.branches[0]))
        self.branches[1].addNode("b1")
        self.branches[1].addNode("c2")
        self.assertFalse(self.tree.equals(self.branches[1]))
        # tests equals with different lengths of branches
        self.branches[0].addNode("d1")
        self.assertFalse(self.tree.equals(self.branches[0]))


if __name__ == '__main__':
    unittest.main()
