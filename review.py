import  cv2 as cv
import  numpy as np
import  matplotlib.pyplot as plt

#--------------------Comment charger une image et conversion ----------------------
imageCouleur = cv.imread("../imageATraiter/lena.png")
imageNivGris=cv.imread("../imageATraiter/lena.png",cv.IMREAD_GRAYSCALE)#cv.IMREAD_GRAYSCALE == 0
#imageNivGris=cv.cvtColor(imageCouleur,cv.COLOR_BGR2GRAY)

# imageNivGris = np.zeros(256,int) # vecteur de 256 zeros
# B,G,R=cv.split(imageCouleur)
# imageNivGris=0.299*R+0.587*G+0.114*B
# imageNivGris=imageNivGris.astype(np.uint8)

#------------------Modifier une modifier de pixel----------------------------
#-------------------Ajouter une ligne verticale blanche (en Colonne 100) sur une ligne--------------------------
# for  i in range(0,imageCouleur.shape[0]):
#      imageCouleur[i,100]=[255,255,255]

#--------------Quart superieur gauche----------------------
# for  i in range(0,imageCouleur.shape[0]//2):
#     for j in range(0,imageCouleur.shape[1]//2):
#         imageCouleur[i,j,0]=0
# plt.imshow(imageCouleur)
# plt.show()

# for  i in range(imageCouleur.shape[0]//2,imageCouleur.shape[0]):
#     for j in range(imageCouleur.shape[1]//2,imageCouleur.shape[1]):
#         imageCouleur[i,j,2]=0
# plt.imshow(imageCouleur)
# plt.show()


# for  i in range(0,imageCouleur.shape[0]//2):
#     for j in range(imageCouleur.shape[1]//2,imageCouleur.shape[1]):
#         imageCouleur[i,j,1]=0
# plt.imshow(imageCouleur[...,::-1])
# plt.show()

# for  i in range(imageCouleur.shape[0]//2,imageCouleur.shape[0]):
#     for j in range(0,imageCouleur.shape[1]//2):
#         imageCouleur[i,j,2]=0
# plt.imshow(imageCouleur[...,::-1])
# plt.show()
#----------Passons d'une photo (noir-blanc) a son negative(blanc-noir)
imageNivGrisComplement =255 - imageNivGris








#--------------------Affichage des Caracteristique------------------------
#print("----------image en couleur--------------")
# print(imageCouleur.shape)
# print(imageCouleur[0,0])

# print("----------Image en Niveau de Gris--------------")
# print(imageNivGris.shape)
# print(imageNivGris[0,0])
#------------------Enregistrement d'une image------------------------
#cv.imwrite("../imageATraiter/lenaGris.png",imageNivGris)
#-----------------Visualiser L'image------------- -------------
#------------Matplotlib.pyplot----------------
# plt.imshow(imageCouleur[...,::-1])
# plt.show()

# plt.imshow(cv.cvtColor(imageNivGris,cv.COLOR_BGR2RGB))
# plt.show()

#------------------openCV---------------------

cv.imshow("Image en couleurs",imageCouleur )
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Image en niveau de gris",imageNivGris)
cv.waitKey(0)
cv.destroyAllWindows()


cv.imshow("Image en niveau de gris",imageNivGrisComplement)
cv.waitKey(0)
cv.destroyAllWindows()