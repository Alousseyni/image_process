import  cv2 as cv
import  numpy as np
import  matplotlib.pyplot as plt

#---------------chargement des images-----------------------
imageColorer =cv.imread("../imageATraiter/imageNonContraster.png")
imageNivGris=cv.cvtColor(imageColorer,cv.COLOR_BGR2GRAY)

cv.imshow("Image  Non Egaliser",imageNivGris)
cv.waitKey(0)
cv.destroyAllWindows()
#----------------Histogramme-------------------------------
histo=np.zeros(256,int)
for i in  range(0,imageNivGris.shape[0]):
  for j in range(0,imageNivGris.shape[1]):
      histo[imageNivGris[i,j]] +=1

print("----------Histogrammes------------")
print(histo)
plt.plot(histo)
plt.show()
#-----1er etape Histogramme Cumulé------------
hc = np.zeros(256,int)
hc[0]=histo[0]
for  i in  range(1,256):
  hc[i] =histo[i]+hc[i-1]
print("-------------Histogrammes Cumulé--------------")
print(hc)
plt.plot(hc)
plt.show()
#-------------------Normalisation---------------------
nbrPixels=imageNivGris.size
hc=hc/(nbrPixels*255)
print("-------Histogramme cumulatif normaliser----------")
print(hc)
plt.plot(hc)
plt.show()
#----------------Egaliser------------------------
for  i in range(0,imageNivGris.shape[0]):
  for j in range(0,imageNivGris.shape[1]):
    imageNivGris[i,j]=hc[imageNivGris[i,j]]
cv.imshow("Image Egaliser",imageNivGris)
cv.waitKey(0)
cv.destroyAllWindows()

