
"""
Solutions to module 4
Review date:
"""

student = "Emelie Flisberg"
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 


 # Generate n random points in d dimensions and check how many are inside the hypersphere
    def random_point():
        return [r.uniform(-1, 1) for _ in range(d)]  # Generate a random point in d dimensions

    # Use map to compute the sum of squares for each point
    def is_inside_sphere(point):
        return sum(map(lambda x: x**2, point)) <= 1  # Check if the point is inside the hypersphere

    points = [random_point() for _ in range(n)]

    # Filter the points that are inside the hypersphere
    inside_sphere = list(filter(is_inside_sphere, points))

    # The ratio of points inside to total points approximates the volume
    volume_approx = (len(inside_sphere) / n) * (2**d)
    
    return volume_approx



def hypersphere_exact(n, d):
    return (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)
     
def main():
    n = 100000
    dimensions = [2, 11]  # Dimensions for testing
    for d in dimensions:
        approx_volume = sphere_volume(n, d)
        exact_volume = hypersphere_exact(n, d)
        
        print(f"Approximate volume of a {d}-dimensional hypersphere (n = {n}): {approx_volume}")
        print(f"Exact volume of a {d}-dimensional hypersphere: {exact_volume}")

  

if __name__ == '__main__':
	main()
