from PIL import Image
import pytesseract
import traceback
class Image_go:
    def image_go(self,image_addres):
        try:
            # c=open(image_addres)
            im = Image.open(image_addres)
            # jiage = pytesseract.image_to_string(im,lang='chi_sim')
            jiage = pytesseract.image_to_string(im)
            return jiage
        except Exception as e:
            ee = traceback.format_exc()
            print(ee)


if __name__ == "__main__":
    a=Image_go().image_go("b.png")
    print(a)