import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from typing import Self


if __name__ == '__main__':

    app = QApplication(sys.argv)
    folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
    