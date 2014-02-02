# Bonnie Ishiguro
# 02/01/2014

def drawGrid(numRows,numCols):
    for i in range(0,numRows):
        drawPlusLine(numCols)
        drawDashLines(numCols)
    drawPlusLine(numCols)        

def drawPlusLine(numCols):
    print ("+ " + "- "*4)*numCols + "+"

def drawDashLines(numCols):
    for i in range(0,4):
        print ("|" + " "*9)*numCols + "|"