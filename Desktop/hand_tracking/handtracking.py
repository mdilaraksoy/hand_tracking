from re import L
import cv2
import mediapipe

camera = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands

hands = mpHands.Hands()

mpDraw = mediapipe.solutions.drawing_utils

while True:

    success, img = camera.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    hlms = hands.process(imgRGB)

    height, width, channel = img.shape

    if hlms.multi_hand_landmarks:
        for handlandmarks in hlms.multi_hand_landmarks:

            for fingerNum, landmark in enumerate(handlandmarks.landmark):
                positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                if fingerNum == 12 and landmark.y < handlandmarks.landmark[11].y:
                    print("raising hand")

                if fingerNum == 7 and landmark.y < handlandmarks.landmark[12].y:
                    print("one finger up")   


            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS) 

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
