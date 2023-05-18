import math
import matplotlib.pyplot as plt
import random
from matplotlib.patches import Ellipse, Rectangle

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

def count_contact_points(x, y, radius, circles):
    contact_points = 0

    for circle in circles:
        dx = circle.x - x
        dy = circle.y - y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < circle.radius + radius:
            contact_points += 1

    return contact_points

def find_best_position(circles, radius, width, height):
    best_x = None
    best_y = None
    max_contact_points = -1
    min_distance = float('inf')

    for y in range(int(radius), int(height - radius) + 1):
        for x in range(int(radius), int(width - radius) + 1):
            contact_points = count_contact_points(x, y, radius, circles)
            distance = min_distance_to_circles(x, y, radius, circles)

            if contact_points > max_contact_points and distance >= 0 and distance < min_distance:
                max_contact_points = contact_points
                min_distance = distance
                best_x = x
                best_y = y

    return best_x, best_y

def pack_circles(rectangle_width, rectangle_height, circle_diameters):
    circles = []
    remaining_diameters = circle_diameters.copy()

    seed_value = random.getstate()
    random.shuffle(remaining_diameters)

    iter = 0

    while remaining_diameters:
        circle_diameter = remaining_diameters.pop(0)
        circle_radius = circle_diameter / 2
        iter +=1

        if not circles:
            x = circle_radius
            y = circle_radius
        else:
            x, y = find_best_position(circles, circle_radius, rectangle_width, rectangle_height)

        if x is not None and y is not None:
            circles.append(Circle(x, y, circle_radius))

        print("Iteracion: ", iter)

    return circles, seed_value

def min_distance_to_circles(x, y, radius, circles):
    for circle in circles:
        dx = circle.x - x
        dy = circle.y - y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < circle.radius + radius:
            return -1

    return distance - radius

def plot_circles(rectangle_width, rectangle_height, circles, top_circle_limit):
    fig, ax = plt.subplots()
    ax.set_xlim([0, rectangle_width])
    ax.set_ylim([0, rectangle_height])

        # Dibujar el rectángulo
    rectangle_patch = Rectangle((0, 0), rectangle_width, rectangle_height, edgecolor='red', facecolor='none')
    ax.add_patch(rectangle_patch)

        # Dibujar la línea horizontal
    plt.axhline(y=top_circle_limit, color='green')

    for circle in circles:
        circle_patch = Ellipse((circle.x, circle.y), circle.radius*2, circle.radius*2, edgecolor='black', facecolor='none')
        ax.add_patch(circle_patch)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def calculate_packing_efficiency(rectangle_height, rectangle_width, diameters, top_circle_limit):

    height = rectangle_height - top_circle_limit
    width = rectangle_width

    # Calculate radii for each type of circle
    radii = [diameter / 2 for diameter in diameters]

    packing_efficiency = 0.0

    for i in range(len(diameters)):
        # Calculate the number of circles in the horizontal direction
        nH = math.floor(width / diameters[i])

        # Calculate the number of circles in the vertical direction
        nV = math.floor(height / (1.5 * radii[i]))

        # Calculate the total number of circles for each type
        total_circles = nH * nV

        # Calculate the area occupied by the circles for each type
        area_circles = total_circles * math.pi * radii[i] ** 2

        # Update the packing efficiency
        packing_efficiency += area_circles

    # Calculate the total area of the rectangle
    total_area = height * width

    # Calculate the packing efficiency percentage
    packing_efficiency_percentage = (packing_efficiency / total_area) * 100

    return packing_efficiency_percentage

def find_top_circle(circles):

    circle_limit = 0
    top_circle_limit = -1
    i = 0

    while circle_limit > top_circle_limit:

        top_circle_limit = circle_limit
        i = i - 1

        last_circle = circles[i]
        cord = last_circle.y
        rad = last_circle.radius
        circle_limit = cord + rad
        
    return top_circle_limit


# Example usage
rectangle_width = 1500
rectangle_height = 3000
circle_diameters = [355, 355, 435, 435, 505, 505, 355, 355, 355]

circles, seed_value = pack_circles(rectangle_width, rectangle_height, circle_diameters)

top_circle_limit = find_top_circle(circles)

efficiency = calculate_packing_efficiency(rectangle_height, rectangle_height, circle_diameters, top_circle_limit)
print(f"Packing Efficiency: {efficiency:.2f}%")

plot_circles(rectangle_width, rectangle_height, circles, top_circle_limit)