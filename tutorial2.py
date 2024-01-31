import cv2
import random
img = cv2.imread('D:/OpenCV/tutorial/asserts/tigre.jpg',-1)

tag = img[500:700, 600:900]
print(type(img))#structure d'un image: un array compose des arrays des lignes, chaque ligne compose des arrays de pixel, chaque pixel est composé de trois valeur: blue, green, red
print(img.shape)#height width,channels
print(img[0])
img[100:300,650:950] = tag

print(img[257][45:400])
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
if img is not None:
    # Afficher l'image
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("L'image n'a pas été chargée correctement.")

# Error: Please select a valid Python interpreter
