# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonSegundo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSegundo.setGeometry(QtCore.QRect(20, 20, 191, 131))
        self.buttonSegundo.setObjectName("buttonSegundo")
        self.buttonTerceiro = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTerceiro.setGeometry(QtCore.QRect(240, 20, 191, 131))
        self.buttonTerceiro.setObjectName("buttonTerceiro")
        self.buttonSair = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSair.setGeometry(QtCore.QRect(30, 190, 401, 91))
        self.buttonSair.setObjectName("buttonSair")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 460, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionSair_2 = QtWidgets.QAction(MainWindow)
        self.actionSair_2.setObjectName("actionSair_2")
        self.menuArquivo.addAction(self.actionSair_2)
        self.menuBar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        self.menuBar.hovered['QAction*'].connect(self.buttonSegundo.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonSegundo.setText(_translate("MainWindow", "Segundo"))
        self.buttonTerceiro.setText(_translate("MainWindow", "Terceiro"))
        self.buttonSair.setText(_translate("MainWindow", "SAIR"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair_2.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

