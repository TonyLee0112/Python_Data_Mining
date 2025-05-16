import random
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

class MazeEnv :
    __size = 0
    __seed = 42
    __h, __w = 0, 0

    def __init__(self,size, seed=None) :
        self.__size = size
        self.__seed = seed
        self.maze = self.get_maze(size, size, seed)
        self.__h, self.__w = self.maze.shape
        self.start = (1,0)
        self.goal = (self.__h - 2, self.__w - 1)
        self.reset()

    def get_maze(self, w, h, seed=None):
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
    def show_maze(self) :
        plt.figure(figsize=(6,6))
        plt.imshow(self.maze, cmap='binary')
        plt.title('Maze')
        plt.axis('off')
        plt.show()
    def reset(self) :
        self.pos = self.start
        return self.state()
    def state(self) :
        # pos : position -> (x,y)
        return self.pos[0] * self.__w + self.pos[1]
    def step(self, action) :
        # 0 번 : Up, 1 번 : Down
        # 2 번 : Left, 3 번 : Right

        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        dy, dx = moves[action]
        y, x = self.pos
        ny, nx = y + dy, x + dx

        if 0 <= ny < self.__h and 0 <= nx < self.__w :
            if self.maze[ny,nx] == 0 : # 이동 가능한 위치면
                self.pos = (ny,nx)

        
        # Reward
        if self.pos == self.goal :
            return self.state(), 1.0, True
        
        else :
            return self.state(), -0.01, False
    
    def render(self) :
        # Agent 와 Goal 을 표시해서 미로 시각화
        display = self.maze.copy()
        y, x = self.pos
        gy, gx = self.goal
        display[y,x] = 2 # Agent 위치
        display[gy, gx] = 3 # Goal 위치

        plt.figure(figsize=(6,6))
        plt.imshow(display, cmap='viridis')
        plt.title('Maze with Agent')
        plt.axis('off')
        plt.show()

def Q_learning(env, episodes=600, 
               alpha = 0.1, gamma = 0.99, 
               eps_start = 0.3, eps_decay=0.995,eps_min=0.01) :
    # return : 학습된 Q 테이블, episode 별 나아간 스텝 수 기록

    # Q table (State,Action -> value, for 4 directions)
    Q = defaultdict(lambda: np.zeros(4))
    episode_steps = []

    epsilon = eps_start

    for ep in range(episodes) :
        state = env.reset()
        done = False
        steps = 0

        while not done :
            # epsilon-greedy 행동 선택
            if random.random() < epsilon :
                # 처음에는 Q 값이 모두 0이니 랜덤하게 이동방향 선택
                action = random.randint(0,3)
            else :
                action =  int(np.argmax(Q[state]))

            next_state, reward, done = env.step(action)

            # Q-learning update
            best_next = np.max(Q[next_state])
            Q[state][action] += alpha * (reward + gamma * best_next
                                         - Q[state][action])
            state = next_state
            steps += 1

            # 안전장치 : 너무 길면 중단단
            if steps > 1000 :
                break
        episode_steps.append(steps)
        epsilon = max(eps_min, epsilon * eps_decay)

    return Q, episode_steps

env = MazeEnv(size=int(input("미로의 크기를 입력해주세요: ")), seed=42)

# 학습
Q, history = Q_learning(env)

# 학습 추이 확인
plt.plot(history)
plt.xlabel("Episode")
plt.ylabel("Steps to Goal")
plt.title("Learning Curve")
plt.show()

# 학습된 Policy 를 이용하여 한 번 실행하고, 시각화
state = env.reset()
done = False
while not done :
    action = int(np.argmax(Q[state]))
    state, _, done = env.step(action)
env.render()
