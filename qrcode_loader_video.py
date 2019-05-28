# import the necessary packages
from pyzbar import pyzbar
from PIL import Image
from io import BytesIO
import urllib.request
import cv2 as cv


TEMP = 'imagens/temp.jpg'

if __name__ == '__main__':
    # initialize the camera
    cap = cv.VideoCapture(0)

    while(True):
        # start the frame captures
        ret, frame = cap.read()

        try:
            # find the barcodes in the image and decode each of the barcodes
            barcodes = pyzbar.decode(frame)
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
                print(f'{err}')
                print(f'Pau no seu cu vacilao')

            img = Image.open(BytesIO(the_page))
            img.save(TEMP)
        except:
            pass
        finally:
            # show the video frames
            cv.imshow('frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()
