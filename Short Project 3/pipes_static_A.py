import graphics
import os

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

    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    win = graphics.graphics(500, 500, "Pipe Grid")
    #row 1
    drawTile(win, 0, 0, False, True, False, True, False, "black")
    drawTile(win, 100, 0, False, False, True, True, False, "black")
    drawTile(win, 200, 0, False, False, False, True, True, "black")
    drawTile(win, 300, 0, False, True, True, False, False, "black")
    drawTile(win, 400, 0, False, True, False, False, True, "black")
    #row 2
    drawTile(win, 0, 100, True, True, False, False, False, "black")
    drawTile(win, 100, 100, False, True, False, False, True, "blue")
    drawTile(win, 200, 100, False, False, True, False, True, "black")
    drawTile(win, 300, 100, True, False, True, True, False, "black")
    drawTile(win, 400, 100, False, False, False, True, True, "black")
    #row 3
    drawTile(win, 0, 200, False, True, True, True, False, "black")
    drawTile(win, 100, 200, True, True, False, True, False, "blue")
    drawTile(win, 200, 200, True, True, True, False, True, "blue")
    drawTile(win, 300, 200, False, True, True, True, False, "black")
    drawTile(win, 400, 200, False, False, True, False, True, "black")
    #row 4
    drawTile(win, 0, 300, False, True, False, True, False, "blue")
    drawTile(win, 100, 300, True, False, True, True, False, "blue")
    drawTile(win, 200, 300, True, False, False, True, False, "blue")
    drawTile(win, 300, 300, True, True, False, True, False, "black")
    drawTile(win, 400, 300, True, False, True, True, False, "black")
    #row 5
    drawTile(win, 0, 400, False, True, False, False, True, "black")
    drawTile(win, 100, 400, True, False, True, False, False, "black")
    drawTile(win, 200, 400, False, False, False, True, True, "black")
    drawTile(win, 300, 400, False, True, False, False, True, "black")
    drawTile(win, 400, 400, False, True, False, False, True, "black")
    win.mainloop()

main()