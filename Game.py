import Map
from CellState import CellState


class Game:

    gameMap = None
    checkList = []

    def __init__(self,playfield, mines):
        self.timer = 0
        self.flags = 0
        self.gameMap = Map.Map(playfield,mines)
        self.flags = mines

    def startTimer(self):
        pass

    def stopTimer(self):
        pass

    def checkCell(self, x, y):
        if self.gameMap.map[x][y].state == CellState.flagged:
            self.gameMap.map[x][y].state = CellState.uncovered
            self.flags += 1
        else:
            if not self.gameMap.map[x][y].isBorder:
                if self.gameMap.map[x][y].mineIndicator == 0 and \
                        self.gameMap.map[x][y].state == CellState.uncovered:
                    for i in range(x - 1, x + 2):
                        for z in range(y - 1, y + 2):
                            if i != x or z != y:
                                # print(f'sprawdzam otoczenie punktu {x},{y}, czyli - {i},{z}')
                                if self.gameMap.map[i][z].isBomb:
                                    self.gameMap.map[x][y].mineIndicator += 1
                if self.gameMap.map[x][y].mineIndicator == 0:
                    for i in range(x - 1, x + 2):
                        for z in range(y - 1, y + 2):
                            if i != x or z != y:
                                coords = (i, z)
                                if self.gameMap.map[i][
                                    z].state == CellState.uncovered:
                                    self.checkList.append(
                                        coords) if coords not in self.checkList else self.checkList
                                    # print(f'lista: {self.checkList}')
            # print(f'oznaczam punkt {x},{y} jako covered')
            self.gameMap.map[x][y].state = CellState.covered
            if self.checkList:
                pair = self.checkList.pop(0)
                Game.checkCell(self, pair[0], pair[1])

    def setLevel(self, level):
        self.level = level

    def flagCell(self, x, y):
        self.gameMap.map[x][y].state = CellState.flagged
        self.flags -= 1


    def checkIfWin(self):
        win = False
        if self.flags == 0:
            win = True
            for i in range(1, self.gameMap.size+1):
                for j in range(1, self.gameMap.size+1):
                    if self.gameMap.map[i][j].state == CellState.uncovered:
                        win = False
        return win




