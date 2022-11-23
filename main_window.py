import sys
import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import scrnipt_1
import scrnipt_2
import scrnipt_3
import scrnipt_4


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        super(Window, self).__init__()

        self.setGeometry(800, 300, 1000, 900)
        self.setFixedSize(920, 800)
        self.setWindowTitle("Weather data")
        self.background = QLabel(self)
        self.fire = QLabel(self)
        self.background.setGeometry(0, 0, 1007, 925)
        self.background.setPixmap(QPixmap("File_folder/bluee.png"))

        self.base = QtWidgets.QLabel(self)
        self.base.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.base.setText("Создание и выбор аннотаций")
        self.base.move(220, 10) 
        self.base.adjustSize()

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Please select folder of dataset"
            )

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Разделение на года")   #добавить подсветку под кнопками
        self.b1.setFixedSize(400, 50)
        self.b1.move(275, 250)
        self.b1.clicked.connect(self.year)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Разделение на недели")
        self.b2.setFixedSize(400, 50)
        self.b2.move(275, 300)
        self.b2.clicked.connect(self.week)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Разделение на даты и данные")
        self.b3.setFixedSize(400, 50)
        self.b3.move(275, 350)
        self.b3.clicked.connect(self.data_date)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Ввести дату")
        self.b4.setFixedSize(400, 50)
        self.b4.move(275, 500)
        self.b4.clicked.connect(self.input_data)


    def data_date(self) -> None:
        scrnipt_1.run_1()


    def week(self) -> None:
        scrnipt_3.run_3()


    def year(self) -> None:
        scrnipt_2.run_2()


    def input_data(self) -> None:
        text, ok = QInputDialog.getText(self, 'Data',
            'Enter data:')

        if ok:
            self.le.setText(str(text))

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def application():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
