from pathlib import Path
from PIL import Image, ImageDraw


class Picture:
    def __init__(self, x= 500, y= 300):
        self.x = x
        self.y = y
        self.image = Image.new('RGB', (x, y), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)


    def drawPixel(self, x:int, y:int, color = 0):
        #print(x, y, color)
        c1, c2, c3 = color
        color = (int(c1), int(c2), int(c3))
        self.draw.point((int(x), int(y)), fill = color)

    def showPicture(self):
        self.image.show()

    def save(self):
        self.image.save("picture.jpg")
