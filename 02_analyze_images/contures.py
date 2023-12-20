import cv2
import matplotlib.pyplot as pyplot

print("OpenCV version: ", cv2.__version__)

def show_image(img):
    # pyplot.imshow(img)
    # pyplot.show()
    cv2.imshow('img', img)
    cv2.waitKey()

img = cv2.imread('logo.png')

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show_image(gray_image)

# pyplot.contour(gray_image, origin="image")

ret, thresh = cv2.threshold(gray_image, 150, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# show_image(img)

car = cv2.imread('car.jpg')
show_image(car)

# GRAYSACLE
gray_car = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
show_image(gray_car)

# FIND CONTURES
ret, thresh = cv2.threshold(gray_car, 150, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(car, contours, -1, (0, 255, 0), 3)
show_image(car)

# SAVE IMAGE
cv2.imwrite('car_contours.png', car)