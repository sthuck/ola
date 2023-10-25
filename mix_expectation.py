from igraph import Graph, Edge, Vertex
import random


class MinExpectation:
    g: Graph

    # set of selected vertices
    S: set[Vertex]

    # set of unselected vertices
    U: set[Vertex]

    # number of edges between selected vertices and unselected vertices
    E_SU: int
    # number of edges between unselected vertices
    E_U = int

    # list of s_v, where s_v is number of neighbors of v in S, for each v in V
    S_V: list[int]

    # list of u_v, where u_v is number of neighbors of v in U, for each v in V
    U_V: list[int]

    # list of g(v) values for each v in V
    G_V: list[int]

    def __init__(self, g: Graph):
        self.g = g

    def initalize(self):
        g = self.g
        v: Vertex
        self.S = set()
        self.U: set[Vertex] = set(g.vs)
        self.E_SU = 0
        self.E_U = len(g.es)
        self.S_V = [0 for v in g.vs]

        # list of u_v, where u_v is number of neighbors of v in U, for each v in V
        self.U_V = [v.degree() for v in g.vs]

    def compute_g_v(self, v: Vertex, i: int) -> float:
        # (3s_vi(n-j)-u_vi(n-j1 + 1) - 3E_SU + 2E_U) / 6
        i = v.index
        n = self.g.vcount()
        return (3 * self.S_V[i] * (n - i) - self.U_V[i] * (n - i + 1) - 3 * self.E_SU + 2 * self.E_U) / 6

    def select_vertex(self, iteration: int):
        # u = argmax g_v(v) for v in U
        u: Vertex = max(self.U, key=lambda v: self.compute_g_v(v, iteration))
        return u

    def update(self, w: Vertex):
        i = w.index

        self.S.add(w)
        self.U.remove(w)
        # E_SU = E_SU + (UV[i] - SV[i])
        self.E_SU += (self.U_V[i] - self.S_V[i])
        # E_U = E_U - UV[i]
        self.E_U -= self.U_V[i]

        v: Vertex
        for v in self.U:
            self.S_V[v.index] = len(self.S.intersection(v.neighbors()))
            self.U_V[v.index] = len(self.U.intersection(v.neighbors()))

def min_expectation(g: Graph) -> Graph:
    min_exp_instance = MinExpectation(g)
    min_exp_instance.initalize()

    for i in range(g.vcount()):
        w_i = min_exp_instance.select_vertex(i)
        min_exp_instance.update(w_i)

    return g
