import graphics
import random

def drawTile(win, x, y, top, bot, left, right, center, color):
    win.rectangle(x + 5, y + 5, 90, 90, "grey")
    if(bot):
        win.line(x + 50, y + 45, x + 50, y + 95, color, 10)
    if(top):
        win.line(x + 50, y + 5, x + 50, y + 55, color, 10)
    if(left):
        win.line(x + 5, y + 50, x + 55, y + 50, color, 10)
    if(right):
        win.line(x + 45, y + 50, x + 95, y + 50, color, 10)
    if(center):
        win.rectangle(x + 35, y + 35, 30, 30, color)

def main():
    win = graphics.graphics(500, 500, "Pipe Grid")
    for i in range(5):
        for j in range(5):
            topRand = bool(random.getrandbits(1))
            botRand = bool(random.getrandbits(1))
            leftRand = bool(random.getrandbits(1))
            rightRand = bool(random.getrandbits(1))
            centerRand = bool(random.getrandbits(1))
            colorRand = "Black"
            if(bool(random.getrandbits(1))):
                colorRand = "Blue"
            drawTile(win, 100 * i, 100 * j, topRand, botRand, leftRand, rightRand, centerRand, colorRand)
    win.mainloop()

main()