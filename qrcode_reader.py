import cv2 as cv2
import os.path
from pyzbar.pyzbar import ZBarSymbol


CAMINHO = "imagens/qrcode01.jpg"

while not os.path.isfile(CAMINHO):
    print("Couldn't open this file\n")
    exit()
    pass


if __name__ == '__main__':
    img = cv2.imread(CAMINHO)
    decoded = decode(img, symbols=[ZBarSymbol.QRCODE])
    print(decoded)
