import tkinter
import math
import json

window = tkinter.Tk()
window.geometry('600x350')
window.title('Simple Stellar System')

showBoard = tkinter.Canvas(window, width=600, height=350, background='black')
showBoard.pack()

x0, y0 = 300, 175
ang = -75 / 180 * math.pi
rad = [120]
xRad = 1
yRad = 2

preSin = math.sin(ang)
preCos = math.cos(ang)
preDSin = math.sin(2 * ang)
preDCos = math.cos(2 * ang)
dXRad = xRad ** 2
dYRad = yRad ** 2
sX = math.sqrt(((dXRad-dYRad)*preDCos+dXRad+dYRad)/2)

firstTemp = math.sqrt(2) / xRad / yRad
secondTemp = dXRad * (1 + preDCos) + dYRad * (1 - preDCos)
thirdTemp = 2 * preSin * preCos * ((dYRad - dXRad) / dXRad / dYRad)
fourthTemp = 2 * (preSin * preSin / dXRad + preCos * preCos / dYRad)

showBoard.create_oval(x0-50, y0-50, x0+50, y0+50, fill="orange")
for star in range(0, 1):
    nowX = sX
    nowY = (firstTemp * math.sqrt(secondTemp - 2 *
                                  nowX * nowX) + nowX * thirdTemp) / fourthTemp

    for i in range(10000, -10000, -1):
        lastX = json.loads(json.dumps(nowX))
        lastY = json.loads(json.dumps(nowY))
        nowX = sX * (i / 10000)
        nowY = (firstTemp * math.sqrt(secondTemp - 2 *
                                      nowX * nowX) + nowX * thirdTemp) / fourthTemp

        showBoard.create_line(x0 + (lastX * rad[star]), y0 + (
            lastY * rad[star]), x0 + (nowX * rad[star]), y0 + (nowY * rad[star]), fill="white")

    for i in range(-10000, 10000, 1):
        lastX = json.loads(json.dumps(nowX))
        lastY = json.loads(json.dumps(nowY))
        nowX = sX * (i / 10000)
        nowY = (-1 * firstTemp * math.sqrt(secondTemp - 2 *
                                           nowX * nowX) + nowX * thirdTemp) / fourthTemp

        showBoard.create_line(x0 + (lastX * rad[star]), y0 + (
            lastY * rad[star]), x0 + (nowX * rad[star]), y0 + (nowY * rad[star]), fill="white")


def move(event):
    global showBoard, x0, y0, ang, rad, xRad, yRad, preSin, preCos, preDSin, preDCos, dXRad, dYRad, sX,  firstTemp, secondTemp, thirdTemp, fourthTemp
    way = -1
    i = 10000

    nowX = sX
    nowY = (firstTemp * math.sqrt(secondTemp - 2 *
                                  nowX * nowX) + nowX * thirdTemp) / fourthTemp
    while(True):
        for star in range(0, 1):
            lastX = json.loads(json.dumps(nowX))
            lastY = json.loads(json.dumps(nowY))
            nowX = sX * (i / 10000)
            nowY = (-1 * way * firstTemp * math.sqrt(secondTemp - 2 *
                                                     nowX * nowX) + nowX * thirdTemp) / fourthTemp

            showBoard.create_oval(x0 + (lastX * rad[star]) + 10, y0 + (
                lastY * rad[star]) + 10, x0 + (lastX * rad[star]) - 10, y0 + (lastY * rad[star]) - 10, fill="black")

            tI, tTime = 0, 0
            tWay = -1 * way
            aX = json.loads(json.dumps(lastX))
            aY = json.loads(json.dumps(lastY))

            track = 20 * abs(way * (40 * abs(nowY))) + 100
            if track < 550:
                track = 550
            while tTime <= track:
                tI += tWay
                if i + tI > 10000 or i + tI < -10000:
                    tWay *= -1
                    tI += 2 * tWay

                bX = json.loads(json.dumps(aX))
                bY = json.loads(json.dumps(aY))
                aX = sX * ((i + tI) / 10000)
                aY = (tWay * firstTemp * math.sqrt(secondTemp -
                                                   2 * aX * aX) + aX * thirdTemp) / fourthTemp

                showBoard.create_line(x0 + (bX * rad[star]), y0 + (
                                      bY * rad[star]), x0 + (aX * rad[star]), y0 + (aY * rad[star]), fill="white")

                tTime += 1

            showBoard.create_oval(x0 + (nowX * rad[star]) + 10, y0 + (
                nowY * rad[star]) + 10, x0 + (nowX * rad[star]) - 10, y0 + (nowY * rad[star]) - 10, fill="aqua")

            showBoard.update()

        speed = 80 * abs(nowY)
        if speed < 200:
            speed = 200
        i += way * speed
        if i < -10000:
            way = 1
            i += -1 * (i + 10000)
        if i > 10000:
            way = -1
            i += -1 * (i - 10000)


window.bind("`", move)

tkinter.mainloop()
