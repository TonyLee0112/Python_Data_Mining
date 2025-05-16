import random
import matplotlib.pyplot as plt
import numpy as np

class MazeEnv:
    def __init__(self, size, seed=None):
        self.size = size
        self.seed = seed
        self.maze = self.get_maze(size, size, seed)
        self.h, self.w = self.maze.shape
        self.start = (1, 0)
        self.goal = (self.h - 2, self.w - 1)
        self.reset()

    @staticmethod
    def get_maze(w, h, seed=None):
        """w×h 공간 크기의 랜덤 미로 생성"""
        if seed is not None:
            random.seed(seed)
        H, W = 2 * h + 1, 2 * w + 1
        maze = np.ones((H, W), dtype=int)
        visited = [[False] * w for _ in range(h)]

        def carve(x, y):
            visited[y][x] = True
            mazX, mazY = 2 * x + 1, 2 * y + 1
            maze[mazY, mazX] = 0
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(dirs)
            for dy, dx in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                    maze[mazY + dy, mazX + dx] = 0
                    carve(nx, ny)

        carve(0, 0)
        # 입구/출구 설정
        maze[1, 0] = 0
        maze[H - 2, W - 1] = 0
        return maze

    def show_maze(self):
        """현재 미로를 화면에 출력"""
        plt.figure(figsize=(6, 6))
        plt.imshow(self.maze, cmap='binary')
        plt.title('Maze')
        plt.axis('off')
        plt.show()

    def reset(self):
        self.pos = self.start
        return self._state()

    def _state(self):
        return self.pos[0] * self.w + self.pos[1]

    def step(self, action):
        # actions: 0=up,1=down,2=left,3=right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dy, dx = moves[action]
        y, x = self.pos
        ny, nx = y + dy, x + dx
        # 이동 가능하면 위치 업데이트
        if 0 <= ny < self.h and 0 <= nx < self.w and self.maze[ny, nx] == 0:
            self.pos = (ny, nx)
        # 보상
        if self.pos == self.goal:
            return self._state(), 1.0, True
        else:
            return self._state(), -0.01, False

    def render(self):
        """에이전트와 목표를 표시하여 미로 시각화"""
        disp = self.maze.copy()
        y, x = self.pos
        gy, gx = self.goal
        disp[y, x] = 2   # 에이전트 위치
        disp[gy, gx] = 3 # 목표 위치
        plt.figure(figsize=(6, 6))
        plt.imshow(disp, cmap='viridis')
        plt.title('Maze with Agent')
        plt.axis('off')
        plt.show()


# 사용 예시
if __name__ == "__main__":
    env = MazeEnv(size=10, seed=42)
    # 원본 미로 보기
    env.show_maze()

    # 간단히 무작위 행동으로 한 스텝 시뮬레이션
    state = env.reset()
    for _ in range(20):
        a = random.randint(0, 3)
        state, reward, done = env.step(a)
        if done:
            break
    env.render()
