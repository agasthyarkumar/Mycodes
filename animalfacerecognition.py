import cv2
# Load the pre-trained dog face classifier
dog_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
# Load an image for detection
img = cv2.imread('dog_image.jpg')
# Convert the image to grayscale for face detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect dog faces in the image
dog_faces = dog_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
# Draw rectangles around the detected dog faces
for (x, y, w, h) in dog_faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# Display the image with detected dog faces
cv2.imshow('Dog Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
