import matplotlib.pyplot as plt

def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(start, [start])]
    visited = {start}

    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None

def display_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]
    for x, y in path:
        if (x, y) != path[0] and (x, y) != path[-1]:
            maze_copy[x][y] = '*'
    for row in maze_copy:
        print(' '.join(str(cell) for cell in row))

def plot_maze(maze, path):
    plt.imshow(maze, cmap="binary")  # 0 = white, 1 = black
    if path:
        px, py = zip(*path)
        plt.plot(py, px, color="red", linewidth=2)
    plt.axis("off")
    plt.show()

# Example Maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

shortest_path = bfs_maze_solver(maze, start, end)
print("Shortest Path:", shortest_path)

if shortest_path:
    print("\nMaze with path marked ('*'):")
    display_maze_with_path(maze, shortest_path)
    plot_maze(maze, shortest_path)
else:
    print("No path found.")
