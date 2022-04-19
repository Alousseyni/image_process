import  numpy as np
import  cv2 as cv
import  matplotlib.pyplot as plt

#-----------------------------------------------Chargement de l'image----------------------------------------------
imagePath="/Users/admin/Desktop/all programs/my codes/traitement-image/imageATraiter/imageNonContraster.png"
#imageGris=cv.imread(imagePath,cv.IMREAD_GRAYSCALE)
image=cv.imread(imagePath)
B,G,R=cv.split(image)
imageGris = 0.299 * R + 0.587 * G + 0.114*B
imageGris = imageGris.astype(np.uint8)
#imageGris=cv.cvtColor(image,cv2.COLOR_BGR2GRAY)

imageColorer=cv.imread(imagePath)
#----------------------------------------------Affichage des images-------------------------------------------------
print(imageColorer.shape)
print(imageColorer[0,0])
print("----------------------------")
print(imageGris.shape)
print(imageGris[0,0])

cv.imshow("image de lena sans contraste",imageColorer)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("image de lena sans contraste",imageGris)
cv.waitKey(0)
cv.destroyAllWindows()

# #------------------------------

# B,G,R=cv.split(image)
# imageGris = 0.299*R + 0.587*G +0.114*B
# imageGris = imageGris.astype(np.uint8)
# imageGris=cv.cvtColor(image,cv2.COLOR_BGR2GRAY)

#----------------------------------------------Histogramme-------------------------------------------------
histo =np.zeros(256,int) # vecteur de 256 zeros
for i in range(0,imageGris.shape[0]):
    for  j in range(0,imageGris.shape[1]):
          histo[imageGris[i,j]] +=1
print(histo)
plt.plot(histo)
plt.show()
#--------------------------------------Histogramme cumule--------------------------------------------
hc = np.zeros(256,int)
hc[0]=histo[0]
for  i in  range(1,256):
  hc[i] =histo[i]+hc[i-1]

print("histogramme cumulé avant la normalisation")
print(hc)
plt.plot(hc)
plt.show()
#-----------------------------------Normalisation de mon histograme cumule-----------------------
nbrPixels=imageGris.size
hc = hc/(nbrPixels*255)

print("histogramme cumulé apres la normalisation")
print(hc)
plt.plot(hc)
plt.show()
#----------------------------------contraste avec consideration de hc comme table de conversion-------------------------
for  i in range(0,imageGris.shape[0]):
    for j in range(0,imageGris.shape[1]):
        imageGris[i,j]=hc[imageGris[i,j]]
cv.imshow("L'image egaliser",imageGris)
cv.waitKey(0)
cv.destroyAllWindows()