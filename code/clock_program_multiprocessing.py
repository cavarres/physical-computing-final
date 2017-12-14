import multiprocessing

#Face detection libraries
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils
#Servo Control libraries
import time
import wiringpi


######Servo set up

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

def findFace(q):
   	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

	# initialize the camera and grab a reference to the raw camera capture
	camera = PiCamera()
	camera.resolution = (160, 128)
	camera.framerate = 30
	rawCapture = PiRGBArray(camera, size=(160, 128))

	# allow the camera to warmup
	time.sleep(0.1)
	lastTime = time.time()*1000.0

	# capture frames from the camera
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	    print "beginning of camera loop", q
	        # grab the raw NumPy array representing the image, then initialize the timestamp
	        # and occupied/unoccupied text
	    image = frame.array
	    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	    # Detect faces in the image
	    faces = face_cascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	    )
	    number_faces = len(faces)

	    print time.time()*1000.0-lastTime," Found {0} faces!".format(len(faces))
	    lastTime = time.time()*1000.0
	    
	    #cv2.imshow("Frame", image)
	    key = cv2.waitKey(1) & 0xFF

	    # clear the stream in preparation for the next frame
	    rawCapture.truncate(0)

	        # if the `q` key was pressed, break from the loop
	    if key == ord("x"):
	        break

def clockMoving(q):
     n_lost = 0
     while True:
        if q.empty() is not False:
        	wiringpi.pwmWrite(18, 5)
        	time.sleep(0.27)
        	wiringpi.pwmWrite(18, 0)
        	time.sleep(0.73)
        	print q.get()
    	else:
    		the_value = q.get()
    		if the_value > 0:
	        	wiringpi.pwmWrite(18, 149)
	        	time.sleep(0.14*(n_lost*2)/(1-0.14))
	        	wiringpi.pwmWrite(18, 149)
	        	time.sleep(0.14)
	        	wiringpi.pwmWrite(18, 0)
	        	time.sleep(0.86)
	        	print "n lost =", n_lost
	        	print the_value
	        	n_lost = 0
	        else:
	        	wiringpi.pwmWrite(18, 146)
	        	time.sleep(0.32)
	        	wiringpi.pwmWrite(18, 0)
	        	time.sleep(0.68)
	        	print "n lost =", n_lost
	        	print the_value
	        	n_lost += 1


if __name__ == "__main__":

    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=findFace, args=(q,))
    p.start()
    m = multiprocessing.Process(target=clockMoving, args=(q,))
    m.start()
