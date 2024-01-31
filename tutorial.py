import cv2
import numpy as np
# print(cv2.__version__)
# print(cv2.getBuildInformation())
img = cv2.imread('D:/OpenCV/tutorial/asserts/tigre.jpg',-1)
print(type(img))#structure d'un image: un array compose des arrays des lignes, chaque ligne compose des arrays de pixel, chaque pixel est composé de trois valeur: blue, green, red
print(img.shape)#height width,channels
# print(img)
# img = cv2.resize(img, (0,0), fx= 0.5, fy = 0.5)
# # -1, cv2.imread_COLOR : load a color image, any transparentcy of image will be neglected, it is the default flag;
# # 0, cv2.IMREAD_GRAYSCALE : loads image in grayscale mode
# # 1, cv2.IMREAD_UNCHANGED : loads image as including alpha channel
img = cv2.resize(img,(400,400) )
img = cv2.resize(img, (0,0), fx =0.5 ,fy =0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE )
cv2.imwrite("new_img.jpg",img)
if img is not None:
    # Afficher l'image
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("L'image n'a pas été chargée correctement.")



# Error: Please select a valid Python interpreter
print(img[0])
print(img[257][45:400])