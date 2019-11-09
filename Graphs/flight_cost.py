#!/usr/bin/env python3

"""

There are n cities connected by m flights. Each fight starts from city src and arrives at dest with a price p. Now given all the cities and fights as input, find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Input:
flights = [[0,1,100],[1,2,100],[0,2,500]] / [src city, dest city, price]

Example 1:
src = 0, dst = 2, k = 1
Output: 200

Example 2:
src = 0, dst = 2, k = 0
Output: 500

Example 3:
src = 1, dst = 0, k = 1
output: -1

"""
# Mock 9, how to use priority queues and graphs for these?

from collections import deque

def build_graph(inp_arr):

    adj = dict()

    for i in inp_arr:
        if i[0] not in adj.keys():
            adj[i[0]] = [(i[1], i[2])]
        else:
            adj[i[0]].append((i[1], i[2]))

    return adj

def bfs(adj, src, dst, k):

    cost_arr = []
    visited = []
    dist = dict()
    cost = dict()

    q = deque([(src, 0)])

    dist[(src, 0)] = 0
    cost[(src, 0)] = 0

    while q:
        curr = q.pop()

        if curr[0] not in adj.keys():
            return [-1]

        visited.append(curr)

        if curr[0] == dst:
            cost_arr.append(cost[curr])
            continue

        if dist[curr] > k:
            continue

        nbors = adj[curr[0]]

        for nbor in nbors: # (dst, cost)
            if nbor not in visited:
                q.append(nbor)
                visited.append(nbor)
                cost[nbor] = cost[curr] + nbor[1]
                dist[nbor] = dist[curr] + 1


    if cost_arr is None:
        return [-1]
    else:
        return cost_arr


def find_min_cost(inp_arr, src, dst, k):
    adj = build_graph(inp_arr)
    cost_arr = bfs(adj, src, dst, k)
    return min(cost_arr)

def main():
    inp_arr = [[0,1,100],[1,2,100],[0,2,500]]
    src = 2
    dst = 1
    k = 1
    print(find_min_cost(inp_arr, src, dst, k))

if __name__ == '__main__':
    main()
