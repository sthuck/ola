from igraph import Graph
from utils import random_graph
from ola import set_random_permutation, measure_ola_distance, algorithm_2
import pandas as pd
from typing import List, Tuple


def main():
    n = 100
    p = 0.2
    iterations = 100
    print(f"n={n}, p={p}, iterations={iterations}")

    results: List[Tuple[int]] = []  # array of tuples, first is navie second is algo2
    for i in range(iterations):
        g = random_graph(n=n, p=p)
        set_random_permutation(g)
        naive_ola_distance = measure_ola_distance(g)
        algorithm_2(g)
        alog2_ola_distance = measure_ola_distance(g)
        results.append((len(g.es), naive_ola_distance, alog2_ola_distance))

    df = pd.DataFrame(results, columns=["edges", "naive", "algo2"])
    print("avergage of runs is \n", df.mean())
    return df


if __name__ == "__main__":
    main()
