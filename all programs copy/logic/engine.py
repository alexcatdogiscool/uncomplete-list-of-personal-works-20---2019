import math
import gates
import objs
import pygame as pg


width, height = 800,800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
sky = (69,69,69)
gatecol = (75, 214, 145)

screen = pg.display.set_mode((width,height))
screen.fill(sky)
pg.display.flip()
pg.font.init()
arial = pg.font.SysFont('Arial', 30)
arialsmall = pg.font.SysFont('Arial', 30)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 38)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    return (self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
newname = InputBox(0,0,200,35)

def dectobin(n, digits):
    b = "{0:0b}".format(n)
    for i in range(digits-len(b)):
        b = '0' + b
    return b

def pythag(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def drawgates(lst):
    for i in range(len(lst)):
        x,y = lst[i].x, lst[i].y
        txtsurf = arial.render(lst[i].name, True, (0,0,0))
        tw = (txtsurf.get_size())[0]
        rw = tw+20
        if lst[i].innum > lst[i].outnum:
            rh = 30*lst[i].innum
        else:
            rh = 30*lst[i].outnum
        lst[i].w = rw
        lst[i].h = rh
        for o in range(lst[i].innum):
            pg.draw.circle(screen, ((int(lst[i].instate[o])*255),0,0), (int(x), int((30*o)+y+15) ),15)
        for o in range(lst[i].outnum):
            pg.draw.circle(screen, ((int(lst[i].outstate[o])*255),0,0), (int(x+rw), int((30*o)+y+15) ),15)
        pg.draw.rect(screen, gatecol, (x, y, rw,rh))
        screen.blit(txtsurf,(x+10, y))

def drawwires(lst):
    for i in range(len(lst)):
        pg.draw.line(screen, (lst[i].state*255,0,0), (lst[i].sx, lst[i].sy), (lst[i].ex, lst[i].ey), 4)

def drawinouts(lst):
    for i in lst:
        pg.draw.circle(screen, (int(i.state*255),0,0), (int(i.x),int(i.y)), 15)



gatelst = []
wirelst = []
inouts = []

outputstates = []
statenum = 0
saving = False
wireing = False
running = True
frame = 0
while running:
    ###############################3
    keys = pg.key.get_pressed()
    add = keys[pg.K_EQUALS]
    minus = keys[pg.K_MINUS]
    addout = keys[pg.K_RIGHTBRACKET]
    minusout = keys[pg.K_LEFTBRACKET]
    mx,my = pg.mouse.get_pos()
    m1,m3,m2 = pg.mouse.get_pressed()

    if keys[pg.K_UP] == 1:
        s = ''
        for g in gatelst:
            s += g.name
            s += ','
        s += '.'
        for w in wirelst:
            s += str(int(w.slocked)) + ';' + str(int(w.elocked)) + ';' + str(int(w.inlocked)) + ';' + str(int(w.outlocked)) + ';' + str(w.iopin) + ';' + str(w.slog) + ';' + str(w.slop) + ';' + str(w.elog) + ';' + str(w.elop)
            s += ','
        s += '.'
        for ios in inouts:
            s += str(ios.mode) + ';' + str(ios.pinnum)
            s += ','
        f = open('test.txt','w')
        f.write(s)
        f.close()

    tmp = 0
    for g in gatelst:
        md = pythag(mx,my, g.x+g.w/2,g.y+g.h/2)
        if md < pythag(0,0, g.w/2,g.h/2) and m2 == 1:
            g.x = mx-(g.w/2)
            g.y = my-(g.h/2)

        for i in range(g.innum+g.outnum):
            if i < g.innum:
                x = g.x
                y = (30*i)+g.y+15
            else:
                x = g.x + g.w
                y = (30*(i-g.innum))+g.y+15

            mdtp = pythag(mx,my,x,y)
            if mdtp < 15 and m1 == True and m1p == False:
                o = objs.wire()
                o.slocked = True
                o.slog = tmp
                o.slop = i
                wirelst.append(o)
                wireing = True     
        tmp += 1
    
    if wireing == True and m1 == False:
        tmp = 0
        for g in gatelst:
            for i in range(g.innum+g.outnum):
                if i < g.innum:
                    x = g.x
                    y = (30*i)+g.y+15
                else:
                    x = g.x + g.w
                    y = (30*(i-g.innum))+g.y+15

                mdtp = pythag(mx,my,x,y)
                if mdtp < 15:
                    wirelst[-1].elocked = True
                    wirelst[-1].elog = tmp
                    wirelst[-1].elop = i
            tmp += 1
        
        for ios in inouts:
            if ios.mode == 1:
                d = pythag(mx,my, ios.x,ios.y)
                if d < 15:
                    wirelst[-1].outlocked = 1
                    wirelst[-1].iopin = ios.pinnum
        wireing = False

    if len(wirelst) != 0:
        if wireing == False and wirelst[-1].elocked == False and wirelst[-1].outlocked == False:
            if len(wirelst) > 0:
                del wirelst[-1]
            else:
                pass


    t = 0
    for ios in inouts:
        d = pythag(mx,my, ios.x,ios.y)
        if d < 15 and m1 == 1 and m1p == 0:
            #print(ios.mode)
            i = objs.wire()
            if ios.mode == 0:
                i.inlocked = 1
                i.iopin = ios.pinnum
                wirelst.append(i)
            wireing = True
        if d < 15 and m2 == 1 and m2p == 0:
            ios.state = 1-ios.state#int(((ios.state-0.5)*-1)+0.5)
        if saving == True:
            if ios.mode == 0:
                #print(inputstates[statenum])
                ios.state = int(inputstates[statenum][t])
                t += 1
            

    if wireing == True and wirelst[-1].elocked == False:
        wirelst[-1].ex = mx
        wirelst[-1].ey = my
    if wireing == True and wirelst[-1].outlocked == False:
        wirelst[-1].ex = mx
        wirelst[-1].ey = my

    

    for w in wirelst:
        w.lock(gatelst, inouts)
        w.updatestate(gatelst, inouts)
    for g in gatelst:
        g.logic()
        g.updatestate(wirelst,gatelst)


    drawwires(wirelst)
    drawgates(gatelst)
    drawinouts(inouts)
    ###### make inouts in middle
    ins = 0
    outs = 0
    for ios in inouts:
        if ios.mode == 0:
            ins += 1
        if ios.mode == 1:
            outs += 1
    yi = (height/2)-((30*ins)/2)
    yo = (height/2)-((30*outs)/2)
    ti = 0
    to = 0
    for ios in inouts:
        if ios.mode == 0:
            ios.y = (ti*30)+yi
            ti += 1
        if ios.mode == 1:
            ios.y = (to*30)+yo
            to += 1


    if add == 1 and addp == 0:
        i = objs.inout()
        i.pinnum = len(inouts)
        i.mode = 0
        i.x = 15
        yd = 0
        for ios in inouts:
            if ios.mode == 0:
                if ios.y > yd:
                    yd = ios.y
        i.y = yd+30
        inouts.append(i)
    
    if minus == 1 and minusp == 0:
        t = 0
        for ios in inouts:
            if ios.mode == 0:
                t = ios.pinnum
        tmp = 0
        for ios in inouts:
            if ios.pinnum == t:
                ww = 0
                for w in wirelst:
                    if w.inlocked == True:
                        if w.iopin == tmp:
                            del wirelst[ww]
                    ww += 1
                del inouts[tmp]
            tmp += 1
    


    if addout == 1 and addoutp == 0:
        i = objs.inout()
        i.pinnum = len(inouts)
        i.mode = 1
        i.x = 800-15
        yd = 0
        for ios in inouts:
            if ios.mode == 1:
                if ios.y > yd:
                    yd = ios.y
        i.y = yd+30
        inouts.append(i)
    
    if minusout == 1 and minusoutp == 0:
        t = 0
        for ios in inouts:
            if ios.mode == 1:
                t = ios.pinnum
        tmp = 0
        for ios in inouts:
            if ios.pinnum == t:
                ww = 0
                for w in wirelst:
                    if w.outlocked == True:
                        if w.iopin == tmp:
                            del wirelst[ww]
                    ww += 1
                del inouts[tmp]
            tmp += 1

    





    
    ####### gate selection
    f = open('newgates.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    names = []
    names.append('AND')
    names.append('NOT')
    for n in range(len(data)):
        names.append(data[n].split('.')[0])
    tw = 0
    w = 0
    for n in range(len(names)):
        txtsurf = arialsmall.render(names[n], True, (0,0,0))
        w += tw
        tw = txtsurf.get_size()[0]
        x,y = w+(n*10)+10, 760
        screen.blit(txtsurf, (x, y))
        d = pythag(mx,my, x+tw/2,y+20)
        if d < 25 and m2 == 1 and m2p == 0:
            i = objs.gate(names[n])
            i.x = mx
            i.y = my
            gatelst.append(i)

    
    ######### save new gate
    name = None
    for event in pg.event.get():
        name = (newname.handle_event(event))
    if name != None:
        s = ''
        s += name + '.'
        for g in gatelst:
            s += g.name
            s += ','
        s += '.'
        for w in wirelst:
            s += str(int(w.slocked)) + ';' + str(int(w.elocked)) + ';' + str(int(w.inlocked)) + ';' + str(int(w.outlocked)) + ';' + str(w.iopin) + ';' + str(w.slog) + ';' + str(w.slop) + ';' + str(w.elog) + ';' + str(w.elop)
            s += ','
        s += '.'
        for ios in inouts:
            s += str(ios.mode) + ';' + str(ios.pinnum)
            s += ','
        s += '\n'
        f = open('newgates.txt','a')
        f.write(s)
        f.close()
    newname.update()
    newname.draw(screen)



    addp = add
    minusp = minus
    addoutp = addout
    minusoutp = minusout
    m1p,m2p,m3p = m1,m2,m3
    frame += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    screen.fill(sky)