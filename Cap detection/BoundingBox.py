import cv2
import numpy as np

black_canvas = np.zeros((500, 500, 3), dtype=np.uint8)


image = cv2.circle(black_canvas, (250, 250), 50, (255, 200, 150), -1)  # filled circle

xmin, ymin = 500, 500
xmax, ymax = 0, 0

for y in range(500):
    for x in range(500):
        b, g, r = image[y, x]
        if b > 0 or g > 0 or r > 0: 
            if x < xmin: xmin = x
            if x > xmax: xmax = x
            if y < ymin: ymin = y
            if y > ymax: ymax = y

# Draw bounding box
cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 255, 255), 2)

# Show output
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
