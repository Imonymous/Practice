'''
Complete the 'nearest_neighbours' function below.

The function accepts integer p_x, p_y, k and a 2D integer array n_points as parameter.
'''

import math
def calc_dist(x, y, point):
    return math.sqrt((x-point.x)**2 + (y-point.y)**2) 
 
import heapq
def nearest_neighbours(p_x, p_y, k, n_points):
    # Write your code here
    heap = []
    count = dict()
    priority_map = dict()

    for point in n_points:
        dist = calc_dist(p_x, p_y, point)
        if dist in count.keys():
            count[dist] += 1
        else:
            count[dist] = 1

        priority = count[dist]

        if len(heap) <= k:
            heapq.heappush(heap, (priority, point))
        else:
            

    for i in range(k):
        print heapq.heappop(heap)