import random

class MineModel(object):

    def __init__(self, w, h, m):
        self.width = w
        self.height = h
        self.totalMines = m
        self.totalMoves = 0
        self.gameOver = False

        self.boardData = []

        for row in range(self.height):
            self.boardData.append( [] )

            for col in range(self.width):
                cellDict = {}
                self.boardData[row].append( cellDict )
                cellDict['hasBomb'] = False
                cellDict['exposed'] = False
                cellDict['neighbors'] = 0

        self.placeMines(self.totalMines)
        self.calcAdjacent()

    def getGameOver(self):
        return self.gameOver

    def setGameOver(self):
        self.gameOver = True

    def getTotalMoves(self):
        return self.totalMoves

    def incrementTotalMoves(self):
        self.totalMoves += 1

    def getCellValue(self, row, col):
        """This method will return -1 if a bomb is there.
           If no bomb, it will return how many neighbor
           bombs there are.
        """
        if self.boardData[row][col]['hasBomb']:
            return -1
        else:
            return self.boardData[row][col]['neighbors']

    def getCellExposed(self, row, col):
        return self.boardData[row][col]['exposed']

    def setCellExposed(self, row, col):
        self.boardData[row][col]['exposed'] = True

    def reset(self):
        self.gameOver = False
        self.totalMoves = 0
        self.resetPos()
        self.placeMines(self.totalMines)
        self.calcAdjacent()
        
    def resetPos(self):
        for row in range(self.height):
            for col in range(self.width):
                self.boardData[row][col]['hasBomb'] = False
                self.boardData[row][col]['exposed'] = False
                self.boardData[row][col]['neighbors'] = 0

        #for row in range(self.height):
        #    for col in range(self.width):
        #        r = self.grid.itemAtPosition(y,x).widget()
        #        r.reset()

    def placeMines(self, totalMines):
        bombsPlaced = 0
        while bombsPlaced < totalMines:
            x = random.randint(0,9) 
            y = random.randint(0,9) 
            if not self.boardData[y][x]['hasBomb']:
                bombsPlaced += 1
                self.boardData[y][x]['hasBomb'] = True

    def getBombValue(self, row, col):
        if row < 0:
            return 0
        if row >= self.height:
            return 0
        if col < 0:
            return 0
        if col >= self.width:
            return 0
        if self.boardData[row][col]['hasBomb']:
            return 1
        else:
            return 0


    def calcAdjacent(self):
        offsetx = [-1,-1,-1, 0, 1, 1, 1, 0]
        offsety = [-1, 0, 1, 1, 1, 0,-1,-1]
        for row in range(self.height):
            for col in range(self.width):
                count = 0
                for i in range(8):
                    count += self.getBombValue(row+offsety[i], col+offsetx[i])
                self.boardData[row][col]['neighbors'] = count


            
