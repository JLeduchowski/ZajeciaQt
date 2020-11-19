from CellState import CellState

class Cell(object):

    def __init__(self):
        self.state = CellState.uncovered
        self.mineIndicator = 0
        self.isBomb = False
        self.isBorder = False

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setmineIndicator(self, mineIndicator):
        self.mineIndicator = mineIndicator

    def getmineIndicator(self):
        return self.mineIndicator

    def setIsBomb(self, bool):
        self.isBomb = bool

    def getIsBomb(self):
        return self.isBomb

    def setIsBorder(self,bool):
        self.isBorder = bool

    def getIsBorder(self):
        return self.isBorder

