import  cv2 as cv
import  numpy as np
import  matplotlib.pyplot as plt

imgPath="./images/smiley_nb.png"
img=cv.imread(imgPath,0)
plt.imshow(img,cmap='gray')
plt.show()
#----------Image Parameters---------------
print('image shape')
print(img.shape)
#------------- Les Masques-----------------
# kernelAcross=cv.getStructuringElement(cv.MORPH_CROSS, (5,5))
# print(kernelAcross)
# plt.imshow(kernelAcross,cmap='gray')
# plt.show()

# kernelCircle=cv.getStructuringElement(cv.MORPH_ELLIPSE,(20,20))
# print(kernelCircle)
# plt.imshow(kernelCircle,cmap='gray')
# plt.show()

# kernelRectangle=cv.getStructuringElement(cv.MORPH_RECT, (5,5))
# print(kernelRectangle)
# plt.imshow(kernelRectangle,cmap='gray')
# plt.show()
