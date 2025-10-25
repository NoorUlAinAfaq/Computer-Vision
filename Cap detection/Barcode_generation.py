import cv2
import numpy as np

canvas = np.ones((500, 500, 3), dtype=np.uint8) * 255
code = [2, 1, 3, 0]
bar_width = 10
max_height = 180
start_x = 20

for idx, num in enumerate(code):
    print(idx,num)
    bar_height = num*40 + 20
    top_y = bar_height

    for y in range(0, top_y):
        for x in range(start_x, start_x + bar_width):
            canvas[y, x] = [0, 0, 0]

    start_x += bar_width + 5

    


cv2.imshow("Output", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()