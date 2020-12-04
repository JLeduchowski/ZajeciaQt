from asyncio import Event
from datetime import datetime

import Game
import MyTimer
import GameUI
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, \
    QApplication

if __name__ == '__main__':



    # thread = MyTimer.MyTimer()
    # thread.start()

    app = QApplication(sys.argv)
    ex = GameUI.DifficultyWindow()
    sys.exit(app.exec_())

    # g1 = Game.Game();
    # g1.gameMap.showMapConsole()
    # print(f'')
    # g1.checkCell(2,2)
    # for i in range(1, g1.gameMap.size + 1):
    #     print(f'')
    #     for y in range(1, g1.gameMap.size + 1):
    #         print(f'{g1.gameMap.map[i][y].mineIndicator} ', end = "")
    # g1.gameMap.showMapConsole()

    # print(f'')
    #
    # string = input('Podaj wspolrzedne odkrywki (x,y) ')
    # while string != "quit":
    #     string_split = string.split(',')
    #     x = int(string_split[0])
    #     y = int(string_split[1])
    #     # print(f'{x},{y}')
    #     g1.checkCell(x, y)
    #     g1.gameMap.showMapConsole()
    #     string = input('Podaj wspolrzedne odkrywki (x,y) ')
