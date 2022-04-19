import  cv2 as cv 
import  numpy as np 
import  matplotlib.pyplot as plt 

imgPath="./images/clara.jpeg"

imgColor=cv.imread(imgPath)

cv.imshow('Clara.jpeg',imgColor)
cv.waitKey(0)
# 1.- blurring an image
blurImages=cv.GaussianBlur(imgColor, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur image',blurImages)
cv.waitKey(0)
#2. Edge image
cannyImg =cv.Canny(imgColor,125,150)
cv.imshow('Edge of the image',cannyImg)
cv.waitKey(0)
cannyBlurImg=cv.Canny(blurImages,130,175)
cv.imshow('Edge of the blrring image',cannyBlurImg)
cv.waitKey(0)
# #blank=np.zeros((512,512,3),dtype='uint8')
# # blank[200:300,300:400]=0,0,255

# #cv.rectangle(blank,(0,0),(300,300),(0,255,0),thickness=2)


cv.destroyAllWindows()
