import cv2
import numpy as np
import matplotlib.pyplot as plt

# 25X2 크기의 랜덤 32비트 정수(0 ~ 99) Array
train_data = np.random.randint(0,100,(25,2)).astype(np.float32)

target = np.random.randint(0,2,(25,1)).astype(np.float32)

# 값이 0인 train_data 는 각각 (x,y) 위치에 빨간색으로 칠한다
# ravel() : 다차원 Array 를 flatten
red = train_data[target.ravel() == 0]
plt.scatter(red[:,0],red[:,1], 80, 'r', '^')

# 값이 1인 데이터는 파란색으로
blue = train_data[target.ravel() == 1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

# map 의 랜덤 위치에 점 하나 찍기
point = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(point[:,0],point[:,1])

knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, target)
Return , result, neighbor, distance = knn.findNearest(point, 3)

# 가까운 3개를 찾고, 거리를 고려하여 자신을 정합니다.
print("result : ", result)
print("neighbors : ",neighbor)
print("distance : ", distance)

plt.show()


