from min_expectation import min_expectation_algo
from ola import set_random_permutation

from ola_distance import measure_ola_distance

from igraph import Graph


# Define your vertices
vertices = ["A", "B", "C"]

edges = [("A", "B"), ("B", "C"), ("A", "C")]

# Use directed=True for a directed graph
g = Graph(directed=False)

# Add vertices to the graph
g.add_vertices(vertices)

# Add edges to the graph
g.add_edges(edges)

# set_random_permutation(g)
min_expectation_algo(g)
print(measure_ola_distance(g))