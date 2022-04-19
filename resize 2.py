import  numpy as np
import  cv2 as cv
import  matplotlib.pyplot as plt

#----------Chargement--------------
imgPath="./images/lena_large.png"
imgColor=cv.imread(imgPath)

#---------Fonction resize--------------
def  rescaleImage(frame,scale=0.5):
        width=int(frame.shape[1]*scale)
        height=int(frame.shape[0]*scale)
        dimension =(width,height)
        return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

resize_image=rescaleImage(imgColor)

cv.imshow("Lenna.png",imgColor)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Resize  lenna.png",resize_image)
cv.waitKey(0)
cv.destroyAllWindows()
