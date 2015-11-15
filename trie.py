# -*- coding: utf-8 -*-


class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.words = 0
        self.prefixes = 0
        self.edges = [None] * 26

    def get(self, char):
        index = ord(char.lower()) - ord('a')
        return self.edges[index]

    def set(self, char):
        index = ord(char.lower()) - ord('a')
        self.edges[index] = TrieNode(char.lower())


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, node=None):
        if node is None:
            node = self.root
        if len(word) == 0:
            node.words += 1
        else:
            node.prefixes += 1
            k = word[0]
            if node.get(k) is None:
                node.set(k)
            self.add_word(word[1:], node.get(k))

    def count_words(self, word, node=None):
        if node is None:
            node = self.root
        if len(word) == 0:
            return node.words
        else:
            k = word[0]
            if node.get(k) is None:
                return 0
            return self.count_words(word[1:], node.get(k))

    def count_prefixes(self, prefix, node=None):
        if node is None:
            node = self.root
        if len(prefix) == 0:
            return node.prefixes
        else:
            k = prefix[0]
            if node.get(k) is None:
                return 0
            return self.count_prefixes(prefix[1:], node.get(k))


if __name__ == '__main__':
    t = Trie()
    t.add_word('all')
    t.add_word('algorithm')
    t.add_word('also')
    t.add_word('association')
    print t.count_words('all')
    print t.count_prefixes('a')
