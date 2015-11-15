# -*- coding: utf-8 -*-


class binary_heap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def swap(self, a, b):
        self.heap_list[a], self.heap_list[b] = self.heap_list[b], self.heap_list[a]

    def min_child(self, i):
        if i*2+1 > self.current_size:
            return i*2
        else:
            return i*2 if self.heap_list[i*2] < self.heap_list[i*2+1] else i*2+1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.swap(i, i//2)
            else:
                break
            i // 2

    def percDown(self, i):
        while i*2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.swap(i, mc)
            else:
                break
            i = mc

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.percUp(self.current_size)

    def del_min(self):
        m = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.percDown(1)

        return m

    def find_min(self):
        return self.heap_list[1]

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
            

def heapsort(alist, size=None):
    bh = binary_heap()
    bh.build_heap(alist)
    ret = []
    if size is None:
        size = len(alist)
    for i in xrange(size):
        ret.append(bh.del_min())

    return ret


if __name__ == '__main__':
    alist = [9, 6, 5, 2, 3]
    bh = binary_heap()
    bh.build_heap(alist)
    for i in alist:
        print bh.del_min()
    
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    alist = heapsort(alist)
    print alist
