import cv2

# 1. 내장 카메라 Video
cap = cv2.VideoCapture(0)

while cap.isOpened() :
    # Read camera frame
    success, frame = cap.read()
    if success :
        # 프레임 출력
        cv2.imshow("Camera Window", frame)

        # ESC : 종료
        key = cv2.waitKey(1) & 0xFF
        if key == 27 :
            break
cap.release()
cv2.destroyAllWindows()

# 실시간으로 카메라를 열어서 화면을 보여줌.
# 27 : ESC 키를 누르면 카메라 꺼짐.


# 2. 영상 주소를 입력해서 영상 재생

import cv2
video_path = r"C:\Users\leesooho\Desktop\Digital_image_processing\Sample Image\test.mp4"

cap = cv2.VideoCapture(video_path)

while cap.isOpened() :
    # Read camera frame
    success, frame = cap.read()
    if success :
        # 프레임 출력
        cv2.imshow("Video Play", frame)

        # ESC : 종료
        key = cv2.waitKey(1) & 0xFF
        if key == 27 :
            break
cap.release()
cv2.destroyAllWindows()



