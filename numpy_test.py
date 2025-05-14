import numpy as np

a = np.zeros((2,3))
print(a,end="\n")

a = np.ones((3,2))
print(a,end="\n")

a = np.full((2,3),5)
print(a, end="\n")

a = np.eye(3) # 3X3 Array 를 만들고 대각성분에 1을 채움
print(a, end="\n")

a = np.array(range(20))
print(a, end="\n")
print(a.reshape((4,5)))
