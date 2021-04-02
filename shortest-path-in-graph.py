from heapq import heappop, heappush


class Solution:

    # Dijkstra's Algorithm
    #
    # shortest path from one node to all other nodes in a weighted graph
    #
    # example input graph:
    # {1 -> (3, 5), (4, 3))
    #  2 -> (1, 3)
    #  3 -> (4, 2)
    #  4 -> (2, 1), (3, 1)
    #  5 -> (2, 4), (4, 2)
    # }
    # outinput:
    # tuple of short_path and min_distance
    def shortest_path_dijkstra(self, graph, start_node, end_node):
        # initially, default to inf
        distance = {n: float('inf') for n in graph}
        distance[start_node] = 0

        # visited nodes
        visited = set()

        # parent, used to track the path
        parent = {n: None for n in graph}

        # search all nodes
        while len(visited) < len(graph):

            # pick the node with min distance from current start
            min_dist = float('inf')
            cur = None
            for n, dist in distance.items():
                if n in visited:
                    continue

                if dist < min_dist:
                    cur = n
                    min_dist = dist

            visited.add(cur)

            # update cost_to_get_to for neighboring nodes
            for neighbor, weight in graph[cur].items():

                if neighbor in visited:
                    continue

                # update distance and parent
                if distance[cur] + weight < distance[neighbor]:
                    distance[neighbor] = distance[cur] + weight
                    parent[neighbor] = cur

        # build path
        path_reversed = [end_node]
        cur = end_node
        while cur:
            cur = parent[cur]
            path_reversed.append(cur)

        return ('->'.join(str(n) for n in path_reversed[::-1]), distance[end_node])

    # # Dijkstra's Algorithm
    #
    # shortest path from one node to all other nodes in a weighted graph
    # use a priority queue to track the shortest distance of vertice
    def shortest_path_dijkstra_priority_queue(self, graph, start_node, end_node):
        # distance from start
        distance = {n: float('inf') for n in graph}
        distance[start_node] = 0
        # distance as a priority queue
        pq = []
        for n, dis in distance.items():
            heappush(pq, (dis, n))

        # number of nodes
        nodes_num = len(graph)

        # visited nodes
        visited = set()

        # parent, used to track the path
        parent = {n: None for n in graph}

        # search all nodes
        while len(visited) < nodes_num:

            # pick the node with min distance from current start
            cur_dis, cur = heappop(pq)
            visited.add(cur)

            # update cost_to_get_to for neighboring nodes
            for neighbor, weight in graph[cur].items():

                if neighbor in visited:
                    continue

                # update distance, parent and pq
                if cur_dis + weight < distance[neighbor]:
                    distance[neighbor] = cur_dis + weight
                    parent[neighbor] = cur
                    # lazy deletion, enqueue the uodated distance
                    heappush(pq, (cur_dis + weight, neighbor))

        # build path
        path_reversed = [end_node]
        cur = end_node
        while cur:
            cur = parent[cur]
            path_reversed.append(cur)

        return ('->'.join(str(n) for n in path_reversed[::-1]), distance[end_node])


# test cases
s = Solution()
graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    7: {0: 8, 1: 11, 8: 7, 6: 1},
    2: {1: 8, 8: 2},
    8: {2: 2, 7: 7, 6: 6},
    6: {7: 1, 8: 6},
}
start = 0
end = 8
a = s.shortest_path_dijkstra(graph, start, end)
print(f'The shorest path is {a[0]} and the distance is {a[1]}')

a = s.shortest_path_dijkstra(graph, start, end)
print(f'The shorest path is {a[0]} and the distance is {a[1]}')
