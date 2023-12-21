from igraph import Graph, Edge, Vertex
import random
from ola_distance import set_vertex_permutation, measure_ola_distance


class MinExpectation:
    g: Graph

    # set of selected vertices
    P: set[Vertex]

    # set of unselected vertices
    U: set[Vertex]

    # list of dP(v), where dP(v) is number of neighbors of v in P, for each v in V
    DP_V: list[int]

    # list of dU(v), where dU(v) is number of neighbors of v in U, for each v in V
    DU_V: list[int]

    def __init__(self, g: Graph):
        self.g = g

    def initalize(self):
        g = self.g
        v: Vertex
        self.P = set()
        self.U: set[Vertex] = set(g.vs)
        self.DP_V = [0 for v in g.vs]

        # list of dU(v), where dU(v) is number of neighbors of v in U, for each v in V
        self.DU_V = [v.degree() for v in g.vs]

    # def compute_g_v(self, v: Vertex, i: int) -> float:
    #     # (3s_vi(n-j)-u_vi(n-j1 + 1) - 3E_SU + 2E_U) / 6
    #     i = v.index
    #     n = self.g.vcount()
    #     return (3 * self.DP_V[i] * (n - i) - self.DU_V[i] * (n - i + 1) - 3 * self.E_SU + 2 * self.E_U) / 6

    def select_vertex(self, iteration: int, debug=False):
        # u = argmax g_v(v) for v in U
        n = self.g.vcount()
        compute_gv = lambda v: 3 * (n - iteration + 1) * self.DP_V[v.index] - (n - iteration + 3) * self.DU_V[v.index]
        if debug:
            GV = sorted([(v.index, compute_gv(v)) for v in self.U], key=lambda x: x[1], reverse=True)
            print('GV:', GV)
        u: Vertex = max(self.U, key=compute_gv)
        rand_max = random.choice([i for i in self.U if compute_gv(i) == compute_gv(u)])
        return rand_max

    def update(self, w: Vertex):
        i = w.index

        self.P.add(w)
        self.U.remove(w)

        v: Vertex
        for v in self.U.intersection(set(w.neighbors())):
            self.DP_V[v.index] += 1
            self.DU_V[v.index] -= 1


def min_expectation_algo(g: Graph, debug=False) -> Graph:
    min_exp_instance = MinExpectation(g)
    min_exp_instance.initalize()

    for i in range(g.vcount()):
        if debug:
            print(f'iteration {i}\n')
        w_i = min_exp_instance.select_vertex(i, debug)
        if debug:
            print(f'selected vertex index {w_i.index}')
        set_vertex_permutation(w_i, i)
        min_exp_instance.update(w_i)

    return g
