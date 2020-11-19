import Map
from CellState import CellState


class Game:

    gameMap = None
    checkList = []

    def __init__(self,level = "easy"):
        self.timer = 0
        self.flags = 0
        self.level = level
        if level == "easy":
            self.gameMap = Map.Map(8,10)
            self.flags = 3

    def startTimer(self):
        pass

    def stopTimer(self):
        pass

    def checkCell(self,x,y):

        if not self.gameMap.map[x][y].isBorder:
                if self.gameMap.map[x][y].mineIndicator == 0 and self.gameMap.map[x][y].state == CellState.uncovered:
                    for i in range(x-1, x+2):
                      for z in range(y-1, y+2):
                         if i != x or z != y:
                            # print(f'sprawdzam otoczenie punktu {x},{y}, czyli - {i},{z}')
                            if(self.gameMap.map[i][z].isBomb):
                                self.gameMap.map[x][y].mineIndicator += 1
                if self.gameMap.map[x][y].mineIndicator == 0:
                    for i in range(x-1, x+2):
                      for z in range(y-1, y+2):
                         if i != x or z != y:
                            coords = (i, z)
                            if self.gameMap.map[i][z].state == CellState.uncovered:
                                self.checkList.append(coords) if coords not in self.checkList else self.checkList
                                # print(f'lista: {self.checkList}')
        # print(f'oznaczam punkt {x},{y} jako covered')
        self.gameMap.map[x][y].state = CellState.covered
        if self.checkList:
            pair = self.checkList.pop(0)
            Game.checkCell(self,pair[0],pair[1])

    def setLevel(self,level):
        self.level = level

    def flagCell(self):
        pass

    def checkIfWin(self):
        pass





