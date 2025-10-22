import cv2

img_num = int(input("Enter image number: "))
img = cv2.imread(f"{img_num}.jpg")
h, w, c = img.shape
output = img.copy()

for y in range(h):
    for x in range(w):
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)
        
        is_red = False
        
        if img_num == 5:
            is_red = r > 50 and r > g + 30 and r > b + 30 and g < 150 and b < 150
        elif img_num == 7:
            is_red = r > 110 and r > 1.5 * g and g < 120
        elif img_num in [1, 2, 3, 6, 8]:
            is_red = r > 1.65 * g and r > 1.65 * b
        elif img_num == 4:
            is_red = r > 1.8 * g and r > 1.1 * b
        
        if is_red:
            continue
        else:
            output[y, x] = [0, 0, 0]

cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()