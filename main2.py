import pandas as pd
import numpy as np
from utils import random_graph
from ola import set_random_permutation, measure_ola_distance, algorithm_2
import pandas as pd
from typing import List, Tuple
from min_expectation import min_expectation_algo
from igraph import Graph

# Define the number of iterations and the array of functions (fns)
iterations = 10
start = 0.5
stop = 10.0
step = 0.5
n = 100
lambda_values = np.arange(start, stop + step, step)

fns = [min_expectation_algo, algorithm_2, set_random_permutation]
# Create a dictionary to store results
results = {}

# Define a range of floating point numbers (x values)
# Create an array using numpy.arange


# Iterate over the functions
for fn in fns:
    function_name = fn.__name__  # Get the function name
    algorithm_results = {}

    # Run the function 'iterations' times and aggregate results
    for lambda_ in lambda_values:
        print(f'running on lambda {lambda_}')
        lambda_iteration_result = []
        for iteration in range(iterations):
            if iteration % 10 == 0:
                print(f'running iteration {iteration}')
            g = random_graph(n, lambda_/n)
            updated_g = fn(g.copy())
            distance = measure_ola_distance(updated_g)
            lambda_iteration_result.append(distance)
        algorithm_results[lambda_] = np.mean(lambda_iteration_result)

    # Calculate the mean of y results
    results[function_name] = algorithm_results

# Create a Pandas DataFrame from the nested dictionary
data_df = pd.DataFrame(results).T

# Print the resulting DataFrame
print(data_df)
data_df.to_csv('./results.csv')
