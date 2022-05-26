from ast import arg
import cv2
import threading
import time

def counter_start():
    global end
    end = time.time()

    threading.Timer(1, counter_start).start()

cap = cv2.VideoCapture(cv2.CAP_DSHOW)

count = 0
start, end = time.time(), time.time()

counter_start()

while(True):
    ret, frame = cap.read()

    if(ret) :
        cv2.putText(frame, str(count), (10, 65), cv2.FONT_HERSHEY_DUPLEX , 3, (0, 255, 0))
        cv2.putText(frame, str(int(end - start))+"sec", (530, 465), cv2.FONT_HERSHEY_DUPLEX , 1, (0, 255, 0))
        
        cv2.imshow('frame_color', frame)
        
        # 테스트 용도 if문
        if cv2.waitKey(1) == ord('q'):
            # 행동 인식 후에 결과에 따라 실행
            count = count + 1

# 종료 버튼 누르면 밑에 두 함수 실행     
cap.release()
cv2.destroyWindows()