# import the necessary packages
from pyzbar import pyzbar
from PIL import Image
from io import BytesIO
import os.path
import urllib.request
import cv2 as cv


CAMINHO = 'imagens/qrcode_sandy_junior.png'
TEMP = 'imagens/temp.jpg'

while not os.path.isfile(CAMINHO):
    print("Couldn't open this file\n")
    exit()
    pass


if __name__ == '__main__':
    # load the input imageQRCode
    image_code = cv.imread(CAMINHO)

    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image_code)

    # loop over the detected barcodes
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        print(f'[INFO] Found {barcodeType} barcode: {barcodeData}')

    # get the page content from url
    try:
        with urllib.request.urlopen(barcodeData) as response:
            # print(f'{response.getcode()}')
            the_page = response.read()
    except OSError as err:
        print(f'{err.code}')
        print(f'Pau no seu cu vacilao')
        exit()

    # converts the content page from image and save a temp image
    img = Image.open(BytesIO(the_page))
    img.save(TEMP)

    image = cv.imread(TEMP)
    cv.imshow('IMAGE from TEMP', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
