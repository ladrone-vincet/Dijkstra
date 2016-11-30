import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from py_alg_dat.graph import DirectedWeightedGraph
from py_alg_dat.graph_vertex import UnWeightedGraphVertex
from py_alg_dat.graph_algorithms import GraphAlgorithms

def create_graph():
     """
     Creates a Directed Weighted Graph
     """
     # Create an empty directed weighted graph
     graph = DirectedWeightedGraph(6)

     # Create vertices
     vertex0 = UnWeightedGraphVertex(graph, "A")
     vertex1 = UnWeightedGraphVertex(graph, "B")
     vertex2 = UnWeightedGraphVertex(graph, "C")
     vertex3 = UnWeightedGraphVertex(graph, "D")
     vertex4 = UnWeightedGraphVertex(graph, "E")
     vertex5 = UnWeightedGraphVertex(graph, "F")

     # Add vertices
     graph.add_vertex(vertex0)
     graph.add_vertex(vertex1)
     graph.add_vertex(vertex2)
     graph.add_vertex(vertex3)
     graph.add_vertex(vertex4)
     graph.add_vertex(vertex5)

     # Add edges
     graph.add_edge(vertex0, vertex1, 7)   # ( A <- B, 7 )
     graph.add_edge(vertex0, vertex2, 9)   # ( A <- C, 9 )
     graph.add_edge(vertex0, vertex5, 14)   # ( A <- F, 14 )
     graph.add_edge(vertex1, vertex2, 10)   # ( B <- C, 10 )
     graph.add_edge(vertex1, vertex3, 15)   # ( B <- D, 15 )
     graph.add_edge(vertex2, vertex3, 11)   # ( C <- D, 2 )
     graph.add_edge(vertex2, vertex5, 2)   # ( C <- F, 2 )
     graph.add_edge(vertex3, vertex1, 15)
     graph.add_edge(vertex3, vertex2, 11)
     graph.add_edge(vertex3, vertex4, 6)
     graph.add_edge(vertex4, vertex5, 9)   # ( E <- F, 2 )
     graph.add_edge(vertex4, vertex3, 6)   # ( E <- D, 2 )
     graph.add_edge(vertex5, vertex1, 14)
     graph.add_edge(vertex5, vertex2, 2)

     return graph





# Create the graph
GRAPH = create_graph()
# Run Dijkstra starting at vertex "A"
TABLE = GraphAlgorithms.dijkstras_algorithm(GRAPH, GRAPH[0])
# Find the edges in the Spanning Tree and its total weight
SPANNING_TREE_EDGES = set()
SPANNING_TREE_WEIGHT = 0
for i in xrange(len(TABLE)):
   entry = TABLE[i]
   if entry.predecessor != None:
       edge = entry.edge
       SPANNING_TREE_EDGES.add(edge)
       SPANNING_TREE_WEIGHT += edge.get_weight()
print "Edges in Spanning Tree: " + str(SPANNING_TREE_EDGES)
print "Weight of Spanning Tree: " + str(SPANNING_TREE_WEIGHT)
PATH = GraphAlgorithms.shortest_path(GRAPH, GRAPH[0], GRAPH[int(sys.argv[1]) - 1])
# Find the edges in the Spanning Tree and its total weight
print PATH
