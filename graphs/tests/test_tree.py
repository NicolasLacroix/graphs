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
