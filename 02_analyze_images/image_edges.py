import cv2
import matplotlib.pyplot as pyplot

print("OpenCV version: ", cv2.__version__)

def show_image(img):
    # pyplot.imshow(img)
    # pyplot.show()
    cv2.imshow('img', img)
    cv2.waitKey()

img = cv2.imread('logo.png')

# detect edges
detected_edges = cv2.Canny(img, 100, 200)
# ret,th2 = cv2.threshold(detected_edges,200,255,cv2.THRESH_BINARY_INV)

# inverted image
inverted_img = 255-detected_edges
show_image(inverted_img)

#save image
cv2.imwrite('edged.png', cv2.cvtColor(inverted_img, cv2.COLOR_RGB2BGR))