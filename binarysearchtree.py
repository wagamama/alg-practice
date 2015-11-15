# -*- coding: utf-8 -*-
import weakref


class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.replace(key, value, left, right)
        self.parent = None
        if parent is not None:
            self.parent = weakref.ref(parent)

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def is_left(self):
        return self.get_parent() is not None and self.parent().left == self

    def is_right(self):
        return self.get_parent() is not None and self.parent().right == self

    def is_root(self):
        return self.get_parent() is None

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_any_children(self):
        return not self.is_leaf()

    def has_both_children(self):
        return self.left is not None and self.right is not None

    def get_parent(self):
        if self.parent is not None:
            return self.parent()
        else:
            return None

    def set_left(self, node):
        self.replace(self.key, self.value, left=node, right=self.right)

    def set_right(self, node):
        self.replace(self.key, self.value, left=self.left, right=node)

    def replace(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.parent = weakref.ref(self)
        if self.right is not None:
            self.right.parent = weakref.ref(self)

    def find_successor(self):
        succ = None
        if self.has_right():
            succ = self.right.find_min()
        else:
            if self.is_left():
                succ = self.get_parent()
            elif self.is_right():
                self.get_parent().set_right(None)
                succ = self.get_parent().find_successor()
                self.get_parent().set_right(self)
        return succ
    
    def find_min(self):
        node = self
        while node.has_left():
            node = node.left
        return node

    def splice_out(self):
        if self.is_leaf():
            if self.is_left():
                self.get_parent().set_left(None)
            elif self.is_right():
                self.get_parent().set_right(None)
        elif self.has_any_children():
            if self.has_left():
                if self.is_left():
                    self.get_parent().set_left(self.left)
                else:
                    self.get_parent().set_right(self.left)
            else:
                if self.is_left():
                    self.get_parent().set_left(self.right)
                else:
                    self.get_parent().set_right(self.right)

    def __iter__(self):
        if self:
            if self.has_left():
                for elem in self.left:
                    yield elem
            yield self
            if self.has_right():
                for elem in self.right:
                    yield elem


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root is not None:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current):
        if key < current.key:
            if current.has_left():
                self._put(key, value, current.left)
            else:
                current.set_left(TreeNode(key, value))
        else:
            if current.has_right():
                self._put(key, value, current.right)
            else:
                current.set_right(TreeNode(key, value))

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        node = self._get(key, self.root)
        if node is not None:
            return node.value
        else:
            return None

    def _get(self, key, current):
        if current is None:
            return None
        elif key == current.key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, k):
        return True if self._get(k, self.root) is not None else False

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node is not None:
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError('no such key in tree')
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('no such key in tree')

    def __delitem__(self, k):
        self.delete(k)

    def remove(self, node):
        if node.is_leaf():
            parent = node.get_parent()
            if node.is_left():
                parent.set_left(None)
            elif node.is_right():
                parent.set_right(None)
            else:  # only root
                self.root = None
        elif node.has_both_children():
            succ = node.find_successor()
            succ.splice_out()
            node.replace(succ.key, succ.value, node.left, node.right)
        else:
            if node.has_left():
                if node.is_left():
                    node.get_parent().set_left(node.left)
                elif node.is_right():
                    node.get_parent().set_right(node.left)
                else:
                    node.replace(node.left.key, node.left.value, node.left.left, node.left.right)
            elif node.has_right():
                if node.is_left():
                    node.get_parent().set_left(node.right)
                elif node.is_right():
                    node.get_parent().set_right(node.right)
                else:
                    node.replace(node.right.key, node.right.value, node.right.left, node.right.right)


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[17] = 'red'
    mytree[5] = 'blue'
    mytree[35] = 'yellow'
    mytree[2] = 'at'
    mytree[11] = ''
    mytree[29] = ''
    mytree[38] = ''
    mytree[9] = ''
    mytree[16] = ''
    mytree[7] = ''
    mytree[8] = ''
    del mytree[5]

    for node in mytree.root:
        p = node.get_parent().key if not node.is_root() else None
        l = node.left.key if node.has_left() else None
        r = node.right.key if node.has_right() else None
        print '[{}]{}, P={}, L={}, R={}'.format(node.key, node.value, p, l, r)
