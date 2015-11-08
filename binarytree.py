# -*- coding: utf-8 -*-
import weakref


class BinaryTree(object):
    def __init__(self, root, parent=None):
        self.key = root
        if parent is not None:
            self.weak_parent = weakref.ref(parent)
        else:
            self.weak_parent = None
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node, parent=self)
        else:
            tree = BinaryTree(node, parent=self)
            tree.insert_left(self.left)
            self.left = tree

    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node, parent=self)
        else:
            tree = BinaryTree(node, parent=self)
            tree.insert_right(self.right)
            self.right = tree

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root(self, root):
        self.key = root

    def get_root(self):
        return self.key

    def get_parent(self):
        if self.weak_parent is not None:
            return self.weak_parent()
        else:
            return None

    def preorder(self):
        print self.key
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print self.key

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print self.key
        if self.right is not None:
            self.right.inorder()


if __name__ == '__main__':
    r = BinaryTree('a')
    print r.get_root()
    print r.get_left()
    r.insert_left('b')
    print r.get_left()
    print r.get_left().get_root()
    r.insert_right('c')
    print r.get_right()
    print r.get_right().get_root()
    r.get_right().set_root('hello')
    print r.get_right().get_root()
