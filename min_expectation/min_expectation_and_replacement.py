from igraph import Graph, Edge, Vertex
import random
from ola_distance import set_vertex_permutation, measure_ola_distance, get_vertex_permutation
from .min_expectation import min_expectation_algo


# given a graph and two vertices, compute the ola_distance if they were to be swapped, return the new distance
def try_replace_vertex(g: Graph, v1: Vertex, v2: Vertex, current_distance: int) -> int:
    v1_permutation = get_vertex_permutation(v1)
    v2_permutation = get_vertex_permutation(v2)

    v1_n = v1.neighbors()
    v1_n_distance = [abs(v1_permutation - get_vertex_permutation(n)) for n in v1_n if n != v2]
    # compute the new distance if v1 were to be replaced with v2
    v1_n_new_distance = [abs(v2_permutation - get_vertex_permutation(n)) for n in v1_n if n != v2]

    v2_n = v2.neighbors()
    v2_n_distance = [abs(v2_permutation - get_vertex_permutation(n)) for n in v2_n if n != v1]
    # compute the new distance if v2 were to be replaced with v1
    v2_n_new_distance = [abs(v1_permutation - get_vertex_permutation(n)) for n in v2_n if n != v1]

    v1_n_distance_diff = sum(v1_n_new_distance) - sum(v1_n_distance)
    v2_n_distance_diff = sum(v2_n_new_distance) - sum(v2_n_distance)

    new_distance = current_distance + v1_n_distance_diff + v2_n_distance_diff
    return new_distance


def do_replace_vertex(g: Graph, vertex_list: list[Vertex], v1: Vertex, v2: Vertex) -> Graph:
    v1_permutation = get_vertex_permutation(v1)
    v2_permutation = get_vertex_permutation(v2)
    vertex_list[v1_permutation] = v2
    vertex_list[v2_permutation] = v1
    set_vertex_permutation(v1, v2_permutation)
    set_vertex_permutation(v2, v1_permutation)


def get_all_vertices_pairs(g: Graph) -> tuple[list[tuple[int, int]], list[Vertex]]:
    vertices = list(g.vs)
    # this controls weather we iterate by the original index, or by the permutation index
    sorted(vertices, key=lambda v: get_vertex_permutation(v))
    pairs = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            pairs.append((i, j))
    return pairs, vertices


def min_expectation_and_replacement_algo(g: Graph, debug=False) -> Graph:
    g = min_expectation_algo(g, False)
    current_distance = measure_ola_distance(g)
    all_pairs, vertex_list = get_all_vertices_pairs(g)

    queue = all_pairs
    done_pairs = []
    while len(queue):
        v1_i, v2_i = queue.pop(0)
        v1, v2 = vertex_list[v1_i], vertex_list[v2_i]
        new_distance = try_replace_vertex(g, v1, v2, current_distance)
        if new_distance < current_distance:
            if debug:
                print(f'new distance {new_distance} is better than current distance {current_distance}, replacing '
                      f'{get_vertex_permutation(v1)} with {get_vertex_permutation(v2)}')
                print('done_pairs:', len(done_pairs))

            do_replace_vertex(g, vertex_list, v1, v2)
            current_distance = new_distance
            queue = queue + done_pairs
            done_pairs = [(v1_i, v2_i)]
        else:
            done_pairs.append((v1_i, v2_i))
    if debug:
        print(f'======= final distance: {current_distance} ====== \n\n\n\n\n')
    return g
