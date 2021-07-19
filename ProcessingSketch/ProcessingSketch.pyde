x = 50
y = 50
spdx = 0
spdy = 0
sketch = None
background_music = None
scrW = 1920
scrH = 1080
ellW = 50
ellH = 50
slowing = 0.7


# def gen_collider(x1, y1, x2, y2):
#   wer = []
#    for x in range(x1, x2 + 1):
#         for y in range(y1, y2 + 1):
#             answer.append(x, y)
#     return answer
def get_collider_positions(x1, y1, x2, y2):
    ans = []
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            ans.append([x, y])
    return ans

def setup():
    global sketch, scrW, scrH
    # scrW = width
    # scrH = height
    # fullScreen()
    size(1920, 1080)
    #setTitle("Nikita")
    #noCursor()
    
    sketch = loadImage("sketch.png")
    frameRate(60)
    

def draw():
    print("X: {}, y: {}".format(x, y))
    global x, y, test_sprite, spd, sketch, ellW, ellH, scrW, scrH, slowing, spdx, spdy
    #background(250, 100, 100)
    image(sketch, 0, 0, scrW, scrH)
    # image(test_sprite, mouseX, mouseY, 60, 40)
    
    spdx *= slowing
    spdy *= slowing
    
    if keyPressed:
        if keyCode == RIGHT:
            spdx += 0.5
        elif keyCode == LEFT:
            spdx -= 0.5
        elif keyCode == UP:
            spdy -= 0.5
        elif keyCode == DOWN:
            spdy += 0.5

    x += spdx
    y += spdy
    
    if  x >= scrW - ellW/2:
        x = scrW - ellW/2
    if y >= scrH - ellH/2:
        y = scrH - ellH/2
    if y <= ellH/2:
        y =  ellH/2
    if x <= ellW/2:
        x =  ellW/2
        
    col1 = get_collider_positions(261, 50, 331, 311)
    for xx, yy in col1:
        if x == xx:
            x -= (x - col1[0][0]) 
        if y == yy:
            x -= (x - col1[0][0]) 
    
    ellipse(x, y, ellW, ellH)
