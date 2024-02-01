#detecter même choses
#meme size (pixel)
import cv2
import numpy as np
img = cv2.imread("tutorial/asserts/soccer_practice.jpg",0)
img = cv2.resize(img, (0,0),fx=0.2,fy =0.2)
# template = cv2.imread("tutorial/asserts/ball.PNG",0)#gray scale, algorithme demande gray scale
template = cv2.imread("tutorial/asserts/shoe.PNG",0)#gray scale, algorithme demande gray scale
template = cv2.resize(template,(0,0),fx = 0.2, fy=0.2  )
h, w = template.shape#que deux dimention, car c'est un gray scale image
print(img)
# meths: 
methodes = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
for methode in methodes:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template,methode)#un autre array de deux dimentions
    #(W -w+1, H -h+1): W: largeur de la base d'image: img2, w est largeur de l'image template
    min_val, max_val, min_loc, max_loc =cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    if methode in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else :
        location = max_loc
    botom_right = (location[0]+w,location[1]+h)
    cv2.rectangle(img2, location,botom_right, 255, 5 )
    cv2.imshow("math",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
