from time import *
from pygame import *

#creating classes
class Card(sprite.Sprite): #creating class for cards (sprite.Sprite - class from Pygame)
    def __init__(self, x, y, width, height, colour_): #class constructor
        super().__init__() #inheriting properties from superclass
        self.rect = Rect(x, y, width, height)
        self.colour = colour_ #card's colour property
    def draw(self):
        draw.rect(window, self.colour, self.rect)

class Picture(sprite.Sprite): #creating class for pictures (sprite.Sprite - class from Pygame)
    def __init__(self, x, y, width, height, image_, speed): #class constructor
        super().__init__() #inheriting properties from superclass
        #an image property for Picture
        self.image = transform.scale(image.load(image_), (width, height))
        self.x = x
        self.y = y
        self.speed = speed
        #rectangle, where the image contains
        self.rect = self.image.get_rect()
    def reset(self): #reseting an image with new image, width or length
        window.blit(self.image, (self.x, self.y))
    def update_arrows(self): #characters' movements
        keys = key.get_pressed() #get pressed keys, write them inside the variable
        #changes chars position depending on pressed arrows
        if keys[K_LEFT] and self.x > 0:
            self.x -= self.speed
        elif keys[K_RIGHT] and self.x < window_size[1] + 100:
            self.x += self.speed
        elif keys[K_UP] and self.y > 20:
            self.y -= self.speed
        elif keys[K_DOWN] and self.y < window_size[0] - 323:
            self.y += self.speed
    def update_letters(self): #characters' movements
        keys = key.get_pressed() #get pressed keys written inside the variable
        #changes chars position depending on pressed letters
        if keys[K_a] and self.x > 0:
            self.x -= self.speed
        elif keys[K_d] and self.x < window_size[1] + 100:
            self.x += self.speed
        elif keys[K_w] and self.y > 20:
            self.y -= self.speed
        elif keys[K_s] and self.y < window_size[0] - 305:
            self.y += self.speed

#creating a window
window_size = (700, 500)
display.set_caption('Random game') #window's name
window = display.set_mode(window_size) #setting a window
background = transform.scale(image.load('backdora.jpg'), window_size) #setting a background
FPS = 90
colour1 = (133, 65, 231)
colour2 = (231, 65, 129)
#creating sprites (objects) using previously created classes
square1 = Card(100, 100, 200, 100, colour1)
square2 = Card(400, 100, 400, 200, colour2)
dora = Picture(100, 100, 100, 70, 'dora.png', 32)
finn = Picture(300, 100, 100, 100, 'FINNTHEHUMAN.png', 31)
clocks = time.Clock()

#game itself
play = True
while play:
    #time.delay(10) #50 msec delay
    window.blit(background, (0,0))

    square1.draw() #char's drawing
    square2.draw()

    dora.reset() #chars' reset
    finn.reset()

    dora.update_letters() #chars' movements
    finn.update_arrows()

    for e in event.get():
        if e.type == QUIT:
            play = False
    
    display.update()
    clocks.tick(FPS)