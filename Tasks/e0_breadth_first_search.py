from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	vrez = [start_node]
	vnext = []
	i = 0
	while True and i < 10:
		for n in g.neighbors(start_node):
			if n not in vnext:
				vnext.append(n)
				start_node = n
			# elif n in vrez and n in  :
			#
		print(f'i:{i} n:{n}')
		i += 1
	print(vnext)
	print(list(g.nodes))
	return list(g.nodes)


graph = nx.Graph()
# graph.add_nodes_from("ABCDEFGHIJ")
# graph.add_edges_from([
# 	('A', 'B'),
# 	('A', 'F'),
# 	('B', 'G'),
# 	('F', 'G'),
# 	('G', 'C'),
# 	('G', 'H'),
# 	('G', 'I'),
# 	('C', 'H'),
# 	('I', 'H'),
# 	('H', 'D'),
# 	('H', 'E'),
# 	('H', 'J'),
# 	('E', 'D'),
# ])

graph.add_nodes_from("ABCD")
graph.add_edges_from([
	('A', 'B'),
	('B', 'C'),
	('B', 'D'),

])

plt.subplot(121)
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()

bfs(graph, 'A')
