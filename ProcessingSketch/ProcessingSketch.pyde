"""

GC presents
............
DASH IN TIME
............


"""

x = 200
y = 420
spdx = 0
spdy = 0
spdxbox = 0
spdybox = 0
sketch = None
h_nh = None
h_nh_left = None
h_hh = None
h_hh_left = None
h_nv = None
h_nv_left = None
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
xbox = 1013
ybox = 603
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
collised = 0
pressed = False
JumpingForCol = False
bsylen = 0.75
col_points_p = []
studying = False
st_f = True
st_ind = 0
helmet = False
visor = False
xe = 1720
ye = 200
we = 400
he = 400
wp = 20
hp = 20
patrons = []
h_hh_a = []
h_hh_l_a = []
h_nv_a = []
h_nv_l_a =[]
present = True
lvl = None
upstairs = True
door = None
door_a = [] 
maindoorsp = None
doorsp = None
centerX = 1920 / 2




def base_ai():
    global x, y, xe, ye, we, he, wp, hp, patrons
    direction = 0
    if x < xe:
         direction = -0.2
    else:
        direction = 0.2
    patrons.append([float(xe), float(ye), float(direction)])
    del direction
    


def pats():
    global patrons, wp, hp
    pats = [patrons[-1]] 
    for patron in pats:
        patron[0] += patron[2]
        ellipse(patron[0], patron[1], wp, hp)
    patrons = []


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
    
    global st_ind, studying
    if studying and (key == 'c' or key == 'C'):
        if st_ind == 3: # Here must be maximum
            st_ind = 0
            studying = False
        st_ind+=1
    
    global wr, wl
    if keyCode == RIGHT:
        #spdx += 0.5
        wr = True
    elif keyCode == LEFT:
        wl = True
    
    global helmet, visor
    if key == 'h' or key == 'H':
        helmet = not helmet
        if not helmet:
            visor = False
        else:
            visor = True
    if helmet and (key == 'v' or key == 'V'):
        visor = not visor
        
    global present
    if keyCode == 9:
        present = not present
    
    
    global upstairs, spdy
    if (451 < x < 506) and not upstairs and key == ' ':
        spdy -= 8.2


    


def keyTyped():
    global wr, wl, pressed
    if keyCode == RIGHT and (not pressed):
        #spdx += 0.5
        pressed = True
        wr = True
    elif keyCode == LEFT and (not pressed):
        pressed = True
        wl = True

def keyReleased():
    global wr, wl, pressed, box1, press
    if keyCode == RIGHT:
        wr = False
        pressed = False
    elif keyCode == LEFT :
        wl = False
        pressed = False
    
    
    press = False

lvl_f = None

def setup():
    global sketch, scrW, scrH, h_nh, h_hh, h_nv, sprite, box_, h_nh_left, walking_r, walking_l, main, mainsprite, jumping_r, jumping_l, box1, st, st_next, h_hh_a, h_nv_a, h_hh_l_a, h_nv_l_a, h_hh_left, h_nv_left, door_a, door
    size(1920, scrH)
    frameRate(300)
    
    sketch = loadImage("bg.png")
    h_nh = loadImage("h_nh.png")
    h_nh_left = loadImage("h_nh_left.png")
    h_nv = loadImage("h_nv.png")
    h_nv_left = loadImage("h_nv_left.png")
    h_hh = loadImage("h_hh.png")
    h_hh_left = loadImage("h_hh_left.png")
    box_ = loadImage("kub.png")
    mainsprite = h_nh
    walking_r = [loadImage("w1.png")] * 10 + [loadImage("w2.png")] * 10 + [loadImage("w3.png")] * 10 + [loadImage("w4.png")] * 10 + [loadImage("w5.png")] * 10 + [loadImage("w6.png")] * 10
    walking_l = [loadImage("w1l.png")] * 10 + [loadImage("w2l.png")] * 10 + [loadImage("w3l.png")] * 10 + [loadImage("w4l.png")] * 10 + [loadImage("w5l.png")] * 10 + [loadImage("w6l.png")] * 10
    h_hh_a = [loadImage("Helmet1.png")] * 10 + [loadImage("Helmet2.png")] * 10 + [loadImage("Helmet3.png")] * 10 + [loadImage("Helmet4.png")] * 10 + [loadImage("Helmet5.png")] * 10 + [loadImage("Helmet6.png")] * 10
    h_hh_l_a = [loadImage("Helmet1_l.png")] * 10 + [loadImage("Helmet2_l.png")] * 10 + [loadImage("Helmet3_l.png")] * 10 + [loadImage("Helmet4_l.png")] * 10 + [loadImage("Helmet5_l.png")] * 10 + [loadImage("Helmet6_l.png")] * 10
    h_nv_a = [loadImage("nv1.png")] * 10 + [loadImage("nv2.png")] * 10 + [loadImage("nv3.png")] * 10 + [loadImage("nv4.png")] * 10 + [loadImage("nv5.png")] * 10 + [loadImage("nv6.png")] * 10
    h_nv_l_a = [loadImage("No_visor1_l.png")] * 10 + [loadImage("No_visor2_l.png")] * 10 + [loadImage("No_visor3_l.png")] * 10 + [loadImage("No_visor4_l.png")] * 10 + [loadImage("No_visor5_l.png")] * 10 + [loadImage("No_visor6_l.png")] * 10
    jumping_r = loadImage("jump_nh.png")
    jumping_l = loadImage("jump_nh_l.png")
    st = [loadImage("start_placeholder.png"), loadImage("helmet_placeholder.png"), loadImage("visor_placeholder.png"), loadImage("box_placeholder.png")]
    st_next = loadImage("next_placeholder.png")
    #box1 = Box(xbox, ybox, "box.png", bsx, bsy)
    global lvl
    lvl = loadImage("lvl1.png")
    door = loadImage("door.png")
    door_a = [loadImage("door1.png")] * 10 + [loadImage("door2.png")] * 10 + [loadImage("door3.png")] * 10 + [loadImage("door4.png")] * 10
    global door_sprite
    door_sprite = door
    
    global lvl_f
    lvl_f = loadImage("lvl1_future.png")

def draw():
    if present:
        draw_present()
    else:
        draw_future()


door_ind = 0
start = True
door_sprite = None

def draw_present():
    global x, y, test_sprite, spd, sketch, ellW, ellH, scrW, scrH, helmet, visor, slowing, h_nv_a, h_nv_l_a, st_next, st_ind, st_f, studying, spdx, spdy, prevX, prevY, h_nh, h_nv, xe, ye, h_hh, h_nh_left, box_, isJumping, spdxbox, spdybox, xbox, ybox, distX, distY, isInteractWithPlayer, sprite, walking_r, walking_l, ind, press, st, st_next, right, mainsprite, bsx, bsy, sx, wr, wl, collised, JumpingForCol, bsylen, box1, col_points_p
    global lvl
    spdx *= slowing
    #spdy *= slowing
    if isInteractWithPlayer:
        xbox = x + distX
        ybox = y + distY
    else:
        if (ybox + bsy / 2) < 532:  
            spdybox += 0.2
        elif (ybox + bsy / 2) >= 532:
            spdybox = 0
            ybox = 532 - bsy / 2
        
         
    global upstairs
    if not (451 < x < 506) and upstairs: # and upstairs: #тут должны быть корды зоны, в которой чекл падает, например not (276 < x < 330):
        if (y + ellH / 2) < 486:   
            spdy += 0.4
        if (y + ellH / 2) >= 486:
            spdy = 0
            y = 486 - ellH / 2
            isJumping = False
            if st_f:
                st_f = False
                studying = True
    else:
        if (y + ellH / 2) < 666:   
            spdy += 0.4
        if (y + ellH / 2) >= 666:
            spdy = 0
            y = 666 - ellH / 2
            isJumping = False
            if st_f:
                st_f = False
                studying = True
    
    if y >= 600 and (451 < x < 506):
        upstairs = False
    # elif not upstairs:
    #     if (y + ellH / 2) < 666:   
    #         spdy += 0.2
    #     if (y + ellH / 2) >= 666:
    #         spdy = 0
    #         y = 666 - ellH / 2
    #         isJumping = False
    #         if st_f:
    #             st_f = False
    #             studying = True
    # elif not isJumping:
    #     upstairs = False
    #     if (y + ellH / 2) < 666:   
    #         spdy += 0.2
    #     if (y + ellH / 2) >= 666:
    #         spdy = 0
    #         y = 666 - ellH / 2
    #         isJumping = False
    #         if st_f:
    #             st_f = False
    #             studying = True

    
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
    
    global h_nv_left, h_hh_left
    
    if helmet:
            if visor:
                if right:
                    mainsprite = h_hh
                else:
                    mainsprite = h_hh_left
            else:
                if right:
                    mainsprite = h_nv
                else:
                    mainsprite = h_nv_left
    else:
        if right:
            mainsprite = h_nh
        else:
            mainsprite = h_nh_left
    sprite = mainsprite
    
    global h_hh_a, h_hh_l_a
    
    if (not helmet) and (not visor):
        if press:
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
    elif helmet and (not visor):
        if press:
            if right:
                sprite = h_nv_a[ind]
                ind += 1
                if ind >= 59:
                    ind -= 59
            else:
                ind += 1
                if ind >= 59:
                    ind -= 59
                sprite = h_nv_l_a[ind]
        if isJumping:
            if right:
                sprite = jumping_r
            else:
                sprite = jumping_l
    elif helmet and visor:
        if press:
            if right:
                sprite = h_hh_a[ind]
                ind += 1
                if ind >= 59:
                    ind -= 59
            else:
                ind += 1
                if ind >= 59:
                    ind -= 59
                sprite = h_hh_l_a[ind]
        if isJumping:
            if right:
                sprite = jumping_r
            else:
                sprite = jumping_l
    
    
    
    
    if keyPressed:
        if  (key == ' ' and keyCode == 0) and (not isJumping):
            spdy += -6.2
            isJumping = True    
    
    col_points_p = [[x - ellW / 2, y - ellH / 2], [x + ellW / 2, y - ellH / 2], [x - ellW / 2, y + ellH / 2], [x + ellW / 2, y + ellH / 2]]
    col_points_b = [[xbox - bsx / 2, ybox - bsy], [xbox + bsx / 2, ybox - bsy], [xbox - bsx / 2, ybox + bsy], [xbox + bsx / 2, ybox + bsy]]
    if (not isInteractWithPlayer) and (upstairs):
        if (col_points_p[1][0] > col_points_b[0][0]) and (col_points_p[0][0] < col_points_b[1][0]):
                if (col_points_p[3][1] > col_points_b[0][1] - bsylen * bsy):
                    spdy = 0
                    if (isJumping):
                        if 0 <= collised < 3:
                            JumpingForCol = True
                        collised = 3
                        isJumping = False
                    elif (not right and collised == 1) or (right and collised == 2):
                        collised = 0
                    elif right and (collised == 0 or collised == 1):
                        x -= abs(col_points_b[0][0] - col_points_p[1][0])
                        collised = 1
                    elif not right and (collised == 0 or collised == 2):
                        x += abs(col_points_b[1][0] - col_points_p[0][0])
                        collised = 2
                    elif collised == 3:
                        if JumpingForCol:
                            spdy = 0
                    if y > col_points_b[0][1] - bsylen * bsy:
                        spdy = 0
                        y = col_points_b[0][1] - bsylen * bsy
                        isJumping = False
                    if keyPressed:
                        if  (key == ' ' and keyCode == 0) and (not isJumping):
                            spdy += -6.2
                            isJumping = True
                        else:
                            press = False
        else:
            collised = 0
    
    #753!!
    
    if upstairs and x >= 860:
        x = 859.9
    
    if not upstairs and 753 <= x <= 904:
        x = 752.9
    
    if y <= 575 and ((not upstairs) and (not 451 < x < 506)):
        y = 574.9 
        spdy += 0.2
    
    if y <= 360:
        upstairs = True
        y = 359.9
        spdy = 3
    
    if not start and 418 >= x and upstairs:
        x = 418.1
    
    if x >= 418 and start:
        start = False
    
    if x <= 24:
        x = 24.1
    
    
    global door, door_a, door_sprite, door_ind, start
    if upstairs:
        if 320 <= x <= 410:
            if door_ind >= 39:
                door_ind = 39
            door_sprite = door_a[door_ind]
            door_ind += 1
        else:
            if door_ind >= 39:
                door_ind = 39
            if door_ind <= 0:
                door_ind = 0
            door_sprite = door_a[door_ind]
            door_ind -= 1
    x += spdx
    y += spdy
    print(str(upstairs))
    sx += -spdx
    
    ybox += spdybox

    st_coords = [x + 100, y - 100]

    image(sketch, 0, 0)
    image(lvl, 0, 0)
    image(door_sprite, 390, 417)
    image(box_, xbox, ybox, bsx, bsy)
    image(sprite, x, y, ellW, ellH)
    ellipse(xe, ye, 100, 100)
    base_ai()
    pats()
    
    
    if studying:
        image(st[st_ind], st_coords[0], st_coords[1])
        image(st_next, st_coords[0], st_coords[1] + 75)
    prevX = round(x)
    
    println(str(x) + ' ' + str(y))
    # print(ind)
    


ind_scr = 0
def draw_future():
    global x, y, test_sprite, spd, sketch, ellW, ellH, scrW, scrH, helmet, visor, slowing, h_nv_a, h_nv_l_a, st_next, st_ind, st_f, studying, spdx, spdy, prevX, prevY, h_nh, h_nv, xe, ye, h_hh, h_nh_left, box_, isJumping, spdxbox, spdybox, xbox, ybox, distX, distY, isInteractWithPlayer, sprite, walking_r, walking_l, ind, press, st, st_next, right, mainsprite, bsx, bsy, sx, wr, wl, collised, JumpingForCol, bsylen, box1, col_points_p
    global lvl
    spdx *= slowing
        
    global upstairs
    #spdy *= slowing
    if isInteractWithPlayer:
        xbox = x + distX
        ybox = y + distY
    else:
        if (ybox + bsy / 2) < 710:  
            spdybox += 0.2
        elif (ybox + bsy / 2) >= 710:
            spdybox = 0
            ybox = 710 - bsy / 2
        
         

    if not (451 < x < 506) and upstairs: # and upstairs: #тут должны быть корды зоны, в которой чекл падает, например not (276 < x < 330):
        if (y + ellH / 2) < 486:   
            spdy += 0.4
        if (y + ellH / 2) >= 486:
            spdy = 0
            y = 486 - ellH / 2
            isJumping = False
            if st_f:
                st_f = False
                studying = True
    else:
        if (y + ellH / 2) < 666:   
            spdy += 0.4
        if (y + ellH / 2) >= 666:
            spdy = 0
            y = 666 - ellH / 2
            isJumping = False
            if st_f:
                st_f = False
                studying = True
    
    if y >= 600 and (451 < x < 506):
        upstairs = False
    # elif not upstairs:
    #     if (y + ellH / 2) < 666:   
    #         spdy += 0.2
    #     if (y + ellH / 2) >= 666:
    #         spdy = 0
    #         y = 666 - ellH / 2
    #         isJumping = False
    #         if st_f:
    #             st_f = False
    #             studying = True
    # elif not isJumping:
    #     upstairs = False
    #     if (y + ellH / 2) < 666:   
    #         spdy += 0.2
    #     if (y + ellH / 2) >= 666:
    #         spdy = 0
    #         y = 666 - ellH / 2
    #         isJumping = False
    #         if st_f:
    #             st_f = False
    #             studying = True

    
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
    
    global h_nv_left, h_hh_left
    
    if helmet:
            if visor:
                if right:
                    mainsprite = h_hh
                else:
                    mainsprite = h_hh_left
            else:
                if right:
                    mainsprite = h_nv
                else:
                    mainsprite = h_nv_left
    else:
        if right:
            mainsprite = h_nh
        else:
            mainsprite = h_nh_left
    sprite = mainsprite
    
    global h_hh_a, h_hh_l_a
    
    if (not helmet) and (not visor):
        if press:
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
    elif helmet and (not visor):
        if press:
            if right:
                sprite = h_nv_a[ind]
                ind += 1
                if ind >= 59:
                    ind -= 59
            else:
                ind += 1
                if ind >= 59:
                    ind -= 59
                sprite = h_nv_l_a[ind]
        if isJumping:
            if right:
                sprite = jumping_r
            else:
                sprite = jumping_l
    elif helmet and visor:
        if press:
            if right:
                sprite = h_hh_a[ind]
                ind += 1
                if ind >= 59:
                    ind -= 59
            else:
                ind += 1
                if ind >= 59:
                    ind -= 59
                sprite = h_hh_l_a[ind]
        if isJumping:
            if right:
                sprite = jumping_r
            else:
                sprite = jumping_l
    
    
    
    
    if keyPressed:
        if  (key == ' ' and keyCode == 0) and (not isJumping):
            spdy += -6.2
            isJumping = True 
     
    
    
    col_points_p = [[x - ellW / 2, y - ellH / 2], [x + ellW / 2, y - ellH / 2], [x - ellW / 2, y + ellH / 2], [x + ellW / 2, y + ellH / 2]]
    col_points_b = [[xbox - bsx / 2, ybox - bsy], [xbox + bsx / 2, ybox - bsy], [xbox - bsx / 2, ybox + bsy], [xbox + bsx / 2, ybox + bsy]]
    if (not isInteractWithPlayer):
        if (col_points_p[1][0] > col_points_b[0][0]) and (col_points_p[0][0] < col_points_b[1][0]):
                if (col_points_p[3][1] > col_points_b[0][1] - bsylen * bsy):
                    spdy = 0
                    if (isJumping):
                        if 0 <= collised < 3:
                            JumpingForCol = True
                        collised = 3
                        isJumping = False
                    elif (not right and collised == 1) or (right and collised == 2):
                        collised = 0
                    elif right and (collised == 0 or collised == 1):
                        x -= abs(col_points_b[0][0] - col_points_p[1][0])
                        collised = 1
                    elif not right and (collised == 0 or collised == 2):
                        x += abs(col_points_b[1][0] - col_points_p[0][0])
                        collised = 2
                    elif collised == 3:
                        if JumpingForCol:
                            spdy = 0
                    if y > col_points_b[0][1] - bsylen * bsy:
                        spdy = 0
                        y = col_points_b[0][1] - bsylen * bsy
                        isJumping = False
                    if keyPressed:
                        if  (key == ' ' and keyCode == 0) and (not isJumping):
                            spdy += -6.2
                            isJumping = True
                        else:
                            press = False
        else:
            collised = 0
    
    #753!!
    
    if upstairs and x >= 860:
        x = 859.9
    
    if y <= 560 and ((not upstairs) and (not 451 < x < 506)) and x <= 937:
        y = 559.9 
        spdy += 0.2
        
    if y <= 360 and not upstairs and (451 < x < 506):
        upstairs = True
        y = 359.9
        spdy = 3
    elif y <= 360 and not upstairs and (not 451 < x < 506):
        y = 360.1
    
    if not start and 418 >= x and upstairs:
        x = 418.1
    
    if x >= 418 and start:
        start = False
    
    if x <= 24:
        x = 24.1
    
    global centerX, ind_scr
    if x >= centerX:
        if ind_scr >= centerX:
            ind_scr = centerX
        translate(-ind_scr, 0)
        if wr:
            ind_scr += 1
    elif x < centerX + 500:
        if ind_scr >= centerX:
            ind_scr = centerX
        if ind_scr <= 0:
            ind_scr = 0
        translate(-ind_scr, 0)
        if wl:
            ind_scr -= 1
    
    global door, door_a, door_sprite, door_ind, start
    if upstairs:
        if 320 <= x <= 410:
            if door_ind >= 39:
                door_ind = 39
            door_sprite = door_a[door_ind]
            door_ind += 1
        else:
            if door_ind >= 39:
                door_ind = 39
            if door_ind <= 0:
                door_ind = 0
            door_sprite = door_a[door_ind]
            door_ind -= 1
    x += spdx
    y += spdy
    print(str(upstairs))
    sx += -spdx
    
    ybox += spdybox

    st_coords = [x + 100, y - 100]

    global lvl_f

    image(sketch, 0, 0)
    image(lvl_f, 0, 0)
    image(door_sprite, 390, 417)
    image(box_, xbox, ybox, bsx, bsy)
    image(sprite, x, y, ellW, ellH)
    
    
    if studying:
        image(st[st_ind], st_coords[0], st_coords[1])
        image(st_next, st_coords[0], st_coords[1] + 75)
    prevX = round(x)
    
    println(str(x) + ' ' + str(y))
    # print(ind)

    
