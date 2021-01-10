import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *

class ProgressBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lista = []
        self.iloscObiektow = 0

        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 500)
        self.progressBar = QProgressBar(self)
        self.lineEdit = QLineEdit(self)
        self.button = QPushButton(self)
        self.progressBar.move(5, 5)
        self.lineEdit.move(150,5)
        self.button.move(300,5)
        self.progressBar.setValue(0)
        self.button.setText('Dodaj do listy')
        self.button.clicked.connect(self.ListProgress)
        self.show()

    def PokazListe(self):
        print(f'Lista zawiera {self.iloscObiektow} obiektow.')
        for i in range(self.iloscObiektow):
            print(f'{i+1}. {self.lista[i]}')

    def ListProgress(self):
        value = self.progressBar.value()
        if value < 100:
            if(self.lineEdit.text() != ''):
                value = value + 10
                self.iloscObiektow += 1
                self.progressBar.setValue(value)
                self.lista.append(self.lineEdit.text())
                self.PokazListe()
        else:
            print('Lista jest pelna')

app = QApplication(sys.argv)
window = ProgressBarDemo()
sys.exit(app.exec_())