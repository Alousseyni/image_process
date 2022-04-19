import  cv2 as cv
import  numpy as np
import  matplotlib.pyplot as plt


#-------------chargement des images-----------------
image =cv.imread("../imageATraiter/lena.png")
message =cv.imread("../imageATraiter/imageCacher.png",0)

# #---------criptage avec la methode simple--------
# # b,v,r =cv.split(image)
# # b=b&0b11111110
# # b=b|(message>0)

# # imageCripter=cv.merge((b,v,r))

# # cv.imwrite("imageCripter.png",imageCripter)

# #------------Criptage discret-------------
b,v,r =cv.split(image)
b=b&0b11111110
b=b|(message>0)^(v&1)

imageCripter=cv.merge((b,v,r))

cv.imwrite("imageCripter.png",imageCripter)
#-------------------------Decriptage Simple----------------------
# imageCripterPret=cv.imread("imageCripter.png")
# B,V,R=cv.split(imageCripterPret)
# imageDeCripter=B&1
# imageDeCripter=imageDeCripter*255

# #----------------------Decriptage complexe-----------------------
imageCripterPret=cv.imread("imageCripter.png")
B,V,R=cv.split(imageCripterPret)
imageDeCripter=(B&1)^(V&1)
imageDeCripter=imageDeCripter*255

cv.imshow("Image Original",image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Image Original",message)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("image Cripter",imageCripter)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("image Decripter",imageDeCripter)
cv.waitKey(0)
cv.destroyAllWindows()


