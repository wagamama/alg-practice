# -*- coding: utf-8 -*-


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connect = {}
        self.reset()

    def add_neighbor(self, nbr, weight=0):
        self.connect[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connect: ' + str([x.id for x in self.connect])

    def get_connections(self):
        return self.connect.keys()

    def get_weight(self, nbr):
        return self.connect[nbr]

    def reset(self):
        self.color = 'white'
        self.pred = None
        self.distance = 0
        self.discovery = 0
        self.finish = 0


class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.size = 0
        self.time = 0

    def add_vertex(self, key):
        self.size += 1
        v = Vertex(key)
        self.vertices[key] = v
        return v

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def reset_all(self):
        for v in self.vertices.values():
            v.reset()

    def bfs(self, key):
        self.reset_all()
        start = self.vertices[key]
        queue = []
        queue.append(start)
        while len(queue) > 0:
            current = queue.pop(0)
            for nbr in current.get_connections():
                if nbr.color == 'white':
                    nbr.color == 'gray'
                    nbr.distance = current.distance + 1
                    nbr.pred = current
                    queue.append(current)
            current.color = 'black'

    def dfs(self, key):
        self.reset_all()
        self.time = 0
        start = self.vertices[key]
        self.dfs_visit(start)

    def dfs_visit(self, current):
        current.color = 'gray'
        self.time += 1
        current.discovery = self.time
        for nbr in current.get_connections():
            if nbr.color == 'white':
                nbr.pred = current
                self.dfs_visit(nbr)
        current.color = 'black'
        self.time += 1
        current.finish = self.time


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print g.vertices

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connections():
            print '({}, {})[{}]'.format(v.id, w.id, v.get_weight(w))
