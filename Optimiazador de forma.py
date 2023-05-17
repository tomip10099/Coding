import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

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

    for x in range(int(radius), int(width - radius) + 1):
        for y in range(int(radius), int(height - radius) + 1):
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
    remaining_diameters = sorted(circle_diameters, reverse=True)

    while remaining_diameters:
        circle_diameter = remaining_diameters.pop(0)
        circle_radius = circle_diameter / 2

        if not circles:
            x = circle_radius
            y = circle_radius
        else:
            x, y = find_best_position(circles, circle_radius, rectangle_width, rectangle_height)

        if x is not None and y is not None:
            circles.append(Circle(x, y, circle_radius))

    return circles

def min_distance_to_circles(x, y, radius, circles):
    for circle in circles:
        dx = circle.x - x
        dy = circle.y - y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < circle.radius + radius:
            return -1

    return distance - radius

def plot_circles(rectangle_width, rectangle_height, circles):
    fig, ax = plt.subplots()
    ax.set_xlim([0, rectangle_width])
    ax.set_ylim([0, rectangle_height])

    for circle in circles:
        circle_patch = Ellipse((circle.x, circle.y), circle.radius*2, circle.radius*2, edgecolor='black', facecolor='none')
        ax.add_patch(circle_patch)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def relacion_utilizacion(rectangle_width, rectangle_height, circle_diameters):
    rectangle_area = rectangle_height * rectangle_width
    circles_areas = 0

    for i in circle_diameters:
        area = (((i)**2) * 3.14)/4
        circles_areas = area + circles_areas 

    ru = (circles_areas/rectangle_area)*100

    return round(ru, 3)

# Example usage
rectangle_width = 1500
rectangle_height = 3000
circle_diameters = [355, 355, 435, 435, 505, 505, 355, 355, 355, 435, 435, 435, 505, 505, 505]

circles = pack_circles(rectangle_width, rectangle_height, circle_diameters)

plot_circles(rectangle_width, rectangle_height, circles)

ru = relacion_utilizacion(rectangle_width, rectangle_height, circle_diameters)
print("Relacion de utilizacion: ", ru, "%")