from ola import set_random_permutation
from ola_distance import measure_ola_distance

from igraph import Graph

# Define your vertices
vertices = ["A", "B", "C", "D", "E", "F"]

# Define your edges as a list of tuples (source, target)
edges = [("B", "C"), ("B", "D"), ("B", "E"), ("C", "D")]

# Create a graph
g = Graph(directed=False)  # Use directed=True for a directed graph

# Add vertices to the graph
g.add_vertices(vertices)

# Add edges to the graph
g.add_edges(edges)

set_random_permutation(g)
print(measure_ola_distance(g))