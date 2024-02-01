import cv2
import numpy as np 
#define the camera device
cap = cv2.VideoCapture("tutorial\TobocanAvecLesGrandsParents.mp4")# numero de webcam ou camera dans le parametre presise quel camara qu'on utilise ou un string avec le nom du document pour indiquer le document d'un vidéo
print(cap)
#setup un whild loop, displyaing le video ou capture
while True:#get un frame
    ret, frame = cap.read()# un image ret indique si le camera marche(true ou false)
    #pour savoir le longeur et largeur de frame
    width = int(cap.get(3))#identifier le properté, 3 est largeur, 4 est longeur
    height = int(cap.get(4))#on ne peut pas utiliser un float pour slice image
    img = cv2.line(frame,(0,0),(width, height),(255,0,0 ), 10)#(target, deux point pour indiquer une ligne :(0,0)est top left of the corner, couleur(BGR), épaisseur de la ligne)
    img = cv2.line(img,(0,height),(width, 0),(255,0,0 ), 10)#(target, deux point pour indiquer une ligne :(0,0)est top left of the corner, couleur(BGR), épaisseur de la ligne)
    img = cv2.rectangle(img, (100, 100),(200,200), (128,128,128), -1)#(target, deux points, deux triangles basé sur ces deux points construit le rectangle, puis couleur, et épaisseur, si c'est négatif, il va remplir tous le réctangle
    print(ret)
    img = cv2.circle(img, (300, 300), 60, (0,0, 255), -1)#source d'image, le point centre du cercle , radio, couleur, épaisseur
    # pour ajouter un text
    #d'abore ajouter un font
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Tim is great !", (10, height -10), font,1, (0,0,0), 5,cv2.LINE_AA)#botom  right corner: source d'image, text, centre posiiton, font, font scale, couleur, epaisseur de la ligne de text, type de ligne(style)
    #rendre le frame en 4 images séparé et les mettre ensemble
    #1.créer un containeur pour stocker les 4 images
    image = np.zeros(frame.shape, np.uint8)#à défaut, c'est vide, avec le meme shape que frame, np.unit8 est le type de arraylist, type de valeur, unsigned integer eigth bits
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy=0.5)
    # image[:height//2, :width//2] = smaller_frame
    # image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = smaller_frame
    # image[height//2:, width//2:] = smaller_frame
    image[:height//2, :width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame
    img = cv2.line(frame,(0,0),(width, height),(255,0,0 ), 10)#(target, deux point pour indiquer une ligne :(0,0)est top left of the corner, couleur(BGR), épaisseur de la ligne)
#display the frame
    if ret == True :
        cv2.imshow('frame', image)
        if cv2.waitKey(1) == ord('q'):#attend 1 millon secondes, ou en appuyant le q, returne the ordinal value égale q
            break
    else:
        break
cap.release() #release the camera resources(au cas ou les autres ont utilisé le caméra)
cv2.destroyAllWindows()