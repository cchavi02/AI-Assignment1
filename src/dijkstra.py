# Dijkstra's algorithm (Heuristic h(n) = 0 for all nodes)
def dijkstra(grid, start, goal):
 return a_star(grid, start, goal, lambda x, y: 0) # Pa
ss zero heuristic