# import cv2
# import numpy as np
# from skimage.transform import hough_ellipse

# TARGET_SIZE = (640,360)
# while(True):  
#     myimage = cv2.imread('C:/600610720/computer vision/CoinCounting/coin5.jpg')
#     myimage = cv2.resize(myimage, TARGET_SIZE)
#     Pim = myimage
#     myimage = cv2.cvtColor(myimage,cv2.COLOR_BGR2HSV)
#     # mask_Y = cv2.inRange(myimage,(13,120,120),(60,255,255))
#     mask_B = cv2.inRange(myimage,(95,95,90),(105,255,255))
#     # mask_B = hough_ellipse(mask_B, threshold=8)
#     kernel = np.ones((12,12), np.uint8)
    
#     mask_B = cv2.erode(mask_B,kernel,iterations = 1)
#     mask_B = cv2.morphologyEx(mask_B, cv2.MORPH_OPEN, kernel)
#     # myimage= hough_ellipse(myimage, threshold=8)
#     cv2.imshow('image',myimage)
#     # cv2.imshow('mask Yellow',mask_Y)
    
#     cv2.imshow('mask Blue',mask_B)
#     # cv2.imshow('pure image',Pim)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # from skimage.transform import hough_ellipse
# # from skimage.draw import ellipse_perimeter
# # img = np.zeros((25, 25), dtype=np.uint8)
# # rr, cc = ellipse_perimeter(10, 10, 6, 8)
# # img[cc, rr] = 1
# # result = hough_ellipse(img, threshold=8)
# # result.tolist()
import cv2
import numpy as np

img = cv2.imread('C:/600610720/computer vision/CoinCounting/coin5.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()