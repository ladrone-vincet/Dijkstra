from alg_dijkstra import * as GDijkstra

graph = GDijkstra.Graph()

for i in range(6):
	graph.add_node(i)

graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 5, 14)

graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)

graph.add_edge(2, 3, 11)
graph.add_edge(2, 5, 2)

graph.add_edge(4, 3, 6)
graph.add_edge(4, 5, 9)

print( dijkstra(graph, 1) )

