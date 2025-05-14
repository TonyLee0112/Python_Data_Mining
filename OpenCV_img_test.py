# OpenCV : Open Source Computer Vision Library
# For real-time computer vision
# Developed by Intel
# Focused on Real-time Image Processing
# Camera, Edge/Cloud-based computing, AI 등을 결합하여 시스템이 사물을 확인하고 식별할 수 있도록 도와줌

import cv2
import matplotlib.pyplot as plt

# Raw String based image path - 주소 왼쪽에 r 붙이기
# img_path 에 한글 있으면 인코딩 문제로 인식 안됨.
img_path = r"C:\Users\leesooho\Desktop\Digital_image_processing\Sample Image\kaisa.jpg"
img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)

blurred_img = cv2.blur(img, (5,5)) # Kernel size = 5X5

plt.imshow(blurred_img, cmap='gray')
plt.show()
