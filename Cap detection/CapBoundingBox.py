import cv2

image = cv2.imread("1.JPG")
h, w, c = image.shape
output = image.copy()


xmin, ymin = w, h
xmax, ymax = 0, 0


for y in range(h):
    for x in range(w):
        b, g, r = image[y, x]

        if r > 100 and r > 1.5 * g and r > 1.3 * b:
            if x < xmin: xmin = x
            if x > xmax: xmax = x
            if y < ymin: ymin = y
            if y > ymax: ymax = y
        else:
           
            output[y, x] = [0, 0, 0]

cv2.rectangle(output, (xmin, ymin), (xmax, ymax), (255, 255, 255), 2)

cv2.imshow("Cap Bounding Box", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
