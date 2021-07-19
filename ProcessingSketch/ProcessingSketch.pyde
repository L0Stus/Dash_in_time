x = 200
y = 200
spdx = 0
spdy = 0
sketch = None
h_nh = None
h_hh = None
h_nv = None
background_music = None
scrW = 1920
scrH = 1080
ellW = 75
ellH = 130
slowing = 0.7
prevX = 50
prevY = 50
isJumping = False


def setup():
    global sketch, scrW, scrH, h_nh
    # scrW = width
    # scrH = height
    # fullScreen()
    size(1920, 1080)
    frameRate(140)
    #setTitle("Nikita")
    #noCursor()
    
    sketch = loadImage("sketch.png")
    h_nh = loadImage("h_nh.png")
    # h_nv = loadImage("h_nv.png")
    # h_hh = loadImage("h_hh.png")
    

def draw():
    #print("X: {}, y: {}".format(x, y))
    global x, y, test_sprite, spd, sketch, ellW, ellH, scrW, scrH, slowing, spdx, spdy, prevX, prevY, h_nh, isJumping
    #background(250, 100, 100)
    image(sketch, 0, 0, scrW, scrH)
    # image(test_sprite, mouseX, mouseY, 60, 40)
    
    spdx *= slowing
    #spdy *= slowing

    if y < 355:  
        spdy += 3
        spdy * 3
    elif y >= 355:
        spdy = 0
        y = 355
        isJumping = False
    
    if keyPressed:
        if keyCode == RIGHT:
            spdx += 3
        elif keyCode == LEFT:
            spdx -= 3
        # elif keyCode == UP:
        #     spdy -= 0.5
        # elif keyCode == DOWN:
        #     spdy += 0.5
        elif keyCode == UP and (not isJumping):
            spdy += -15.2
            isJumping = True

    x += spdx
    y += spdy

    
    # if  x >= scrW - ellW/2:
    #     x = scrW - ellW/2
    # if y >= scrH - ellH/2:
    #     y = scrH - ellH/2
    # if y <= ellH/2:
    #     y =  ellH/2
    # if x <= ellW/2:
    #     x =  ellW/2
    
        
    # col1 = get_collider_positions(261, 50, 331, 311)
    # for xx, yy in col1:
    #     if x == xx:
    #         x -= (x - col1[0][0]) 
    #     if y == yy:
    #         x -= (x - col1[0][0]) 69 407
    
    
    # if (0 <= y <= 311) and (263 <= x <= 349):
    #     x = prevX
    #     y = prevY
        
    
    image(h_nh, x, y, ellW, ellH)
    prevX = round(x)
    prevY = round(y)
