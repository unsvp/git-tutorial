import numpy as np
import cv2


cap = cv2.VideoCapture(0)
#cap.SetCaptureProperty(cap, CV_CAP_PROP_FRAME_WIDTH, 1280)
#cv2.SetCaptureProperty(cap, CV_CAP_PROP_FRAME_HEIGHT, 720)

w = cap.get(3)
h = cap.get(4)
w, h = int(w), int(h) # По умолчанию возвращаются как float
print("Camera default settings: ",w,"x",h)

#cap.set(3, 1280)
#cap.set(4, 720)
#w = cap.get(3)
#h = cap.get(4)
#w, h = int(w), int(h) # По умолчанию возвращаются как float
#print("camera set: ",w,"x",h)

#cv.SetCaptureProperty(self.cap,cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
#cv.SetCaptureProperty(self.cap,cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = 30
w, h = 640, 480
#w, h = 1280, 720
stream = cv2.VideoWriter("test.avi", fourcc, fps, (w, h))

while cap.isOpened():
	result, frame = cap.read()
	cv2.imshow('Press q for quit',frame)
	stream.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()