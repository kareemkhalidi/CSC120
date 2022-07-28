from tkinter.constants import Y
import graphics

def main():

    #initialize window, counter, and y positions
    win = graphics.graphics(600, 325, "Animation")
    yPosition = 100
    counter = 1

    while(not win.is_destroyed()):

        #track y position
        if(yPosition == 100):
            yPosition = 150
        else:
            yPosition = 100

        #track where in the animation we are
        counter += 1
        if(counter > 40):
            counter = 1

        win.clear()

        #head and body 1
        win.ellipse(75, yPosition, 50, 50, "white")
        win.line(75, yPosition + 25, 75, yPosition + 125)

        #head and body 2
        win.ellipse(225, yPosition, 50, 50, "white")
        win.line(225, yPosition + 25, 225, yPosition + 125)

        #head and body 3
        win.ellipse(375, yPosition, 50, 50, "white")
        win.line(375, yPosition + 25, 375, yPosition + 125)

        #head and body 4
        win.ellipse(525, yPosition, 50, 50, "white")
        win.line(525, yPosition + 25, 525, yPosition + 125)

        #legs up position
        if(yPosition == 100):
            win.line(75, 225, 50, 325)
            win.line(75, 225, 100, 325)

            win.line(225, 225, 200, 325)
            win.line(225, 225, 250, 325)

            win.line(375, 225, 350, 325)
            win.line(375, 225, 400, 325)

            win.line(525, 225, 500, 325)
            win.line(525, 225, 550, 325)

        #legs down position
        if(yPosition == 150):
            win.line(75, 275, 55, 300)
            win.line(55, 300, 50, 325)
            win.line(75, 275, 95, 300)
            win.line(95, 300, 100, 325)

            win.line(225, 275, 205, 300)
            win.line(205, 300, 200, 325)
            win.line(225, 275, 245, 300)
            win.line(245, 300, 250, 325)

            win.line(375, 275, 355, 300)
            win.line(355, 300, 350, 325)
            win.line(375, 275, 395, 300)
            win.line(395, 300, 400, 325)

            win.line(525, 275, 505, 300)
            win.line(505, 300, 500, 325)
            win.line(525, 275, 545, 300)
            win.line(545, 300, 550, 325)

        #arms for figure 1
        if(counter <= 8):
            win.line(75, yPosition + 25, 50, yPosition + 125)
            win.line(75, yPosition + 25, 100, yPosition + 125)
        else:
            win.line(75, yPosition + 50, 25, yPosition - 75)
            win.line(75, yPosition + 50, 125, yPosition - 75)

        #arms for figure 2
        if(counter <= 16):
            win.line(225, yPosition + 25, 200, yPosition + 125)
            win.line(225, yPosition + 25, 250, yPosition + 125)
        else:
            win.line(225, yPosition + 50, 200, yPosition - 25)
            win.line(200, yPosition - 25, 225, yPosition - 10)
            win.line(225, yPosition + 50, 250, yPosition - 25)
            win.line(250, yPosition - 25, 225, yPosition - 10)

        #arms for figure 3
        if(counter <= 24):
            win.line(375, yPosition + 25, 350, yPosition + 125)
            win.line(375, yPosition + 25, 400, yPosition + 125)
        else:
            win.line(375, yPosition + 50, 475, yPosition)
            win.line(375, yPosition + 50, 475, yPosition + 100)

        #arms for figure 4
        if(counter <= 32):
            win.line(525, yPosition + 25, 500, yPosition + 125)
            win.line(525, yPosition + 25, 550, yPosition + 125)
        else:
            win.line(525, yPosition + 50, 500, yPosition - 25)
            win.line(500, yPosition - 25, 515, yPosition - 75)
            win.line(525, yPosition + 50, 550, yPosition - 25)
            win.line(550, yPosition - 25, 535, yPosition - 75)

        win.update_frame(3)


main()