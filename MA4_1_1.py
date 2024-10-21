
"""
Solutions to module 4
Review date:
"""

student = "Emelie Flisberg"
reviewer = ""


import random as r
import matplotlib.pyplot as plt
import math 

def approximate_pi(n):
    # Initialize counters
    inside_circle = 0
    points_inside = []
    points_outside = []
    
    # Generate n random points
    for _ in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        
        # Check if the point lies inside the circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            points_inside.append((x, y))  # Store point inside circle
        else:
            points_outside.append((x, y))  # Store point outside circle
    # Approximate π
    pi_approx = 4 * inside_circle / n
    
    # Print results
    print(f"Number of points in total: {n}")
    print(f"Number of points inside the circle: {inside_circle}")
    print(f"Approximation of π: {pi_approx}")
    print(f"Builtin value of π: {math.pi}")

    # Plot the points
    plt.figure(figsize=(6,6))
    plt.scatter(*zip(*points_inside), color='red', s=1, label='Inside Circle')
    plt.scatter(*zip(*points_outside), color='blue', s=1, label='Outside Circle')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Approximation of π with n = {n}\nπ ≈ {pi_approx}")
    plt.legend(loc="upper right")
    plt.savefig(f'monte_carlo_pi_n_{n}.png')  # Save figure as PNG file
    plt.show()

    return pi_approx  # <-- Return the calculated approximation of π

    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
