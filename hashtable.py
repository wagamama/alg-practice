# -*- coding: utf-8 -*-


class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        if self.slot[hashvalue] == None:
            self.slot[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slot[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue)
                while self.slot[nextslot] is not None and self.slot[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slot[nextslot] == None:
                    self.slot[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size

    def get(self, key):
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slot[position] != None and not stop and not found:
            if self.slot[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        self.put(key, None)


if __name__ == '__main__':
    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    print h.slot
    print h.data
    print h[20]
    print h[17]
    h[20] = 'duck'
    print h[20]
    print h.data
    del h[20]
    print h[20]
    print h.data
