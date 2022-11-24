import sys
import PyQt5
import datetime
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import scrnipt_1
import scrnipt_2
import scrnipt_3
import scrnipt_4

class Window2(QWidget):                           # <===
    def __init__(self, date):
        super().__init__()
        print(date)

        self.setGeometry(250, 55, 600, 600)
        self.setWindowTitle('Выбор файла')

        self.b2_1 = QPushButton('Найти данные в файле по дата/данные', self)
        self.b2_1.resize(170, 50)
        self.b2_1.move(40, 100)
        self.b2_1.clicked.connect(self.date_data)

        self.b2_2 = QPushButton('Найти данные в файле по годам', self)
        self.b2_2.resize(170, 50)
        self.b2_2.move(40, 150)
        self.b2_2.clicked.connect(self.sort_week)

        self.b2_3 = QPushButton('Найти данные по неделям', self)
        self.b2_3.resize(170, 50)
        self.b2_3.move(40, 200)
        self.b2_3.clicked.connect(self.sort_week)

        self.b2_4 = QPushButton('Найти данные по датасету', self)
        self.b2_4.resize(170, 50)
        self.b2_4.move(40, 250)
        self.b2_4.clicked.connect(self.sort_week)
      
    def date_data(self):
        pass
    def years(self):
        pass
    def week(self):
        pass
    def dataset(self):
        pass





    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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
        self.b2.clicked.connect(self.sort_week)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Разделение на даты и данные")
        self.b3.setFixedSize(400, 50)
        self.b3.move(275, 350)
        self.b3.clicked.connect(self.sort_data_date)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Ввести дату")
        self.b4.setFixedSize(400, 50)
        self.b4.move(275, 500)
        self.b4.clicked.connect(self.input_data)


    def sort_data_date(self) -> None:
        scrnipt_1.run_1()
        QMessageBox.about(self, "data_date", "Данные отсорированны")


    def sort_week(self) -> None:
        scrnipt_3.run_3()
        QMessageBox.about(self, "week", "Данные отсорированны")


    def sort_year(self) -> None:
        scrnipt_2.run_2()
        QMessageBox.about(self, "year", "Данные отсорированны")


    def input_data(self) -> None:
        text, ok = QInputDialog.getText(self, 'Data',
            'Enter the data in the format dd.mm.yyyy:')

        if ok:
            if (0<=int(text[0:2])<=31 and 0<=int(text[3:5])<=12 and 0<=int(text[6:10])<=3000):
                date = datetime.date(int(text[6:10]), int(text[3:5]), int(text[0:2]))
                self.show_window_2(date)

                #self.hide()
            else: 
                QMessageBox.about(self, "Внимание", "Вводите реальные даты...")

    def show_window_2(self, date):
        self.w2 = Window2(date)
        self.w2.show()

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
