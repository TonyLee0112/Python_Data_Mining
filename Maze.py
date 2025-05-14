import random
import matplotlib.pyplot as plt
import numpy as np

def get_maze(w, h, seed=None):
    if seed is not None:
        random.seed(seed)
    H = 2 * h + 1
    W = 2 * w + 1
    maze = np.ones((H, W),dtype=int)
    visited = [[False] * w for _ in range(h)]
    
    # DFS Backtracking
    def carve(x,y):
        # Cell 종류 = 벽 or 공간
        visited[y][x] = True
        maze[2*y+1, 2*x+1] = 0  # 해당 공간 open
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        random.shuffle(dirs)
        for dy, dx in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                maze[2*y+1 + dy, 2*x+1 + dx] = 0 # 공간 사이 벽 허물기
                carve(nx, ny)

    carve(0, 0)
    maze[1, 0] = 0             # 입구
    maze[H-2, W-1] = 0         # 출구
    return maze

# 미로 생성 및 시각화
def show_maze(maze) :
    plt.figure(figsize=(6,6))
    plt.imshow(maze, cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.title('Generated Maze')
    plt.show()

maze = get_maze(10, 10)
show_maze(maze)

