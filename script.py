import cv2

cap = cv2.VideoCapture("video path")

while(True):
  ret, frame = cap.read()

  font = cv2.FONT_HERSHEY_COMPLEX
  color = (46, 204, 113)

  cv2.putText(frame, "#StayAtHome", (400, 50), font, 1, color,4, cv2.LINE_8)

  cv2.imshow("video title", frame)

  if(cv2.waitKey(22) & 0xFF == ord("q")):
    break


cap.release()

cv2.destroyAllWindows()