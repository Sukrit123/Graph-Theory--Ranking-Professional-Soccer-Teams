from numpy import matrix
from graph_tool.all import *
adj=matrix([[0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1],[0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,1],[0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1],[0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],[0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1],[1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0],[0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1],[1,1,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1],[0,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1],[0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0],[0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1],[0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1],[0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0],[0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1],[0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1],[0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0]])
print adj
g = graph_tool.Graph(directed = False)
g.add_vertex(len(adj))
edge_weights = g.new_edge_property('double')
for i in range(adj.shape[0]):
        for j in range(adj.shape[1]):
                if i > j and adj[i,j] != 0:
                    e = g.add_edge(i, j)
                    edge_weights[e] = adj[i,j]
 grph = {'1': ['2', '3', '4', '5', '6', '8', '10', '11', '12', '14', '15', '16', '17', '18', '19'],
             '2': ['3', '5', '6', '9', '10', '12', '13', '15', '16', '17', '19'],
             '3': ['4', '6', '7', '8', '9', '10', '13', '16', '17', '20'],
             '4': ['2', '5', '7', '12', '13', '14', '17', '19', '20'],
             '5': ['2', '3', '6', '8', '10', '11', '14', '15', '16', '17', '18', '19'],
             '6': ['4', '7', '8', '9', '10', '12', '14', '16', '20'],
             '7': ['1', '2', '8', '9', '10', '11', '15', '16', '18', '19' ],
             '8': ['2', '4', '9', '10', '12', '13', '15', '20'],
             '9': ['1', '10', '12', '13', '11', '15', '16', '20'],
             '10': ['2', '6', '7', '11', '12', '16', '19' ],
             '11': ['2', '3', '9', '10', '14', '15', '16', '18', '20' ],
             '12': ['4', '5', '20'],
             '13': ['1', '6', '7', '9', '10', '11', '15', '20' ],
             '14': ['6', '9', '11', '13', '16', '19', '20'],
             '15': ['2', '4', '8', '9', '10', '11', '12', '16', '20' ],
             '16': ['10' ],
             '17': ['4', '6', '8', '10', '11', '12', '13', '14', '16', '20'],
             '18': ['3', '6', '8', '9', '11', '14', '16', '18', '20'],
             '19': ['4', '7', '9', '10', '11', '15', '16''17', '20' ],
             '20': ['2', '11' ]
        }


def hamilpaths(grph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not grph.has_key(start):
            return []
        paths = []
        for node in grph[start]:
            if node not in path:
                npat = hamilpaths(grph, node, end, path)
                for newpath in npat:
                    paths.append(newpath)
        return paths
def findpath(grph):
    cycles=[]
    for firstnode in grph:
        for lastnode in grph:
            npat = hamilpaths(grph, firstnode, lastnode)
            for path in npat:
                if (len(path)==len(grph)):                    
                    cycles.append(path)
    return cycles

def cycl(grph):
    cycles=[]
    for firstnode in grph:
        for lastnode in grph:
            npat = hamilpaths(grph, firstnode, lastnode)
            for path in npat:
                if (len(path)==len(grph)):
                    if path[0] in grph[path[len(grph)-1]]:
                        path.append(path[0])
                        cycles.append(path)
    return cycles

print" hello"
hamil = findpath(grph)
print "hello"

for any in hamil:
    for hamil2 in any:
        print "hello"
        print hamil2, "-",
    print
print "The number of Hamiltonian paths is ", len(hamil)
print " "



