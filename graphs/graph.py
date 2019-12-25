# encoding: utf-8

# author : Nicolas Lacroix


# TODO: define and compare traversal methods' performances (pre-order, post-order, in-order, generic)

class Tree(object):
    """
    
    """
    
    def __init__(self, node=None, children: list = None):
        self.node = node
        if children:
            self.children = children
        else:
            self.children = []
    
    def addNode(self, node):
        """Add node to the end of the graph
        
        :param node:
        :return:
        """
        if self.node:
            if len(self.children) > 0:
                # if the tree contains at least one branch
                self.children[0].addNode(node)
            else:
                self.children.append(Tree(node))
        else:
            self.node = node
    
    def removeNode(self, node):
        """Remove the first occurrence of the given node in the tree
        
        :param node:
        :return:
        """
        if self.containsNode(node):
            if self.node != node:
                for child in self.children:
                    # for each branch of the tree
                    if child.removeNode(node):
                        # if node was deleted in the current branch
                        return True
            elif len(self.children) > 0:
                # if the tree contains at least one branch
                self.node = self.children[0].node
                # recursively removing
                self.children[0].removeNode(self.node)
                return True
            else:
                self.node = None
                return True
        else:
            return False
    
    def containsNode(self, node):
        """Return whether the graph contains the given node or not
        
        :param node:
        :return:
        """
        if self.node == node:
            return True
        else:
            for child in self.children:
                # for each branch of the tree
                if child.containsNode(node):
                    return True
        return False
    
    def getMinDepth(self):
        """Return the minimal depth of current tree's branches
        
        :return: 
        """
        if len(self.children) > 0:
            return 1 + min([child.getMinDepth() for child in self.children])
        else:
            return 0
    
    def getMaxDepth(self):
        """Return the maximal depth of current tree's branches
        
        :return:
        """
        if len(self.children) > 0:
            return 1 + max([child.getMaxDepth() for child in self.children])
        else:
            return 0
    
    def equals(self, other):
        """Return whether other equals self or not
        
        :param other:
        :return:
        """
        if isinstance(other, self.__class__) and self.node == other.node:
            if len(self.children) != len(other.children):
                return False
            return True and all(child.equals(otherChild) for child, otherChild in zip(self.children, other.children))
        return False
