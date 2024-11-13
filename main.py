from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)


while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    if hands:
        fingers=detector.fingersUp(hands[0])
        print(fingers)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()