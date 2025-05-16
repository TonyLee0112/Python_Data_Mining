import random
import matplotlib.pyplot as plt
import numpy as np

def get_maze(w, h, seed=None) :
    if seed != None :
        random.seed(seed)
    
    H = 2 * h + 1
    W = 2 * w + 1

    # initial maze
    maze = np.ones((H,W),dtype=int) # 세로 H, 가로 W

    # 공간들만을 가진 matrix
    visited = [[False for _ in range(w)] for _  in range(h)]

    def carve(x,y) :
        visited[y][x] = True
        
        mazX, mazY = 2*x+1, 2*y+1
        # 입력된 좌표의 공간 open
        # ndarray 의 indexing 방식
        maze[mazY,mazX] = 0 
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        random.shuffle(dirs)
        for dy, dx in dirs :
            nextX = x + dx
            nextY = y + dy
            if 0 <= nextX < w and 0 <= nextY < h :
                # 경계 밖으로 벗어나지 않고
                if visited[nextY][nextX] == False :
                    # 방문한 적이 없으면 조건 충족
                    # 공간 사이 벽을 허물자
                    maze[mazY+dy,mazX+dx] = 0

                    # 그리고 다음 방향으로 진출
                    # 즉 다음 위치의 공간을 뚫을 거고
                    # 그 공간을 기준으로 다음 벽을 어디를 뚫을지 결정하겠지
                    carve(nextX,nextY)
    carve(0,0) # 시작지점
    maze[1,0] = 0
    maze[H-2,W-1] = 0
    return maze

def show_maze(maze) :
    plt.figure(figsize=(6,6))
    plt.imshow(maze, cmap='binary')
    plt.title('Maze')
    plt.show()

size = int(input("Maze size : "))
maze = get_maze(size,size)
show_maze(maze)
