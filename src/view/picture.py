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
        color = (int(color[0]), int(color[1]), int(color[2]))
        self.draw.point((int(x), int(y)), fill = color)

    def showPicture(self):
        self.image.show()

    def save(self):
        self.image.save("picture.jpg")
