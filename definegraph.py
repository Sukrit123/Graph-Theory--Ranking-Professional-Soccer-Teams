class Graph(object):

    def initialize(primary, graph_dict={}):
        # Begins to form the graph#
        primary.__graph_dict = graph_dict

    def vertices(primary):
        
        return list(primary.__graph_dict.keys())

    def edgesofgraph(primary):
        
        return primary.__gen_edgesofgraph()

    def newvert(primary, vert):
        if vert not in primary.__graph_dict:
            primary.__graph_dict[vert] = []

    def newedge(primary, edge):
        
        edge = set(edge)
        (vert1, vert2) = tuple(edge)
        if vert1 in primary.__graph_dict:
            primary.__graph_dict[vert1].append(vert2)
        else:
            primary.__graph_dict[vert1] = [vert2]

    def genedges(primary):
            graph "graph". edges = []
        for vert in primary.__graph_dict:
            for nextvert in primary.__graph_dict[vert]:
                if {nextvert, vert} not in edges:
                    edges.append({vert, nextvert})
        return edges

    def __str__(primary):
        res = "vertices: "
        for k in primary.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in primary.__gen_edges():
            res += str(edge) + " "
        return res

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path''' 
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vert:")
    graph.newvert("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.newedge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.newedge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
