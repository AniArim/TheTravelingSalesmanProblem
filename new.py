import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming


def calculate_vector(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    way_count = ((x2-x1)**2 + (y2-y1)**2)**0.5
    list_of_count.append(list_of_count[-1] + way_count)


coords_list = [(0, 2), (5, 2), (6, 6), (2, 5), (8, 3)]
x, y, list_of_count, final_list_of_points = [], [], [0], []

for item in coords_list:
    x.append(item[0]), y.append(item[1])

point_x, point_y = np.array(x), np.array(y)

d_point_x, d_point_y = point_x[..., np.newaxis] - point_x[np.newaxis, ...],\
                       point_y[..., np.newaxis] - point_y[np.newaxis, ...]

distance = np.array([d_point_x, d_point_y])
#  var = distance.shape
distance_matrix = (distance ** 2).sum(axis=0) ** 0.5
permutation, all_dist = solve_tsp_dynamic_programming(distance_matrix)

for i in permutation:
    final_list_of_points.append(coords_list[i])
final_list_of_points.append(coords_list[0])


for element in range(len(final_list_of_points)):
    try:
        calculate_vector(final_list_of_points[element], final_list_of_points[element+1])
    except IndexError:
        pass
list_of_count.remove(0)
print(final_list_of_points[0], "-> ", end="")

k = 1
for j in list_of_count:
    if j == all_dist:
        print(final_list_of_points[0], [all_dist], "= ", all_dist)
    else:
        print(final_list_of_points[k], [j], "-> ", end="")
        k += 1

