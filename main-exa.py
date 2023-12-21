import time

from ola import set_random_permutation, measure_ola_distance, algorithm_2
import pandas as pd
from typing import List, Tuple
from min_expectation import min_expectation_algo
from igraph import Graph
import os
import numpy as np
from utils import random_graph


def simple_becnh(fn):
    def wrapper(*args):
        start = time.time()
        rv = fn(*args)
        end = time.time()
        # print('total time:', end - start)
        return rv, end - start
    return wrapper


def read_graph_from_edgelist_file(file_path):
    with open(file_path, 'r') as file:
        # Read the comment line
        comment_line = file.readline().strip()

        # Read the line with symbol '#'
        hash_line = file.readline().strip()
        if not hash_line.startswith('#'):
            raise ValueError("Invalid file format. Second line should start with '#'.")

        # Read id, vertex_number, and edge_number
        id_, vertex_number, edge_number = map(int, hash_line[1:].split())

        # Create an empty directed graph
        graph = Graph(directed=True)

        # Add vertices to the graph
        graph.add_vertices(vertex_number)

        # Read edges and add them to the graph
        for _ in range(edge_number):
            source, destination = map(int, file.readline().split())
            # Convert 1-based indexing to 0-based indexing
            source -= 1
            destination -= 1
            graph.add_edge(source, destination)

        return graph


# Example usage


def main():
    directory_path = 'Exa'
    iterations = 100
    results = {}
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for filename in os.listdir(directory_path):
            if filename.endswith('.edgelist'):
                file_path = os.path.join(directory_path, filename)
                print(f"Processing file: {file_path}")
                g = read_graph_from_edgelist_file(file_path)
                ola_results_for_iterations = []
                time_results_for_iterations = []
                for _ in range(iterations):
                    copyg = g.copy()
                    result_g, time = simple_becnh(min_expectation_algo)(copyg)
                    result = measure_ola_distance(copyg)
                    ola_results_for_iterations.append(result)
                    time_results_for_iterations.append(time)
                ola_result_mean = np.mean(ola_results_for_iterations)
                time_results_mean = np.mean(time_results_for_iterations)
                results[file_path] = [ola_result_mean, time_results_mean]
    pd.DataFrame(results).T.to_csv('./exa_results.csv')


def run_debug():
   # filename = "./Exa/p100_24_34.edgelist"
   # g = read_graph_from_edgelist_file(filename)
    g = random_graph(n=7, p=0.75)
    min_expectation_algo(g, debug=True)
    result = measure_ola_distance(g)
    print(f'final result={result}')


if __name__ == '__main__':
   # main()
    run_debug()