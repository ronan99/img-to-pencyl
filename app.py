
import sys
sys.path.append('./')
from helpers.functions import *
from pathlib import Path
import os
#reading image

def main():
    entry = input("Digite o caminho da imagem que será convertida!\n")

    option = int(input("Qual conversor deseja usar?\n"))

    if(not fileIsValid(entry)):
        print("Imagem inválida")
        return
    if option == 1 :
        convertImageOption1(entry)
    if option == 2 :
        convertImageOption2(entry)
    if option == 3 :
        convertImageOption3(entry)
        

    print("Imagem convertida!\n")


if __name__ == "__main__":
    main()