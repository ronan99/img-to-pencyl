import os
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
from sketchify import sketch

plt.style.use('seaborn')

FORMATS = [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"]

def getImageName(full_path):
    aux = full_path.split("/")[-1]
    image_name = aux.split("\\")[-1]
    
    return image_name

def fileIsValid(path_to_image):
    
    if not os.path.isfile(path_to_image):
        return False
    aux = Path(path_to_image)
    file_format = aux.suffix.lower()
    
    if( file_format in FORMATS):
        return True
    
def getPathToSave(path , conversor = ""):
    image_name = getImageName(path)
    pathSplitted = path.split("/")
    pathSplitted = "\\".join(("".join(pathSplitted)).split("\\")[:-1])
    
    aux = image_name.split('.')
    # print(pathSplitted + "\\" + aux[0] + "_pencyl." + aux[1])
    return pathSplitted + "\\" + aux[0] + "_pencyl" + conversor + "." + aux[-1]


def convertImageOption1(entry):
    image = cv2.imread(entry)

    #converting BGR image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #image inversion
    inverted_image = 255 - gray_image

    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    # print(getPathToSave(entry , "1"))
    # return
    cv2.imwrite(getPathToSave(entry , "1") , pencil_sketch)
    # cv2.imshow("Original Image", image)
    # cv2.imshow("Pencil Sketch of Dog", pencil_sketch)
    cv2.waitKey(0)

def convertImageOption2(entry):
    img = cv2.imread(entry)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    
    final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
    
    cv2.imwrite(getPathToSave(entry, "2") , final)
    
    
def convertImageOption3(entry):
    sketch.normalsketch(entry, "\\".join(getPathToSave(entry).split("\\")[:-1]) , getImageName(entry).split(".")[0] + "_pencyl3" , scale = 10)