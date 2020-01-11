"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Hashable, Any, Optional, Tuple
import networkx as nx

_root: Optional[Hashable] = None
_tree = nx.Graph()


def insert(key: Hashable, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	"""
	global _root
	if _root is None:
		_root = key
		_tree.add_node(key, value=value)
	else:
		_value, root_node = _find_in_subTree(key, _root, None)

		if root_node != key:
			_tree.add_edge(root_node, key)
	_tree.add_node(key, value=value)

	return None


def remove(key: Hashable) -> Optional[Tuple[Hashable, Any]]:
	"""
	Remove key and associated value from the BST if exists

	:param key: key to be removed
	:return: deleted (key, value) pair or None
	"""
	_tree.remove_node(key)
	print(f'remove:{key}  tree:{list(_tree.nodes)}')
	# return None

def _find_in_subTree(key: Hashable, root: Hashable, parent) -> Tuple[Any, Hashable]:
	if key == root:
		return _tree.nodes[root]["value"], root

	for node in _tree.neighbors(root):
		if node == parent:
			continue
		if node < root and node < root or \
				node > root and node > root:
			return _find_in_subTree(key, node, root)
	return None, root


def find(key: Hashable) -> Optional[Any]:
	"""
	Find value by given key in the BST

	:param key: key for search in the BST
	:return: value associated with the corresponding key
	"""
	global _root
	if _root is None:
		_root = key

	# 	print(key)
	return None


def clear() -> None:
	"""
	Clear the tree

	:return: None
	"""
	global _root
	_root = None
	_tree.clear()

# return None

#
#
# _tree.add_nodes_from('abcd')
# print(list(_tree.nodes))
#
# remove('b')
# # clear()
#
# print(list(_tree.nodes))

# _root = 6
# _tree.add_nodes_from('134569')
# _tree.add_edges_from([
# 	(3, 5),
# 	(3, 1),
# 	(3, 4),
# 	(9, 5),
# 	(9, 6)
# ])


# print
# _root = 5

insert('5', 5)
insert('3', 3)
insert('9', 9)
insert('1', 1)
insert('4', 4)
insert('6', 6)
insert('7', 7)
insert('7', 9)


print(list(_tree.nodes))