x = 50
y = 50
spd = 1
sketch = None
scrW = 1920
scrH = 1080
ellW = 50
ellH = 50

def setup():
    global sketch
    size(1920, 1080)
    #setTitle("Nikita")
    #noCursor()
    
    sketch = loadImage("sketch.png")
    frameRate(60)
    
def draw():
    global x, y, test_sprite, spd, sketch, ellW, ellH, scrW, scrH
    #background(250, 100, 100)
    image(sketch, 0, 0, scrW, scrH)
    # image(test_sprite, mouseX, mouseY, 60, 40)
    if  x >= scrW - ellW/2:
        x = scrW - ellW/2
    if y >= scrH - ellH/2:
        y = scrH - ellH/2
    if y <= ellH/2:
        y =  ellH/2
    if x <= ellW/2:
        x =  ellW/2
    ellipse(x, y, ellW, ellH)
    
    if keyPressed:
        if keyCode == RIGHT:
            x += spd
        elif keyCode == LEFT:
            x -= spd
        elif keyCode == UP:
            y += spd
        elif keyCode == DOWN:
            y -= spd
    

     
