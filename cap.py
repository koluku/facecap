import cv2
import time
from datetime import datetime

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    cascade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    color = (255, 255, 255)
    thickness = 2

    while True:
        i = 0
        date = datetime.now()
        ret, frame = cap.read()
        facerect = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(96, 96))

        if len(facerect) > 0:

            for rect in facerect:
                cv2.imwrite("faces" + "/" + date.strftime('%Y-%m-%d-%H.%M.%S_') + "{}.jpg".format(i), frame[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
                cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), color, thickness)
                i += 1

        cv2.imshow("frame", frame)
        time.sleep(3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.dstroyAllWindows()
