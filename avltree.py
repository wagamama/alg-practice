# -*- coding: utf-8 -*-
from binarysearchtree import TreeNode, BinarySearchTree


class AVLNode(TreeNode):
    def __init__(self, key, value, left=None, right=None, parent=None):
        super(AVLNode, self).__init__(key, value, left, right, parent)
        self.balance_factor = 0


class AVLTree(BinarySearchTree):
    def put(self, key, value):
        if self.root is not None:
            self._put(key, value, self.root)
        else:
            self.root = AVLNode(key, value)
        self.size += 1

    def _put(self, key, value, current):
        if key < current.key:
            if current.has_left():
                self._put(key, value, current.left)
            else:
                current.set_left(AVLNode(key, value))
                self.update_balance(current.left)
        else:
            if current.has_right():
                self._put(key, value, current.right)
            else:
                current.set_right(AVLNode(key, value))
                self.update_balance(current.right)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        
        if node.is_left():
            node.get_parent().balance_factor += 1
        elif node.is_right():
            node.get_parent().balance_factor -= 1

        if node.get_parent() is not None and node.get_parent().balance_factor != 0:
            self.update_balance(node.get_parent())

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
            self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
            self.rotate_right(node)

    def rotate_left(self, rot_root):
        new_root = rot_root.right
        children = new_root.left

        if rot_root.is_left():
            rot_root.get_parent().set_left(new_root)
        elif rot_root.is_right():
            rot_root.get_parent().set_right(new_root)
        else:
            new_root.parent = None
            self.root = new_root

        new_root.set_left(rot_root)
        rot_root.set_right(children)

        rot_root.balance_factor += 1 - min(0, new_root.balance_factor)
        new_root.balance_factor += 1 + max(0, rot_root.balance_factor)

    def rotate_right(self, rot_root):
        new_root = rot_root.left
        children = new_root.right

        if rot_root.is_left():
            rot_root.get_parent().set_left(new_root)
        elif rot_root.is_right():
            rot_root.get_parent().set_right(new_root)
        else:
            new_root.parent = None
            self.root= new_root

        new_root.set_right(rot_root)
        rot_root.set_left(children)

        rot_root.balance_factor += -1 - max(0, new_root.balance_factor)
        new_root.balance_factor += -1 + min(0, rot_root.balance_factor)


if __name__ == '__main__':
    t = AVLTree()
    t[17] = ''
    t[5] = ''
    t[35] = ''
    t[2] = ''
    t[11] = ''
    t[29] = ''
    t[38] = ''
    t[9] = ''
    t[16] = ''
    t[7] = ''
    t[8] = ''

    for node in t.root:
        p = node.get_parent().key if not node.is_root() else None
        f = node.balance_factor
        l = node.left.key if node.has_left() else None
        r = node.right.key if node.has_right() else None
        print '[{}]{}, f={}, P={}, L={}, R={}'.format(node.key, node.value, f, p, l, r)
