import cv2
import imutils
import numpy as np
# pytesseract.pytesseract.tesseract_cmd =r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = cv2.imread('car4.jpg')
img = imutils.resize(img, width=500)

# cv2.imshow('Original Image', image)
# cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray)
cv2.waitKey(0)


bfilter = cv2.bilateralFilter(gray, 11,17,17)
edged = cv2.Canny(bfilter, 30, 200)
cv2.imshow("Edged Image", edged)
cv2.waitKey(0)


# Find contours in the binary image
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Select the top 10 largest contours based on area
top_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]


location = None
for conture in contours:
    approx = cv2.approxPolyDP(conture, 10, True)
    x1,y1 = conture[0][0]
    
    if(len(approx) == 4):
        location = approx
        
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(conture)
            ratio = float(w)/h
            if ratio >= 0.9 and ratio <= 1.1:
                img = cv2.drawContours(img, [conture], -1, (0,255,255), 3)
                cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            else:
                cv2.putText(img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                img = cv2.drawContours(img, [conture], -1, (0,255,0), 3)
            
            cv2.imshow("Edged Image", img)
            cv2.waitKey(0)
            
# print(location)







# # edge detection
# corner = cv2.Canny(gray, 30, 200)
# cv2.imshow("Highlighted edges", corner)
# cv2.waitKey(0)

# # კონტურების აღმოჩენა
# # Find contours in the binary image
# contours, _ = cv2.findContours(corner.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Sort contours based on area in descending order and select the top 20
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]

# NoPlate = None

# # image2 = image.copy()
# # cv2.drawContours(image2, seg, -1, (0,255,0),3)
# # cv2.imshow("Number plate segmention", image2)
# # cv2.waitKey(0)

# # count = 0
# # name = 1
# location = None
# for conture in contours:
#     approx = cv2.approxPolyDP(conture, 10, True)
#     if(len(approx) == 4):
#         location = approx
#         break
# print(location)

# mask = np.zeros(gray.shape, np.uint8)
# new_image = cv2.drawContours(mask, [location], 0,255,-1)
# new_image = cv2.bitwise_and(image, image, mask=mask)

# cv2.imshow("Highlighted edges", new_image)
# cv2.waitKey(0)
