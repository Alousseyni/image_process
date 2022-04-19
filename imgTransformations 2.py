import  cv2 as cv
import  numpy as np 
import  matplotlib.pyplot as plt 

imgPath="./images/Woman.jpeg"
image=cv.imread(imgPath)
cv.imshow('Alicia.jpeg Original image',image)
cv.waitKey(0)
#-----Translate-----------
def  translation(image,x,y):
        transMat=np.float32([[1,0,x],[0,1,y]])
        dimensions=(image.shape[1], image.shape[0])
        return cv.warpAffine(image,transMat,dimensions)
  
# imageTranslater=translation(image ,0 ,50)
# cv.imshow('Image translater',imageTranslater)
# cv.waitKey(0)

# imageTranslater=translation(image , 50 ,0)
# cv.imshow('Image translater',imageTranslater)
# cv.waitKey(0)

# imageTranslater=translation(image , -50 ,0)
# cv.imshow('Image translater',imageTranslater)
# cv.waitKey(0)

# imageTranslater=translation(image ,0 ,-50)
# cv.imshow('Image translater',imageTranslater)
# cv.waitKey(0)


#------------Rotate---------------
def  rotation(img, angle, rotPoint=None):
        (height,width)=img.shape[:2]
        if  rotPoint is None:
            rotPoint=(width//2,height//2)
        rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions=(width,height)

        return cv.warpAffine(img,rotMat,dimensions)
# rotatedImage=rotation(image,45)
# cv.imshow('Image rotate anti-wise clock',rotatedImage)
# cv.waitKey(0)

# rotatedImage_rotate=rotation(rotatedImage,45)
# cv.imshow("rotate more further",rotatedImage_rotate)
# cv.waitKey(0)

rotatedImageInvert=rotation(image,-45)
cv.imshow("rotation anti-wise clock",rotatedImageInvert)
cv.waitKey(0)

cv.destroyAllWindows()