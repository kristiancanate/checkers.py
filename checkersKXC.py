from graphics import *

sqSz = 50 #Defines size of squares

def create_tile():
    global sqSz
    tL = Rectangle(Point(sqSz, sqSz),
                   Point(sqSz * 2, sqSz * 2))
    tL.draw(chWin)

chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #Draws window
chWin. setCoords(0, 0, sqSz * 10, sqSz * 10) #Assigns coordinates to window

create_tile()

chWin.getMouse()
chWin.close()
