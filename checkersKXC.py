from graphics import *

sqSz = 50 #Defines size of squares

def create_tile(tR, tC):
    global sqSz
    tL = Rectangle(Point(sqSz * (tR + 1), sqSz * (tC + 1)),
                   Point(sqSz * (tR + 2), sqSz * (tC + 2)))
    if tC % 2 == 0: #even
        if tR % 2 == 0: #even
            tL.setFill("red")
        else: #odd
            tL.setFill("black")
    else: #odd
        if tR % 2 == 1: #odd
            tL.setFill("red")
        else: #even
            tL.setFill("black")
    tL.draw(chWin)

chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #Draws window
chWin. setCoords(0, 0, sqSz * 10, sqSz * 10) #Assigns coordinates to window

for j in range(8):
    for i in range(8):
        create_tile(i, j)

chWin.getMouse()
chWin.close()
