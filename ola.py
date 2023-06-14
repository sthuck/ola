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


def algorithm_2(g: Graph) -> Graph:
    # order vertices by degree ascending
    # going through each vertex in this order:
    # alternate between low-high values
    # 0,n,1,n-1,2,n-2,3,n-3,...
    sorted_vertices = sorted(g.vs, key=lambda v: v.degree())
    lower_index = 0
    upper_index = len(sorted_vertices) - 1
    use_lower_index = True

    for v in sorted_vertices:
        if use_lower_index:
            set_vertex_permutation(v, lower_index)
            lower_index += 1
        else:
            set_vertex_permutation(v, upper_index)
            upper_index -= 1
        use_lower_index = not use_lower_index
    return g
