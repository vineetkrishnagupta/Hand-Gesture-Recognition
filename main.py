import cv2
import mediapipe as mp

from point4MaxValue import *
from point4MinValue import *
from rectangleFunction import *


face_cascade = cv2.CascadeClassifier('face.xml')

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(* 'XVID')
out = cv2.VideoWriter("index.mp4", fourcc, 10.0, (640, 480))

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

finger_coordinate = [(8, 6), (12, 10)]

for i in range(10000):

    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    xf = faces[0][0]
    yf = faces[0][1]
    wf = faces[0][2]
    hf = faces[0][3]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multi_land_marks = results.multi_hand_landmarks

    if multi_land_marks:
        hand_points = list()

        for handLms in multi_land_marks:

            for idx, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                hand_points.append((cx, cy))

                
        for point in hand_points:
            cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points)), (max_x_for_hand_rectangle(hand_points), max_y_for_hand_rectangle(hand_points)), (255, 255, 255), 2)


        for coordinate in finger_coordinate:

            if hand_points[8][1] < hand_points[6][1] and hand_points[12][1] < hand_points[10][1] and hand_points[16][1] < hand_points[14][1] and hand_points[20][1] < hand_points[18][1] and hand_points[5][1]> hand_points[6][1] and hand_points[9][1]> hand_points[10][1]:
                helloRectangleColor = (25, 51, 0)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points)), (max_x_for_hand_rectangle(hand_points), max_y_for_hand_rectangle(hand_points)), helloRectangleColor, 2)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), helloRectangleColor, -1)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), helloRectangleColor, 2)
                
                cv2.putText(img, "Hello", (min_x_for_hand_rectangle(hand_points) + 2, min_y_for_hand_rectangle(hand_points) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)



            elif hand_points[8][1] < hand_points[6][1] and hand_points[12][1] < hand_points[10][1] and hand_points[5][1]> hand_points[6][1] and hand_points[9][1]> hand_points[10][1]:
                vitryRectangleColor = (0, 151, 151)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points)), (max_x_for_hand_rectangle(hand_points), max_y_for_hand_rectangle(hand_points)), vitryRectangleColor, 2)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), vitryRectangleColor, -1)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), vitryRectangleColor, 2)

                cv2.putText(img, "vitry", (min_x_for_hand_rectangle(hand_points) + 2, min_y_for_hand_rectangle(hand_points)- 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)



            elif hand_points[4][1] <= hand_points[2][1] and hand_points[4][1] <= hand_points[5][1] and min_value_for_Point_4(hand_points) == True:
                likeRectangleColor = (160, 255, 88)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points)), (max_x_for_hand_rectangle(hand_points), max_y_for_hand_rectangle(hand_points)), likeRectangleColor, 2)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), (160, 255, 88), -1)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), (160, 255, 88), 2)

                cv2.putText(img, "Like", (min_x_for_hand_rectangle(hand_points) + 2, min_y_for_hand_rectangle(hand_points) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)



            elif hand_points[4][1] > hand_points[2][1] and hand_points[4][1] > hand_points[5][1] and max_value_for_point_4(hand_points) == True:
                unLikeRectangleColor = (40,40,239)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points)), (max_x_for_hand_rectangle(hand_points), max_y_for_hand_rectangle(hand_points)), unLikeRectangleColor, 2)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), (40, 40, 239), -1)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), (40, 40, 239), 2)

                cv2.putText(img, "unLike", (min_x_for_hand_rectangle(hand_points) + 2, min_y_for_hand_rectangle(hand_points) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)



            elif hand_points[7][0] > xf and hand_points[7][1] > yf and hand_points[7][0] < xf + wf and hand_points[7][1] < yf + hf:
                vitryRectangleColor = (102,202,0)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points)), (max_x_for_hand_rectangle(hand_points), max_y_for_hand_rectangle(hand_points)), vitryRectangleColor, 2)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), vitryRectangleColor, -1)
                cv2.rectangle(img, (min_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 5), (max_x_for_hand_rectangle(hand_points), min_y_for_hand_rectangle(hand_points) - 35), vitryRectangleColor, 2)

                cv2.putText(img, "silent", (min_x_for_hand_rectangle(hand_points) + 2, min_y_for_hand_rectangle(hand_points) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)



    cv2.imshow('Vineet', img)
    out.write(img)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
print("exit")


# developed  by vineet k. gupt@
# email - vineetkrishnagupta@gmail.com
# linkedin - https://www.linkedin.com/in/vineet-krishna-gupta-6989a5209/
# phone +91 63945-12899, +91 98397-60815