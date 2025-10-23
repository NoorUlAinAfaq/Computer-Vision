import cv2
import numpy as np

img = np.zeros((200,200,3))

cv2.circle(img,(20,20),10,(0,255,0),-1)



def bbox(img):
    
    for y in range(0,200):
        for x in range(0,200):
            img2=img.copy()
            
            cv2.rectangle(img2,(x,y),(x+4,y+4),(0,255,255),-1)
            if(img[y,x][1]==255):
                
                while(True):
                    if(img[y,x][1]==255):
                        y+=1
                        print(y)
                    else:
                        break
                
                cv2.rectangle(img2,(0,y),(x+1,y),(255,0,255),-1)
                
                #cv2.rectangle(img2,(x,y),(x+4,y+4),(255,0,255),-1)
                cv2.imshow("n",img2)
                cv2.waitKey(0)
                break
            cv2.imshow("n",img2)
            cv2.waitKey(1)


bbox(img)

cv2.imshow("n",img)
cv2.waitKey(0)