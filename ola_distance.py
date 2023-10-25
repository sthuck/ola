from igraph import Vertex, Edge, Graph


def set_vertex_permutation(v: Vertex, index: int):
    v["permutation_index"] = index
    return v


def get_vertex_permutation(v: Vertex) -> int:
    return v["permutation_index"]


def compute_distance(e: Edge) -> int:
    source, dest = e.vertex_tuple
    return abs(get_vertex_permutation(source) - get_vertex_permutation(dest))


def measure_ola_distance(g: Graph) -> int:
    e: Edge
    return sum(compute_distance(e) for e in g.es)

