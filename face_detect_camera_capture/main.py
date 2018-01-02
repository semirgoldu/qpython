# Import android from the scripting layer for android
import androidhelper.sl4a as android
# Import opencv
import cv as cv2
from time import sleep
import sys
from PIL import Image
# Initialize Android class
droid = android.Android()
# Start the camera for interactive image capture
cam_cap = '/sdcard/capture.jpg'
droid.cameraInteractiveCapturePicture( cam_cap)

# Resize the image for faster processing
img = Image.open(cam_cap)
reduced_percent=0.1
out = img.resize([int(reduced_percent*s) for s in img.size])
imagePath = "/sdcard/image.jpg"
out.save(imagePath)
sleep(3)
# Set the haarcascade file path
cascPath = "/sdcard/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#save the image
cv2.imwrite('/sdcard/out.jpg', image)
#display the image
droid.view("file:///sdcard/out.jpg","image/*")
