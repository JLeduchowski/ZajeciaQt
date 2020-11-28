import random
from functools import partial

from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QPushButton

from Game import Game
from CellState import CellState

class DifficultyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.game = None
        self.name = "Saper"
        self.gridLayout = QGridLayout(self)
        self.difText = QLabel('Wybierz poziom trudności')
        self.initUI()


    def initUI(self):
        self.setFixedSize(500, 200)
        self.setGeometry(700, 400, 500, 200)

        buttonEasy = QPushButton(f'{"łatwy".title()}', self)
        buttonMedium = QPushButton('Średni', self)
        buttonHard = QPushButton('Trudny', self)
        buttonEasy.clicked.connect(lambda: self.initGameUI(300, 300, 10, 10))
        buttonMedium.clicked.connect(lambda: self.initGameUI(500, 500, 14, 25))
        buttonHard.clicked.connect(lambda: self.initGameUI(800, 800, 20, 50))


        self.gridLayout.addWidget(buttonEasy, 1, 0)
        self.gridLayout.addWidget(buttonMedium, 1, 1)
        self.gridLayout.addWidget(buttonHard, 1, 2)
        self.gridLayout.addWidget(self.difText, 0, 1)


        self.setWindowTitle(self.name)
        self.show()

    def initGameUI(self, width=500, height=500, playField=14, mines = 7):
        self.setFixedSize(width, height)
        for i in range(1, playField+1):
            self.buttons.append([])
            for j in range(0, playField):
                tempButton = QPushButton('', self)
                tempButton.clicked.connect(partial(self.onButtonClick, i - 1, j))
                self.buttons[i-1].append(tempButton)
                self.gridLayout.addWidget(tempButton , i, j)
        minesLeft = mines
        self.gridLayout.addWidget(QLabel(f'{minesLeft}'), 0, 0)
        self.difText.setText(' ')
        self.game = Game(playField,mines)

    def onButtonClick(self, x, y):
        self.game.checkCell(x+1,y+1)
        print(f'Clicked cell {x+1},{y+1}')
        print(f'')

        self.updateMap()
        print(f'')
        # for i in range(1, self.game.gameMap.size + 1):
        #     print(f'')
        #     for y in range(1, self.game.gameMap.size + 1):
        #         print(f'{self.game.gameMap.map[i][y].mineIndicator} ', end = "")
        self.game.gameMap.showMapConsole()

    def updateMap(self):
        for x in range(1, self.game.gameMap.getSize()+1):
            for y in range(1, self.game.gameMap.getSize()+1):
                if(self.game.gameMap.map[x][y].getmineIndicator() > 0):
                    self.buttons[x-1][y-1].setText(str(self.game.gameMap.map[x][y].getmineIndicator()))
                if (self.game.gameMap.map[x][y].getState() == CellState.covered):
                    self.buttons[x - 1][y - 1].setDisabled(True)
                if (self.game.gameMap.map[x][y].isBomb == True):
                    self.buttons[x-1][y-1].setText('B')





