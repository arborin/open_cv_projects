import cv2

damaged = cv2.imread('damaged.png')
cv2.imshow('title', damaged)
cv2.waitKey()

damaged_mask = cv2.imread('logo.png')
cv2.imshow('title', damaged_mask)
cv2.waitKey()


threshbold_value = 254
output_value = 255
ret, thresh = cv2.threshold(damaged_mask, threshbold_value, \
    output_value, \
        cv2.THRESH_BINARY
        )
# print(ret)
# print(thresh)
cv2.imshow('img', thresh)
cv2.waitKey()