from utils import random_graph
from ola import set_random_permutation, measure_ola_distance, algorithm_2
import pandas as pd
from typing import List, Tuple
from min_expectation import min_expectation_algo

def main_small_graph_iteration():
    times_to_run = 1000
    n = 1000
    p = 0.5
    iterations = 1

    df_csv = pd.DataFrame(columns=["edges", "min-expectation-mean", "min-expectation-min", "min-expectation-var", "naive-alg-mean", "naive-alg-min", "naive-alg-var"])
    for j in range(times_to_run):
        g = random_graph(n=n, p=p)
        edges = len(g.es)
        print(f"n={n}, p={p}, edges={edges}, iterations={iterations}")
        #min_ola_distance_res = []
        results: List[Tuple[int]] = []  # array of tuples, first is navie second is algo2
        for i in range(iterations):
            # Calculate min_expectation and save it in min_ola_distance_res
            min_expectation_graph = min_expectation_algo(g.copy(), False)
            min_expectation_ola_distance = measure_ola_distance(min_expectation_graph)
            #min_ola_distance_res.append(min_expectation_ola_distance)
            # Calculate naive algorithm and save it in min_ola_distance_res
            set_random_permutation(g)
            naive_ola_distance = measure_ola_distance(g)
            results.append((len(g.es), min_expectation_ola_distance, naive_ola_distance))
            # print("min_expectation_ola_distance: ", min_expectation_ola_distance)
            # print("------------------------------------")
        #for i in range(iterations):
        #    print(f"index {i}, min_ola_distance_res = {min_ola_distance_res.pop()}")
        df = pd.DataFrame(results, columns=["edges", "min-exp", "naive-alg"])
        print("average of runs is \n", df.mean())
        print("var of runs is \n", df.var())
        #df_csv = pd.DataFrame(results, columns=["mean", "var"])
        df_csv.loc[len(df_csv)] = [
           df.loc[:, 'edges'].mean(),
           df.loc[:, 'min-exp'].mean(),
           df.loc[:, 'min-exp'].min(),
           df.loc[:, 'min-exp'].var(),
           df.loc[:, 'naive-alg'].mean(),
           df.loc[:, 'naive-alg'].min(),
           df.loc[:, 'naive-alg'].var(),
        ]
        #df_csv['mean'] = df.loc[:, 'min-exp'].mean()
        print("var: ", df.loc[:, 'min-exp'].var())
        df = pd.DataFrame(columns=["edges", "min-exp", "naive-alg"])
    df_csv.drop_duplicates(inplace=True)
    df_csv.to_csv('./main_small_graph_iteration_results.csv')
    return df_csv

    #results: List[Tuple[int]] = []  # array of tuples, first is navie second is algo2
    #for i in range(iterations):
    #    set_random_permutation(g)
    #    naive_ola_distance = measure_ola_distance(g)
    #    results.append((len(g.es), min_expectation_ola_distance))

    #df = pd.DataFrame(results, columns=["edges", "min-exp"])
    #print("average of runs is \n", df.mean())
    #print("var of runs is \n",  df.var())
    #return df

if __name__ == '__main__':
   main_small_graph_iteration()
