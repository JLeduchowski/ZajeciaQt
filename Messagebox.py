import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, \
    QPushButton, QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Msg'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle(self.name)

        buttonMsg = QPushButton('Exit', self)
        buttonMsg.resize(100, 25)
        buttonMsg.move(100, 125)
        buttonMsg.clicked.connect(self.showMsg)

        self.show()

    def showMsg(self):
        choice = QMessageBox.question(self, 'Wybierz', 'Czy na pewno chcesz zakonczyc dzialanie aplikacji?'
                                      , QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()

app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())