from graphics import *

sqSz = 50 #Defines size of squares

def create_tile(tR, tC, color):
    global sqSz
    tL = Rectangle(Point(sqSz * (tR + 1), sqSz * (tC + 1)),
                   Point(sqSz * (tR + 2), sqSz * (tC + 2)))
    tL.setFill(color)
    tL.draw(chWin)

chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #Draws window
chWin. setCoords(0, 0, sqSz * 10, sqSz * 10) #Assigns coordinates to window

for j in range(8):
    for i in range(8):
        if j % 2 == 0: #even
            if i % 2 == 0: #even
                sqCol = "red"
            else: #odd
                sqCol = "black"
        else: #odd
            if i % 2 == 1: #odd
                sqCol = "red"
            else: #even
                sqCol = "black"
        create_tile(i, j, sqCol)

chWin.getMouse()
chWin.close()
