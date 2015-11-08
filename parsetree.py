# -*- coding: utf-8 -*-
from binarytree import BinaryTree


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    pStack = []
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insert_left('')
            pStack.append(currentTree)
            currentTree = currentTree.get_left()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.set_root(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.set_root(i)
            currentTree.insert_right('')
            pStack.append(currentTree)
            currentTree = currentTree.get_right()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree

def build_parse_tree2(fpexp):
    fplist = fpexp.split()
    eTree = BinaryTree('')
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insert_left('')
            currentTree = currentTree.get_left()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.set_root(int(i))
            currentTree = currentTree.get_parent()
        elif i in ['+', '-', '*', '/']:
            currentTree.set_root(i)
            currentTree.insert_right('')
            currentTree = currentTree.get_right()
        elif i == ')':
            currentTree = currentTree.get_parent()
        else:
            raise ValueError

    return eTree


if __name__ == '__main__':
    pt = build_parse_tree2('( ( 10 + 5 ) * 3 )')
    pt.postorder()
