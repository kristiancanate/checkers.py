from graphics import *

sqSz = 50 #Defines size of squares

def create_tile(tlN):
    global sqSz
    tL = Rectangle(Point(sqSz * (tlN + 1), sqSz),
                   Point(sqSz * (tlN + 2), sqSz * 2))
    tL.draw(chWin)

chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #Draws window
chWin. setCoords(0, 0, sqSz * 10, sqSz * 10) #Assigns coordinates to window

for i in range(8):
    create_tile(i)

chWin.getMouse()
chWin.close()
