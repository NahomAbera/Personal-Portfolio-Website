import cv2
import numpy as np

# Load the image (replace 'circle_image.png' with the path to your image)
image = cv2.imread("C:/Users/nahom/Downloads/HeadshotPro Avatar 2024-09-07T17-12-05-243Z.png")

# Create a mask with the same dimensions as the image
height, width = image.shape[:2]
mask = np.ones((height, width, 3), dtype=np.uint8) * 255  # White mask

# Detect where the circle is located and cover it with the rectangle
# You can customize the dimensions of the rectangle as needed
x, y, w, h = 50, 50, 300, 200  # Example values for x, y, width, height of the rectangle
cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 0), -1)

# Apply the mask to the image
result = cv2.bitwise_or(image, mask)

# Save the result
cv2.imwrite('rectangle_image.png', result)

# Display the result (optional)
cv2.imshow('Rectangle Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
