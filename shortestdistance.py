import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint       
        self.visited = False  
        self.previous = None

    def createadjacent(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def link(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def weight(self, neighbor):
        return self.adjacent[neighbor]

    def setdist(self, dist):
        self.distance = dist

    def dist(self):
        return self.distance

    def prev(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def addvertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def getvertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def newedge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.addvertex(frm)
        if to not in self.vert_dict:
            self.addvertex(to)

        self.vert_dict[frm].createadjacent(self.vert_dict[to], cost)
        self.vert_dict[to].createadjacent(self.vert_dict[frm], cost)

    def showvertex(self):
        return self.vert_dict.keys()

    def prev(self, current):
        self.previous = current

    def getprevious(self, current):
        return self.previous

def shortest(v, path):
    ''' Shortest Past is made from previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(grph, x, final):
    print '''Dijkstra's shortest path'''
    
    x.setdist(0)

    
    unvisited_queue = [(v.dist(),v) for v in grph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

       
        for next in current.adjacent:
            
            if next.visited:
                continue
            new_dist = current.dist() + current.weight(next)
            
            if new_dist < next.dist():
                next.setdist(new_dist)
                next.prev(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.dist())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.dist())

        
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        
        unvisited_queue = [(v.dist(),v) for v in grph if not v.visited]
        heapq.heapify(unvisited_queue)
    
if __name__ == '__main__':

    g = Graph()

    g.addvertex('a')
    g.addvertex('b')
    g.addvertex('c')
    g.addvertex('d')
    g.addvertex('e')
    g.addvertex('f')

    g.newedge('a', 'b', 7)  
    g.newedge('a', 'c', 9)
    g.newedge('a', 'f', 14)
    g.newedge('b', 'c', 10)
    g.newedge('b', 'd', 15)
    g.newedge('c', 'd', 11)
    g.newedge('c', 'f', 2)
    g.newedge('d', 'e', 6)
    g.newedge('e', 'f', 9)

    print 'Graph data:'
    for v in g:
        for w in v.link():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.weight(w))

    dijkstra(g, g.getvertex('a'), g.getvertex('e')) 

    final = g.getvertex('e')
    path = [final.get_id()]
    shortest(final, path)
    print 'The shortest path : %s' %(path[::-1])
