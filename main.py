import Game
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, \
    QApplication


class DifficultyWindow(QWidget):
    def __init__(self):
        super().__init__()
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
        buttonEasy.clicked.connect(self.easyClick)
        buttonMedium.clicked.connect(self.mediumClick)
        buttonHard.clicked.connect(self.hardClick)

        self.gridLayout.addWidget(buttonEasy, 1, 0)
        self.gridLayout.addWidget(buttonMedium, 1, 1)
        self.gridLayout.addWidget(buttonHard, 1, 2)
        self.gridLayout.addWidget(self.difText, 0, 1)

        self.setWindowTitle(self.name)
        self.show()

    def initGameUI(self, width=500, height=500, playField=14):
        self.setFixedSize(width, height)
        for i in range(1, playField):
            for j in range(0, playField):
                self.gridLayout.addWidget(QPushButton(' ', self), i, j)
        minesLeft = playField
        self.gridLayout.addWidget(QLabel(f'{minesLeft}'), 0, 0)
        self.difText.setText(' ')

    def easyClick(self):
        self.initGameUI(300, 300, 10)

    def mediumClick(self):
        self.initGameUI(500, 500, 14)

    def hardClick(self):
        self.initGameUI(800, 800, 20)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = DifficultyWindow()
    sys.exit(app.exec_())


    # g1.gameMap.showMapConsole()
    # print(f'')
    # g1.checkCell(2,2)
    # for i in range(1, g1.gameMap.size + 1):
    #     print(f'')
    #     for y in range(1, g1.gameMap.size + 1):
    #         print(f'{g1.gameMap.map[i][y].mineIndicator} ', end = "")
    g1.gameMap.showMapConsole()

    print(f'')

    string = input('Podaj wspolrzedne odkrywki (x,y) ')
    while string != "quit":
        string_split = string.split(',')
        x = int(string_split[0])
        y = int(string_split[1])
        # print(f'{x},{y}')
        g1.checkCell(x, y)
        g1.gameMap.showMapConsole()
        string = input('Podaj wspolrzedne odkrywki (x,y) ')
