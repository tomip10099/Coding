import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Constants
RECTANGLE_WIDTH = 10.0
RECTANGLE_HEIGHT = 8.0
CIRCLE_RADII = [1.0, 2.0, 3.0, 1.5, 3.0]  # Updated list with 5 radii

def calculate_overlap_area(center_points, radii):
    total_overlap = 0.0
    num_circles = len(center_points)
    
    for i in range(num_circles):
        for j in range(i + 1, num_circles):
            distance = np.linalg.norm(center_points[i] - center_points[j])
            radii_sum = radii[i] + radii[j]
            
            if distance < radii_sum:
                overlap = radii_sum - distance
                total_overlap += overlap * overlap
            
    return total_overlap

def objective_function(x):
    num_circles = len(CIRCLE_RADII)
    x_coordinates = x[:num_circles]
    y_coordinates = x[num_circles:]
    center_points = np.column_stack((x_coordinates, y_coordinates))
    
    return calculate_overlap_area(center_points, CIRCLE_RADII)

# Constraints
def circle_constraint(x):
    num_circles = len(CIRCLE_RADII)
    x_coordinates = x[:num_circles]
    y_coordinates = x[num_circles:]
    
    constraints = []
    for i in range(num_circles):
        constraints.append(RECTANGLE_WIDTH - x_coordinates[i] - CIRCLE_RADII[i])
        constraints.append(RECTANGLE_HEIGHT - y_coordinates[i] - CIRCLE_RADII[i])
    
    return constraints

constraints = [{'type': 'ineq', 'fun': circle_constraint}]

# Initial guess
initial_guess = np.random.rand(2 * len(CIRCLE_RADII))

# Solve the optimization problem
solution = minimize(objective_function, initial_guess, constraints=constraints)

# Extract the optimized coordinates
x_coordinates = solution.x[:len(CIRCLE_RADII)]
y_coordinates = solution.x[len(CIRCLE_RADII):]
center_points = np.column_stack((x_coordinates, y_coordinates))

# Visualization
fig, ax = plt.subplots()
ax.set_xlim(0, RECTANGLE_WIDTH)
ax.set_ylim(0, RECTANGLE_HEIGHT)
ax.set_aspect('equal')
ax.set_title('Optimized Circle Arrangement')

# Plot rectangle
rectangle = plt.Rectangle((0, 0), RECTANGLE_WIDTH, RECTANGLE_HEIGHT, ec='red', fc='none')
ax.add_patch(rectangle)

# Plot circles
for center, radius in zip(center_points, CIRCLE_RADII):
    circle = plt.Circle(center, radius, ec='black', fc='none')
    ax.add_patch(circle)

plt.show()
