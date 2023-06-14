from igraph import Graph
from utils import random_graph
from ola import set_random_permutation, measure_ola_distance


def main():
    g = random_graph(100, p=0.2)
    set_random_permutation(g)
    print(measure_ola_distance(g))


if __name__ == "__main__":
    main()
