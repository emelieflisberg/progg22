
"""
Solutions to module 4
Review date:
"""

student = "Emelie Flisberg"
reviewer = ""

import math as m
import random as r
from time import perf_counter as pc
from concurrent.futures import ProcessPoolExecutor




def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    inside_count = 0
    
    for _ in range(n):
        point = [r.uniform(-1, 1) for _ in range(d)]
        if sum(x ** 2 for x in point) <= 1:
            inside_count += 1
    
    volume_approx = (2 ** d) * (inside_count / n)
    
    return volume_approx

def hypersphere_exact(d):

    """Compute the exact volume of a d-dimensional hypersphere with radius 1."""
    return (m.pi ** (d / 2)) / m.gamma((d / 2) + 1)



# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    with ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, n, d) for _ in range(10)]
        volumes = [f.result() for f in futures]
    
    # Average the results from all parallel computations
    return sum(volumes) / len(volumes)


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    """Parallelize the computation by splitting the data among processes."""
    chunk_size = n // np
    with ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, chunk_size, d) for _ in range(np)]
        volumes = [f.result() for f in futures]
    
    # Average the results from all parallel computations
    return sum(volumes) / len(volumes)


def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10  # Number of processes

    # Sequential execution
    start = pc()

    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    seq_time = stop - start
    print(f"Sequential time: {seq_time:.4f} seconds")

    # Parallel execution: Task 1 (parallelizing the loop)
    start = pc()
    parallel_volume1 = sphere_volume_parallel1(n, d, np)
    stop = pc()
    parallel_time1 = stop - start
    print(f"Parallel (loop) volume: {parallel_volume1:.4f}, Time: {parallel_time1:.4f} seconds")

    # Parallel execution: Task 2 (parallelizing the data)
    start = pc()
    parallel_volume2 = sphere_volume_parallel2(n, d, np)
    stop = pc()
    parallel_time2 = stop - start
    print(f"Parallel (data) volume: {parallel_volume2:.4f}, Time: {parallel_time2:.4f} seconds")

    # Exact volume for comparison
    exact_volume = hypersphere_exact(d)
    print(f"Exact volume: {exact_volume:.4f}")




if __name__ == '__main__':
	main()
