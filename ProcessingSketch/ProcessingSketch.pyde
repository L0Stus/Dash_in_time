x = 200
y = 200
spdx = 0
spdy = 0
spdxbox = 0
spdybox = 0
sketch = None
h_nh = None
h_nh_left = None
h_hh = None
h_nv = None
box_ = None
background_music = None
scrW = 3828
scrH = 1080
ellW = 51
ellH = 127
slowing = 0.7
prevX = 50
prevY = 50
isJumping = True
sprite = None 
xbox = 620
ybox = 100
isInteractWithPlayer = False
distX = 0
distY = 0
walking_r = []
walking_l = []
ind = 0
press = False
mainsprite = None
right = True
jumping_r = None
jumping_l = None
bsx = 37
bsy = 37
st_ind = 0
st = []
st_next = None
st_coords = []
sx = 0
wr = False
wl = False


def keyPressed():
    global isInteractWithPlayer, distX, distY, xbox, ybox, x, y, right
    if key == 'e' or key == 'E':
        distX = xbox - x
        distY = ybox - y
        println(distX)
        println(distY)
        if 0 < distX < 100 and right:
            isInteractWithPlayer = not isInteractWithPlayer
        elif -100 < distX < 0 and (not right):
            isInteractWithPlayer = not isInteractWithPlayer
        elif isInteractWithPlayer:
            isInteractWithPlayer = not isInteractWithPlayer
        println(isInteractWithPlayer)
    
    global wr, wl
    if keyCode == RIGHT:
        #spdx += 0.5
        wr = True
    elif keyCode == LEFT:
        wl = True


def keyTyped():
    global wr, wl
    if keyCode == RIGHT:
        #spdx += 0.5
        wr = True
    elif keyCode == LEFT:
        wl = True

def keyReleased():
    global wr, wl
    if keyCode == RIGHT:
        wr = False
    elif keyCode == LEFT:
        wl = False
    

def setup():
    global sketch, scrW, scrH, h_nh, sprite, box_, h_nh_left, walking_r, walking_l, main, mainsprite, jumping_r, jumping_l
    size(1920, scrH)
    frameRate(300)
    
    sketch = loadImage("bg.png")
    h_nh = loadImage("h_nh.png")
    h_nh_left = loadImage("h_nh_left.png")
    h_nv = loadImage("h_nv.png")
    h_hh = loadImage("h_hh.png")
    box_ = loadImage("kub.png")
    mainsprite = h_nh
    walking_r = [loadImage("w1.png")] * 10 + [loadImage("w2.png")] * 10 + [loadImage("w3.png")] * 10 + [loadImage("w4.png")] * 10 + [loadImage("w5.png")] * 10 + [loadImage("w6.png")] * 10
    walking_l = [loadImage("w1l.png")] * 10 + [loadImage("w2l.png")] * 10 + [loadImage("w3l.png")] * 10 + [loadImage("w4l.png")] * 10 + [loadImage("w5l.png")] * 10 + [loadImage("w6l.png")] * 10
    jumping_r = loadImage("jump_nh.png")
    jumping_l = loadImage("jump_nh_l.png")
    st = [loadImage("start_placeholder.png"), loadImage("box_placeholder.png")]
    st_next = loadImage("next_placeholder.png")


def draw():
    global x, y, test_sprite, spd, sketch, ellW, ellH, scrW, scrH, slowing, spdx, spdy, prevX, prevY, h_nh, h_nv, h_hh, h_nh_left, box_, isJumping, spdxbox, spdybox, xbox, ybox, distX, distY, isInteractWithPlayer, sprite, walking_r, walking_l, ind, press, right, mainsprite, bsx, bsy, sx, wr, wl
    
    
    spdx *= slowing
    #spdy *= slowing
    if isInteractWithPlayer:
        xbox = x + distX
        ybox = y + distY
    else:
        if (ybox) < 441:  
            spdybox += 3
            spdybox *= 3
        elif (ybox) >= 447:
            spdybox = 0
            ybox = 447
            
        
    if 1: #тут должны быть корды зоны, в которой чекл падает, например not (276 < x < 330):
        if (y + ellH / 2) < 412:   
            spdy += 0.2
        if (y + ellH / 2) >= 412:
            spdy = 0
            y = 355
            isJumping = False
    elif not isJumping:
        println("else!")
        spdy += 0.2
    
    if keyPressed:
        if  (keyCode == UP or (key == ' ' and keyCode == 0)) and (not isJumping):
            spdy += -6.2
            isJumping = True
    else:
        press = False
    
    if wr:
        spdx += 0.5
        mainsprite = h_nh
        press = True
        right = True
    elif wl:
        spdx -= 0.5
        mainsprite = h_nh_left
        press = True
        right = False
    
        
    
    
    sprite = mainsprite
    
    if press: #spdx > 0:
        if right:
            sprite = walking_r[ind]
            ind += 1
            if ind >= 59:
                ind -= 59
        else:
            sprite = walking_l[ind]
            ind += 1
            if ind >= 59:
                ind -= 59
    if isJumping:
        if right:
            sprite = jumping_r
        else:
            sprite = jumping_l
    col_points_p = [[x - ellW / 2, y - ellH / 2], [x + ellW / 2, y - ellH / 2], [x - ellW / 2, y + ellH / 2], [x + ellW / 2, y + ellH / 2]]
    col_points_b = [[xbox - bsx / 2, ybox - bsy], [xbox + bsx / 2, ybox - bsy], [xbox - bsx / 2, ybox + bsy], [xbox + bsx / 2, ybox + bsy]]
    if (col_points_p[1][0] > col_points_b[0][0]) and (col_points_p[0][0] < col_points_b[1][0]):
        if (col_points_p[3][1] > col_points_b[0][1]):
            if right:
                x -= abs(col_points_b[0][0] - col_points_p[1][0])
            elif not rights:
                x += abs(col_points_b[1][0] - col_points_p[0][0])

    x += spdx
    y += spdy
    
    sx += -spdx
    
    ybox += spdybox

    st_coords = [x + 300, y + 150]

    image(sketch, 0, 0)
    image(box_, xbox, ybox, bsx, bsy)
    image(sprite, x, y, ellW, ellH)
    prevX = round(x)
