import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Kalkulator'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle(self.name)
        gridLayout = QGridLayout(self)

        digit = 0
        for i in range(3):
            for y in range(3):
                digit += 1
                digitButton = QPushButton(str(digit), self)
                gridLayout.addWidget(digitButton,i,y)

        self.show()

app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())