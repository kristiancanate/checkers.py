from graphics import *

sqSz = 50 #Defines size of squares

def create_tile(tR, tC, color):
    global sqSz
    tL = Rectangle(Point(sqSz * (tR + 1), sqSz * (tC + 1)),
                   Point(sqSz * (tR + 2), sqSz * (tC + 2)))
    tL.setFill(color)
    tL.draw(chWin)

print("""Please input what colors you would like the checkerboard to be.
If you'd like a standard red & black board, simply leave the input empty
by hitting return:""")
uC1 = input()
if uC1 != "":
    uC2 = input()
else:
    uC1 = "red"
    uC2 = "black"

chWin = GraphWin("Checkers", sqSz * 10, sqSz * 10) #Draws window
chWin. setCoords(0, 0, sqSz * 10, sqSz * 10) #Assigns coordinates to window

for j in range(8):
    for i in range(8):
        if j % 2 == 0: #even
            if i % 2 == 0: #even
                sqCol = uC1
            else: #odd
                sqCol = uC2
        else: #odd
            if i % 2 == 1: #odd
                sqCol = uC1
            else: #even
                sqCol = uC2
        create_tile(i, j, sqCol)

chWin.getMouse()
chWin.close()
