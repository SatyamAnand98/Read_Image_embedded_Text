try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys

reload(sys)
sys.setdefaultencoding('utf8')


'''
Syntax:
image_to_data(image, lang=None, config='', nice=0, output_type=Output.STRING, timeout=0)
'''

print(pytesseract.image_to_string(Image.open('/home/stoneduser/Desktop/test.png')))
