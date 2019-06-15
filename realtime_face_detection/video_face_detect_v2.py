import numpy as np
import urllib
import cv as cv2
from time import sleep
import sys
from PIL import Image
import socket
import androidhelper.sl4a as android
from StringIO import StringIO
import urllib
from time import sleep
import threading

scaling_factor=10

def url_to_image():
	url = "http://192.168.43.1:8081/shot.jpg"
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	res = urllib.urlopen(url)
	image = np.asarray(bytearray(res.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# perform the actual resizing of the image according to scaling_factor
	height, width = image.shape[:2]
	resized = cv2.resize(image, (width/scaling_factor, height/scaling_factor), interpolation = cv2.INTER_AREA)
	# Return gray sale image
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	return gray
# Set the haarcascade file path
cascPath = "/sdcard/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# Open a flask connection to sl4a server to send information to takser
# If your QPython is able to send messages to tasker directly use script version #2

def recognition():
	while True:
		# Get frame from video
		image_new = url_to_image()
		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.2,
    		minNeighbors=5,
    		minSize=(10, 10),
    		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		# Print result
		print("Found {0} faces!".format(len(faces)))
	
		# Draw a rectangle around the faces
		# Counter variable if you want multiple face detections
		cnt=1
		for (x, y, w, h) in faces:
			#print w,h,x,y
			# Multiply our result with our scaling factor 10
			dim = str(w*scaling_factor)+","+str(h*scaling_factor)+","+str(x*scaling_factor)+","+str(y*scaling_factor)
			#print dim
			# Set %Vals variable in tasker to trigger our Profile
			# Your script to set %Vals variable value to dim
				# Example : tasker_set_variable ("%Vals***",dim)
			
			cnt=cnt+1
if __name__=='main':
	recognition()
	

	
	
