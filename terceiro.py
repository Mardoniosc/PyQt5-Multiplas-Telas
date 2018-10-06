# coding: utf-8
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QDialog
from PyQt5.uic import loadUi


class Terceiro(QDialog):
    def __init__(self):
        super(Terceiro, self).__init__()
        loadUi('terceiro.ui', self)
        self.setWindowTitle('terceiro')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=Terceiro()
    widget.show()
    sys.exit(app.exec())
