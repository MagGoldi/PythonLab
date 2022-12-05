import sys
import datetime
import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QPixmap

import scrnipt_1
import scrnipt_2
import scrnipt_3
import scrnipt_4


class Window2(QWidget):
    def __init__(self, date: datetime.date, path_to_csv: os.path ) -> None:
        """designer class Window2"""
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(path_to_csv + '/polnayapapka.png'))

        self.setGeometry(250, 500, 600, 500)
        self.background_2 = QLabel(self)
        self.fire = QLabel(self)
        self.background_2.setGeometry(-50, -100, 1007, 925)
        self.background_2.setPixmap(QPixmap(path_to_csv + "/cat.png"))
        self.setWindowTitle('File Selection')

        self.base_2 = QtWidgets.QLabel(self)
        self.base_2.setFont(QtGui.QFont("Times", 11, QtGui.QFont.Light))
        self.base_2.setText("Найти данные в файле по...")
        self.base_2.move(100, 10)
        self.base_2.setStyleSheet("background-color: white; border: 1px solid black;")
        self.base_2.adjustSize()

        self.b2_1 = QPushButton('Дата/Данные', self)
        self.b2_1.resize(250, 80)
        self.b2_1.move(170, 100)
        self.b2_1.clicked.connect(lambda: self.date_data(date))

        self.b2_2 = QPushButton('Годам', self)
        self.b2_2.resize(250, 80)
        self.b2_2.move(170, 180)
        self.b2_2.clicked.connect(lambda: self.years(date))

        self.b2_3 = QPushButton('Неделям', self)
        self.b2_3.resize(250, 80)
        self.b2_3.move(170, 260)
        self.b2_3.clicked.connect(lambda: self.week(date))

        self.b2_4 = QPushButton('Dataset', self)
        self.b2_4.resize(250, 80)
        self.b2_4.move(170, 340)
        self.b2_4.clicked.connect(lambda: self.dataset(date))

    def date_data(self, date: datetime.date) -> None:
        """function search data in file date/data"""
        tmp = scrnipt_4.work_1(date)
        QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")

    def years(self, date: datetime.date) -> None:
        """"function search data in file years"""
        tmp = scrnipt_4.work_2(date)
        QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")

    def week(self, date: datetime.date) -> None:
        """function search data in file week"""
        tmp = scrnipt_4.work_3(date)
        QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")

    def dataset(self, date: datetime.date) -> None:
        """function search data in file dateset"""
        tmp = scrnipt_4.work_0(date)
        QMessageBox.about(self, "Информация по дате", f"Дата: {date} \nДанные : {tmp}")

    def closeEvent(self, event) -> None:
        """function calling window question exit"""
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Window(QMainWindow):

    def __init__(self) -> None:
        """designer class Window"""
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        "main functions work class Window"
        path_to_csv = os.path.join("C:/", "PYTHON", "PythonLab3", "File_folder")
        super(Window, self).__init__()
        self.setWindowIcon(QtGui.QIcon(path_to_csv+'/cloud.png'))

        self.setGeometry(800, 300, 900, 900)
        self.setFixedSize(920, 800)
        self.setWindowTitle("Weather data")
        self.background = QLabel(self)
        self.fire = QLabel(self)
        self.background.setGeometry(0, 0, 1000, 900)
        self.background.setPixmap(QPixmap(path_to_csv+"/bib.png"))

        self.base = QtWidgets.QLabel(self)
        self.base.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.base.setText("Создание и выбор аннотаций")
        self.base.move(190, 10)
        self.base.adjustSize()

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Please select folder of dataset"
            )

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Разделение на года")  # добавить подсветку под кнопками
        self.b1.setFixedSize(400, 50)
        self.b1.move(275, 250)
        self.b1.clicked.connect(self.sort_year)

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
        """sorting function by data/date"""
        scrnipt_1.run_1()
        QMessageBox.about(self, "Sort", "Sorting by date")

    def sort_week(self) -> None:
        """sorting function by week"""
        scrnipt_3.run_3()
        QMessageBox.about(self, "Sort", "Sorting by week")

    def sort_year(self) -> None:
        """sorting function by year"""
        scrnipt_2.run_2()
        QMessageBox.about(self, "Sort", "Sorting by year")

    def check_date(self, text: str) -> bool:
        Flag = False
        check, check_value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], ["0", "1", "3", "4", "6", "7", "8", "9"]
        if  len(text) != 10: return False
        for i in range(len(check_value)):
            for j in range(len(check)):  
                if text[int(check_value[i])] == check[j]: Flag = True
            if Flag == False: return False    
        if (0 <= int(text[0:2]) <= 31 and 0 <= int(text[3:5]) <= 12 and 2005 <= int(text[6:10]) <= 2030): return True
        else: return False

    def input_data(self) -> None:
        """a function that accepts a date and checks it for correctness"""
        text, ok = QInputDialog.getText(self, 'Data',
                                        'Enter the data in the format dd.mm.yyyy:')
        dictionary = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if ok:
            if self.check_date(text) == True:
                        if  int(text[0:2])<=dictionary[int(text[3:5])-1]:
                            date = datetime.date(int(text[6:10]), int(text[3:5]), int(text[0:2]))
                            self.show_window_2(date)
                        else:  QMessageBox.about(self, "warning!", "Неправильные данные...")    
            else:  QMessageBox.about(self, "warning!", "Неправильный формат входных данных...")

    def show_window_2(self, date: datetime.date) -> None:
        """function calling window 2"""
        self.w2 = Window2(date, path_to_csv = os.path.join("C:/", "PYTHON", "PythonLab3", "File_folder"))
        self.w2.show()

    def closeEvent(self, event) -> None:
        """function calling window question exit"""

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def application() -> None:
    """functions showing window"""
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()