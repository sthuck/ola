from igraph import Graph, Edge, Vertex
import random


def set_vertex_permutation(v: Vertex, index: int):
    v["permutation_index"] = index
    return v


def get_vertex_permutation(v: Vertex) -> int:
    return v["permutation_index"]


def compute_distance(e: Edge) -> int:
    source, dest = e.vertex_tuple
    return abs(get_vertex_permutation(source) - get_vertex_permutation(dest))


def set_random_permutation(g: Graph):
    random_permutation = list(range(g.vcount()))
    random.shuffle(random_permutation)
    for index, v in enumerate(g.vs):
        set_vertex_permutation(v, random_permutation[index])


def measure_ola_distance(g: Graph) -> int:
    e: Edge
    return sum(compute_distance(e) for e in g.es)
