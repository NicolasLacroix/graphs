# encoding: utf-8

# author : Nicolas Lacroix


# TODO: define and compare traversal methods' performances (pre-order, post-order, in-order, generic)
# TODO: add self-balancing for addNode methods
# TODO: implement Depth-First Search (DFS) and Breadth-First Search (BFS) traversal methods

def checkParametersType(expectedTypes: tuple, parameters: tuple):
    if not all(isinstance(x, expectedTypes) for x in parameters):
        raise TypeError("Parameters must be of type : ", expectedTypes)


class Tree(object):
    """
    
    """
    
    def __init__(self, root=None, children: list = None):
        # TODO: add type hints for list elements
        self.root = root
        if children:
            self.children = children
        else:
            self.children = []

    def addNode(self, node):
        """Add node to the end of the graph
        
        :param node:
        :return:
        """
        # TODO: fix only adding to left branch
        if self.root:
            if len(self.children) > 0:
                # if the tree contains at least one branch
                self.children[0].addNode(node)
            else:
                self.children.append(Tree(node))
        else:
            self.root = node
    
    def removeNode(self, node):
        """Remove the first occurrence of the given node in the tree
        
        :param node:
        :return:
        """
        # TODO: check from leafs to root
        if self.containsNode(node):
            if self.root != node:
                for child in self.children:
                    # for each branch of the tree
                    if child.removeNode(node):
                        # if node was deleted in the current branch
                        return True
            elif len(self.children) > 0:
                # if the tree contains at least one branch
                self.root = self.children[0].root
                # recursively removing
                self.children[0].removeNode(self.root)
                return True
            else:
                self.root = None
                return True
        else:
            return False
    
    def containsNode(self, node):
        """Return whether the graph contains the given node or not
        
        :param node:
        :return:
        """
        if self.root == node:
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
        if isinstance(other, self.__class__) and self.root == other.root:
            if len(self.children) != len(other.children):
                return False
            return True and all(child.equals(otherChild) for child, otherChild in zip(self.children, other.children))
        return False


class BinaryTree(Tree):
    # TODO: to complete
    """
    
    """
    
    def __init__(self, root=None, leftChild=None, rightChild=None):
        children = []
        #  TODO: to improve
        if leftChild:
            self.leftChild = Tree(leftChild)
            children.append(self.leftChild)
        else:
            self.leftChild = leftChild
        if rightChild:
            self.rightChild = Tree(rightChild)
            children.append(self.rightChild)
        else:
            self.rightChild = rightChild
        super(BinaryTree, self).__init__(root, children)
    
    def addNode(self, node):
        """
        Overrides Tree's addNode method
        :param node:
        :return:
        """
        if self.root:
            if self.leftChild:
                self.leftChild.addNode(node)
            else:
                self.leftChild = Tree(node)
                self.children.append(self.leftChild)
        else:
            self.root = node


class BinarySearchTree(BinaryTree):
    """

    """
    
    def __init__(self, root: int = None, leftChild: int = None, rightChild: int = None):
        checkParametersType((int, type(None)), (root, leftChild, rightChild))
        if leftChild and rightChild:
            if leftChild == rightChild:
                raise ValueError("Can't have equal children.")
            # the min/max uses ensure that leftChild is lower than rightChild (BST rule)
            leftChild = min(leftChild, rightChild)
            rightChild = max(leftChild, rightChild)
        else:
            # if it has only one child, we set it as the left child
            leftChild = leftChild if leftChild else rightChild
            rightChild = None
        super(BinarySearchTree, self).__init__(root, leftChild, rightChild)
    
    def addNode(self, node: int):
        """

        :param node:
        :return:
        """
        checkParametersType((int, ), (node, ))
        if self.containsNode(node):
            raise ValueError("The BST already contains a node with the given value.")
        if self.root:
            if node < self.root:
                if self.leftChild:
                    self.leftChild.addNode(node)
                else:
                    self.leftChild = BinarySearchTree(node)
                    self.children.append(self.leftChild)
            else:
                if self.rightChild:
                    self.rightChild.addNode(node)
                else:
                    self.rightChild = BinarySearchTree(node)
                    self.children.append(self.rightChild)
        else:
            self.root = node
