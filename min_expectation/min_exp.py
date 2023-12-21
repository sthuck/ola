from random import random
import networkx as nx
from networkx import nodes, edges


class MinExpectation2:
    g: nx.Graph()

    # set of selected vertices
    P: set()

    # set of unselected vertices
    U: set()

    # list of dP(v), where dP(v) is number of neighbors of v in P, for each v in V
    DP_V: list[int]

    # list of dU(v), where dU(v) is number of neighbors of v in U, for each v in V
    DU_V: list[int]

    def __init__(self, dimension):
        self.dimension = dimension
        self.graph = nx.hypercube_graph(dimension)

    def initalize(self, *args):
        g = self.graph
        v: nodes
        self.P = set()
        self.U = set(g.nodes)
        self.DP_V = [0 for v in g.nodes]
        self.DU_V = args[0]

    def select_vertex(self, iteration: int, debug=False):

        self.U = set()
        node_indices = list(self.graph.nodes())
        for index, node in enumerate(node_indices):
            self.U.add(index)
        n = self.graph.number_of_nodes()
        print(isinstance(self.DU_V, int))
        compute_gv = lambda v: 3 * (n - iteration + 1) * self.DP_V[v] - (n - iteration + 3) * (self.DU_V)
        if debug:
            GV = sorted([(v.index, compute_gv(v)) for v in self.U], key=lambda x: x[1], reverse=True)
            print('GV:', GV)
        u: nodes = max(self.U, key=compute_gv)
        #rand_max = random.choice([i for i in self.U if compute_gv(i) == compute_gv(u)])
        return u


    def update(self, w: nodes):
        i = w.index

        self.P.add(w)
        self.U.remove(w)

        v: nodes
        for v in self.U.intersection(set(w.neighbors())):
            self.DP_V[v.index] += 1
            self.DU_V[v.index] -= 1


def min_expectation_algo2(g: nx.Graph, dim: int, debug=False) -> nx.Graph:
    min_exp_instance = MinExpectation2(dim)
    min_exp_instance.initalize(dim)

    for i in range(g.number_of_nodes()):
        if debug:
            print(f'iteration {i}\n')
        w_i = min_exp_instance.select_vertex(i, debug)
        if debug:
            print(f'selected vertex index {w_i.index}')
        set_vertex_permutation(w_i, i)
        min_exp_instance.update(w_i)

    return g


def set_vertex_permutation(v:nodes, index: int):
    v["permutation_index"] = index
    return v

def get_vertex_permutation(v: nodes) -> int:
    return v["permutation_index"]


def compute_distance(e: edges) -> int:
    source, dest = e.vertex_tuple
    return abs(get_vertex_permutation(source) - get_vertex_permutation(dest))


def measure_ola_distance(g: nx.Graph) -> int:
    e: edges
    return sum(compute_distance(e) for e in g.edges)

