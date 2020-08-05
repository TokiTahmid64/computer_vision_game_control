import cv2
import numpy as np
import pyautogui
cap=cv2.VideoCapture(1)
pyautogui.FAILSAFE=False

lower_g=np.array([100,150,0],np.uint8)
upper_g=np.array([140,255,255],np.uint8)
lower_y = np.array([20, 100, 100])
upper_y = np.array([30, 255, 255])

y_prev=0
center_x1=0
center_y1=0
center_x2=0
center_y2=0
font= cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale= 1
fontColor= (255,255,255)
lineType= 2
while True:
    r,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask1=cv2.inRange(hsv,lower_g,upper_g)
    mask2=cv2.inRange(hsv,lower_y,upper_y)
    image,contours,h=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    image2,contours2,h2=cv2.findContours(mask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


    for c in contours:
        area=cv2.contourArea(c)
        if(area>100):
            x,y,w,h=cv2.boundingRect(c)
            center_x1=int(x+(w/2))
            center_y1=int(y+(h/2))
            cv2.circle(frame,(center_x1,center_y1),10,(0,255,0),5)



           # y_prev=y
    for c in contours2:
        area=cv2.contourArea(c)

        if(area>100):
           x, y, w, h = cv2.boundingRect(c)
           center_x2 = int(x + (w / 2))
           center_y2 = int( y + (h / 2))
           cv2.circle(frame, (center_x2, center_y2), 10, (0, 0, 255), 5)
          # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
           #pyautogui.press('up')



    cv2.line(frame,(center_x1,center_y1),(center_x2,center_y2),(255,0,0),5)

    angle=np.arctan(((center_y2-center_y1)/(np.abs(center_x2-center_x1)+1)))*180/3.1416
    g = float("{:.2f}".format(angle))
    #cv2.addText(frame,angle,nameFont='arial',pointSize=20,color=(0,255,0),org=(10,10))
    position = (10, 50)

    cv2.putText(frame,str(g),position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 4)

    if g>10:
        pyautogui.press('d')
    else:
        pyautogui.press('a')


    cv2.imshow('frame',frame)
    if cv2.waitKey(10)==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
