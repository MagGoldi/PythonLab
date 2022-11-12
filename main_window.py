#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5 import QtCore
from PyQt5 import QtGui


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowIcon(QtGui.QIcon('C://PYTHON//PythonLab3//blue_lobster.jpg'))
        self.setWindowIcon(QtGui.QIcon("C://PYTHON//PythonLab3//blue.png"))
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())