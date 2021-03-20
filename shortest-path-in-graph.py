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
        distance_from_start = {n: float('inf') for n in graph}
        distance_from_start[start_node] = 0

        # visited nodes
        visited = set()

        # parent, used to track the path
        parent = {n: None for n in graph}

        # search all nodes
        while len(visited) < len(graph):

            # pick the node with min distance from current start
            min_dist = float('inf')
            cur = None
            for n, dist in distance_from_start.items():
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
                if distance_from_start[cur] + weight < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = distance_from_start[cur] + weight
                    parent[neighbor] = cur

        # build path
        path_end_to_start = [end_node]
        cur = end_node
        while cur:
            cur = parent[cur]
            path_end_to_start.append(cur)

        return ('->'.join(str(n) for n in path_end_to_start[::-1]), distance_from_start[end_node])


# test cases
s = Solution()
graph = {
    0: {
        1: 4,
        7: 8
    },
    1: {
        0: 4,
        2: 8,
        7: 11
    },
    7: {
        0: 8,
        1: 11,
        8: 7,
        6: 1
    },
    2: {
        1: 8,
        8: 2
    },
    8: {
        2: 2,
        7: 7,
        6: 6
    },
    6: {
        7: 1,
        8: 6
    },
}
a = s.shortest_path_dijkstra(graph, 0, 8)
print(f'The shorest path is {a[0]} and the distance is {a[1]}')
