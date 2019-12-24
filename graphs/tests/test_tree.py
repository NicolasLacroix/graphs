# encoding: utf-8

import unittest

from graphs.graph import Tree


class GraphTest(unittest.TestCase):
    
    def setUp(self):
        self.tree = Tree()
        self.nodeA = "a"
        self.nodeB = "b"
        self.nodeC = "c"
    
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
        branches = [Tree("a1"), Tree("a2")]
        for i in range(9):
            branches[0].addNode("a"+str(i))
        for i in range(2):
            branches[1].addNode("b"+str(i))
        self.assertEqual(0, Tree().getMinDepth())
        self.assertEqual(0, Tree("A").getMinDepth())
        self.tree.children = branches
        self.assertEqual(minDepth, self.tree.getMinDepth())
    
    def testGetMaxDepth(self):
        maxDepth = 10
        branches = [Tree("a1"), Tree("a2")]
        for i in range(9):
            branches[0].addNode("a" + str(i))
        for i in range(2):
            branches[1].addNode("b" + str(i))
        self.assertEqual(0, Tree().getMaxDepth())
        self.assertEqual(0, Tree("A").getMaxDepth())
        self.tree.children = branches
        self.assertEqual(maxDepth, self.tree.getMaxDepth())
    
    def testRemoveNode(self):
        self.tree.addNode(self.nodeA)
        self.tree.addNode(self.nodeB)
        self.tree.removeNode("a")
        self.assertFalse(self.tree.containsNode(self.nodeA))
        self.tree.removeNode("b")
        self.assertFalse(self.tree.containsNode(self.nodeB))
        self.tree.removeNode("c")  # TODO: raise error


if __name__ == '__main__':
    unittest.main()
