from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image = frame.array

    cv.imshow('Image', image)
    
    if cv.waitKey(1) == 27:
        break
    
    rawCapture.truncate(0)
    
    
cv.destroyAllWindows()
