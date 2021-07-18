m = 50
test_sprite = PImage()
def setup():
    size(1920, 1080)
    #noCursor()
    test_sprite = loadImage("ch.png")
    
def draw():
    global m, test_sprite
    #background(250, 100, 100)
    #image(test_sprite, mouseX, mouseY)
    ellipse(m, 2*m, 50, 50)
    m += 1
    
