import tkinter
import math
import json
from PIL import ImageGrab

window = tkinter.Tk()
window.geometry('600x350')
window.title('Simple Stellar System')

showBoard = tkinter.Canvas(window, width=600, height=350, background='black')
showBoard.pack()

x0, y0 = 300, 175
ang = -75 / 180 * math.pi
rad = [70]
xRad = 2
yRad = 3

preSin = math.sin(ang)
preCos = math.cos(ang)
preDSin = math.sin(2 * ang)
preDCos = math.cos(2 * ang)
dXRad = xRad ** 2
dYRad = yRad ** 2
sX = math.sqrt(((dXRad-dYRad)*preDCos+dXRad+dYRad)/2)


def save():
    global window, showBoard

    x = window.winfo_rootx()+showBoard.winfo_x()
    y = window.winfo_rooty()+showBoard.winfo_y()
    ImageGrab.grab().crop((x, y, x+600, y+350)).save("saves.gif")


showBoard.create_oval(x0-50, y0-50, x0+50, y0+50, fill="orange")
for star in range(0, 1):
    nowX = sX
    nowY = (math.sqrt(2) / xRad / yRad * math.sqrt(dXRad * (1 + preDCos) + dYRad * (1 - preDCos) - 2 * nowX * nowX) + 2 * nowX *
            preSin * preCos * ((dYRad - dXRad) / dXRad / dYRad)) / (2 * (preSin * preSin / dXRad + preCos * preCos / dYRad))

    for i in range(10000, -10000, -1):
        lastX = json.loads(json.dumps(nowX))
        lastY = json.loads(json.dumps(nowY))
        nowX = sX * i / 10000
        if i >= 9997:
            print(nowX, dXRad * (1 + preDCos) + dYRad *
                  (1 - preDCos) - 2 * nowX * nowX)
        nowY = (math.sqrt(2) / xRad / yRad * math.sqrt(dXRad * (1 + preDCos) + dYRad * (1 - preDCos) - 2 * nowX * nowX) + 2 * nowX *
                preSin * preCos * ((dYRad - dXRad) / dXRad / dYRad)) / (2 * (preSin * preSin / dXRad + preCos * preCos / dYRad))

        showBoard.create_line(x0 + (lastX * rad[star]), y0 + (
            lastY * rad[star]), x0 + (nowX * rad[star]), y0 + (nowY * rad[star]), fill="white")

    for i in range(-10000, 10000, 1):
        lastX = json.loads(json.dumps(nowX))
        lastY = json.loads(json.dumps(nowY))
        nowX = sX * i / 10000
        nowY = (-1 * math.sqrt(2) / xRad / yRad * math.sqrt(dXRad * (1 + preDCos) + dYRad * (1 - preDCos) - 2 * nowX * nowX) + 2 * nowX *
                preSin * preCos * ((dYRad - dXRad) / dXRad / dYRad)) / (2 * (preSin * preSin / dXRad + preCos * preCos / dYRad))

        showBoard.create_line(x0 + (lastX * rad[star]), y0 + (
            lastY * rad[star]), x0 + (nowX * rad[star]), y0 + (nowY * rad[star]), fill="white")


def move(event):
    global showBoard, x0, y0, ang, rad, xRad, yRad, preSin, preCos, preDSin, preDCos, dXRad, dYRad, sX
    save()
    img = tkinter.PhotoImage(file="saves.gif")
    way = -1
    i = 500

    nowX = sX
    nowY = (math.sqrt(2) / xRad / yRad * math.sqrt(dXRad * (1 + preDCos) + dYRad * (1 - preDCos) - 2 * nowX * nowX) + 2 * nowX *
            preSin * preCos * ((dYRad - dXRad) / dXRad / dYRad)) / (2 * (preSin * preSin / dXRad + preCos * preCos / dYRad))
    while(True):
        #showBoard.create_image(x0, y0, image=img)
        for star in range(0, 1):
            lastX = json.loads(json.dumps(nowX))
            lastY = json.loads(json.dumps(nowY))
            nowX = sX * (i / 500)
            nowY = (-1 * way * math.sqrt(2) / xRad / yRad * math.sqrt(dXRad * (1 + preDCos) + dYRad * (1 - preDCos) - 2 * nowX * nowX) + 2 * nowX *
                    preSin * preCos * ((dYRad - dXRad) / dXRad / dYRad)) / (2 * (preSin * preSin / dXRad + preCos * preCos / dYRad))

            showBoard.create_oval(x0 + (nowX * rad[star]) + 10, y0 + (
                nowY * rad[star]) + 10, x0 + (nowX * rad[star]) - 10, y0 + (nowY * rad[star]) - 10, fill="skyblue")

            showBoard.update()

        i += way
        if(i < -500):
            way = 1
        if(i > 500):
            way = -1


window.bind("`", move)

tkinter.mainloop()
