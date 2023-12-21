from utils import random_graph
from ola import set_random_permutation, measure_ola_distance, algorithm_2
import pandas as pd
from typing import List, Tuple
from min_expectation import min_expectation_algo

def main():
    n = 1000
    p = 1/2
    iterations = 1
    print(f"n={n}, p={p}, iterations={iterations}")

    g = random_graph(n=n, p=p)
    g_algo2 = algorithm_2(g.copy())
    alog2_ola_distance = measure_ola_distance(g_algo2)

    min_expectation_graph = min_expectation_algo(g.copy())
    min_expectation_ola_distance = measure_ola_distance(min_expectation_graph)


    results: List[Tuple[int]] = []  # array of tuples, first is navie second is algo2
    for i in range(iterations):
        set_random_permutation(g)
        naive_ola_distance = measure_ola_distance(g)
        results.append((len(g.es), naive_ola_distance, alog2_ola_distance, min_expectation_ola_distance))

    df = pd.DataFrame(results, columns=["edges", "naive", "algo2", "min-exp"])
    print("average of runs is \n", df.mean())
    return df


if __name__ == "__main__":
     main()
