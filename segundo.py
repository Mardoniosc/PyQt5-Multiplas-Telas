# coding: utf-8
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.uic import loadUi


class Segundo(QWidget):
    def __init__(self):
        super(Segundo, self).__init__()
        loadUi('segundo.ui', self)
        self.setWindowTitle('Segundo')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=Segundo()
    widget.show()
    sys.exit(app.exec())
