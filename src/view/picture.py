from PIL import Image, ImageDraw
from datetime import *

class Picture:
    def __init__(self, x= 500, y= 300):
        self.x = x
        self.y = y
        self.image = Image.new('RGB', (x, y), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)


    def drawPixel(self, x:int, y:int, color):
        #print(x, y, color)
        self.draw.point((int(x), int(y)), fill = color)


    def showPicture(self):
        self.image.show()


    def save(self):
        now = datetime.now()
        filename = "picture_" + now.strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"
        path = "output\\" + filename
        print(filename)
        self.image.save(path)
