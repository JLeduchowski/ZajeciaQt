import random
import sys
from functools import partial
import time
from threading import Thread

from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QPushButton, \
    QMessageBox, QApplication, qApp

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
        #self.flagsLeft = 0
        self.flagLabel = None
        self.timer = None
        self.timeLabel = QLabel('')

    def initUI(self):
        self.setFixedSize(500, 200)
        self.setGeometry(700, 400, 500, 200)
        self.timer = time.perf_counter()
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

    def initGameUI(self, width=500, height=500, playField=10, mines = 10):
        self.timer = time.perf_counter()
        self.Timer.start()
        self.setFixedSize(width, height)
        for i in range(1, playField+1):
            self.buttons.append([])
            for j in range(0, playField):
                tempButton = QPushButton('', self)
                tempButton.clicked.connect(partial(self.onButtonClick, i - 1, j))
                tempButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                tempButton.customContextMenuRequested.connect(partial(self.onRightClick, i-1, j))
                self.buttons[i-1].append(tempButton)
                self.gridLayout.addWidget(tempButton , i, j)
        self.flagsLeft = mines
        self.flagLabel = QLabel(f'{self.flagsLeft}')
        self.gridLayout.addWidget(self.flagLabel, 0, 0)
        self.difText.setText(' ')
        self.game = Game(playField,mines)


    def onRightClick(self, x, y):
        self.game.flagCell(x+1, y+1)
        self.flagLabel.setText(f'{self.game.flags}')
        if self.game.checkIfWin():
            self.celebration()
        self.updateMap()


    def onButtonClick(self, x, y):
        self.game.checkCell(x+1, y+1)
        print(f'Clicked cell {x+1},{y+1}')
        print(f'')
        self.flagLabel.setText(f'{self.game.flags}')
        self.updateMap()
        print(f'')
        # for i in range(1, self.game.gameMap.size + 1):
        #     print(f'')
        #     for y in range(1, self.game.gameMap.size + 1):
        #         print(f'{self.game.gameMap.map[i][y].mineIndicator} ', end = "")
        if self.game.gameMap.map[x+1][y+1].isBomb:
            self.showAllMines()
            self.sadness()
            return

        if self.game.checkIfWin():
            self.celebration()
        self.game.gameMap.showMapConsole()

    def updateMap(self):
        for x in range(1, self.game.gameMap.getSize()+1):
            for y in range(1, self.game.gameMap.getSize()+1):
                if self.game.gameMap.map[x][y].getmineIndicator() > 0:
                    self.buttons[x-1][y-1].setText(str(self.game.gameMap.map[x][y].getmineIndicator()))
                if self.game.gameMap.map[x][y].getState() == CellState.covered:
                    self.buttons[x - 1][y - 1].setDisabled(True)
                if self.game.gameMap.map[x][y].isBomb:
                    self.buttons[x-1][y-1].setText('B')
                if self.game.gameMap.map[x][y].getState() == CellState.flagged:
                    self.buttons[x-1][y-1].setText('F')
                if self.game.gameMap.map[x][y].getState() == CellState.uncovered:
                    self.buttons[x-1][y-1].setText('')

    def showAllMines(self):
        for x in range(1, self.game.gameMap.getSize()+1):
            for y in range(1, self.game.gameMap.getSize()+1):
                if self.game.gameMap.map[x][y].isBomb:
                    self.buttons[x-1][y-1].setText('B')

    def celebration(self):
        timeEnd = time.perf_counter()
        choice = QMessageBox.question(self,
                'Gratulacje', f'Brawo, zajęło Ci to {timeEnd-self.timer:0.2f} sekund czy chcesz zagrać jeszcze raz?',
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('hej')
        elif choice == QMessageBox.No:
            return
        else:
            print('oj')

    def sadness(self):
        msgBox = QMessageBox()
        qApp.beep()
        msgBox.setText('oj widzowie nie udalo sie')
        msgBox.setWindowTitle('PORAŻKA')
        msgBox.exec()

    #class Timer(Thread):
    #    startTime = time.perf_counter()
    #    while True:
    #        currentTime = time.perf_counter() - startTime
    #        time.sleep(0.9)
