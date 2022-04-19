import  cv2 as cv
import  numpy as np
import  matplotlib.pyplot as plt

#---------------------cahrgement d'image-----------------
imagePathLena="/Users/admin/Desktop/all programs/my codes/traitement-image/imageATraiter/lena.png"
imagePathCacher="/Users/admin/Desktop/all programs/my codes/traitement-image/imageATraiter/imageCacher.png"
image =cv.imread(imagePathLena)
message=cv.imread(imagePathCacher,0)

cv.imshow("Lena.png",image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Image a cacher dans lena.png en version gris",message)
cv.waitKey(0)
cv.destroyAllWindows()

#------------------------Cacher une image d'info dans une autre ------------------------
# b,v,r =cv.split(image)
# b=b & 0b11111110 #effacer le bit de poids faible des octets de b
# b=b | (message > 0) # ajouter le bit de poids faible en fonction du message

#--------Cacher plus discretement---------
b,v,r =cv.split(image)
b=b & 0b11111110 
b=b | (message > 0) ^ (v&1)


cacher =cv.merge((b,v,r))
cv.imwrite("Cacher.png",cacher)

cv.imshow("Image avec contenu cacher",cacher)
cv.waitKey(0)
cv.destroyAllWindows()

#---------------------Algo de Decodage --------------------

##----decodage avec cryptage simple-------------------

#-------Chargement de l'image crypter precedement--------------
# imageCrypter = cv.imread("cacher.png")

# B,V,R=cv.split(imageCrypter)
# cacher1 = B & 1 # extraire la 1er bit (de poids faible)
# cacher1 = cacher1*255

# cv.imshow("Image decrypter ",cacher1)
# cv.waitKey(0)
# cv.destroyAllWindows()
##-------------decodage avec cryptage complexe----------------
imageCrypter = cv.imread("cacher.png")

B,V,R=cv.split(imageCrypter)
imageDeCrypter = (B & 1)^(V&1)
imageDeCrypter=imageDeCrypter*255

cv.imshow("Image decrypter ",imageDeCrypter)
cv.waitKey(0)
cv.destroyAllWindows()