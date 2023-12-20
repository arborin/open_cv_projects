import cv2
import numpy as np

# Read the input image
image = cv2.imread('car3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter to reduce noise while preserving edges
gray_filtered = cv2.bilateralFilter(gray, 11, 17, 17)

# Use Canny edge detector to find edges in the image
edges = cv2.Canny(gray_filtered, 30, 200)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on their area to eliminate noise
min_contour_area = 1000
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

# Sort the contours by area in descending order
sorted_contours = sorted(filtered_contours, key=cv2.contourArea, reverse=True)

# Iterate through the sorted contours to find the possible license plate contour
license_plate_contour = False
for contour in sorted_contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4:
        license_plate_contour = approx
        


        # Draw the license plate contour on the original image
        cv2.drawContours(image, [license_plate_contour], -1, (0, 255, 0), 2)

        # Display the result
        cv2.imshow('Detected License Plate', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
