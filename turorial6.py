import cv2
import numpy as np 
img = cv2.imread('tutorial/chessBord.jpeg')
img = cv2.resize(img, (0,0), fx = 0.75, fy = 0.75)
# convert l'image à gris scale d'abord
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)# arguments: source d'image, le nombre de meilleurs corners, minimum qualité de corner(0-1), minimume distance entre euclidean distance entre les corners retourner
#display the corners
print(corners)#ce sont des floats
corners = np.int0(corners)
print(corners)
for corner in corners:
    print(corner)
    # corner = corner[0]
    x, y = corner.ravel() #ravel rendre an array faltten, rendre plusieurs dimention en une dimention
    cv2.circle (img, (x, y), 5, (255, 0, 0), -1)#source d'image, centre du cercle, radio, couleur, épaisseur
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 =tuple( corners[j][0])
        color = tuple(map(lambda x : int(x), np.random.randint(0, 255,size=3) )) #c'est quoi tuple? revoir map
        cv2.line(img, corner1, corner2,(color), 1)#random color


if img is not None:
    cv2.imshow('frame', img)
    # cv2.imshow ()
    # cv2.imshow("corners", corners)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
