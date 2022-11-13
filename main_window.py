import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt


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

        self.setGeometry(300, 250, 1007, 925)
        self.setFixedSize(1007, 925)
        self.setWindowTitle("Данные о")
        self.background = QLabel(self)
        self.fire = QLabel(self)
       #картинка
        self.background.setGeometry(0, 0, 1007, 925)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Создание и выбор аннотаций")
        self.main_text.move(725, 10)
        self.main_text.adjustSize()

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Please select folder of dataset"
            )

        self.botton1 = QtWidgets.QPushButton(self)
        self.botton1.setText("Разделение на года")
        self.botton1.setFixedWidth(300)
        self.botton1.move(670, 30)
        self.botton1.clicked.connect(self.year)

        self.botton2 = QtWidgets.QPushButton(self)
        self.botton2.setText("Разделение на недели")
        self.botton2.setFixedWidth(300)
        self.botton2.move(670, 60)
        self.botton2.clicked.connect(self.week)

        self.botton3 = QtWidgets.QPushButton(self)
        self.botton3.setText("Разделение на даты и данные")
        self.botton3.setFixedWidth(300)
        self.botton3.move(670, 90)
        self.botton3.clicked.connect(self.data_date)

    def hidden_text(self):
        self.text = QtWidgets.QPushButton(self)
        self.text.setText("Введите дату дд/мм/гггг")
        self.text.move(735, 120)
        self.text.adjustSize()

        self.fire.setGeometry(0, 0, 686, 520)
        self.fire.setPixmap(QPixmap('pngwing.com.png'))
        self.fire.hide()   


        self.dateEdit = QtWidgets.QPushButton(self)
        self.dateEdit.show()
        self.dateEdit.move(760, 136)


        self.weather_text = QtWidgets.QPushButton(self)
        self.weather_text.setText("Данные")
        self.weather_text.move(135, 310)

        self.weather_text.adjustSize()
        self.weather_text.setStyleSheet("color: rgb(0, 0, 0); font-size: 18px;")
        self.weather_text.hide()

        self.btn_weather = QtWidgets.QPushButton(self)
        self.btn_weather.show()
        self.btn_weather.setText("Получить данные")
        self.btn_weather.setFixedWidth(200)
        self.btn_weather.move(720, 170)
        self.btn_weather.clicked.connect(self.data_of_weather)

    def data_date(self) -> None:
        scrnipt_1.run_1()
        self.flag = 1
        self.hidden_text()

    def week(self) -> None:
        scrnipt_3.run_3()
        self.flag = 2
        self.hidden_text()

    def year(self) -> None:
        scrnipt_2.run_2()
        self.flag = 3
        self.hidden_text()

    def data_of_weather(self) -> None:
        text = ""
        self.fire.show()
        self.weather_text.show()
        if self.flag == 1:
            text = scrnipt_4.work_1(
                scrnipt_4.work_0(self.dateEdit.dateTime().toString("dd-MM-yyyy"))
            )
        else:
            if self.flag == 2:
                text = scrnipt_4.work_3(
                    scrnipt_4.work_0(
                        self.dateEdit.dateTime().toString("dd-MM-yyyy")
                    )
                )
            else:
                text = scrnipt_4.work_2(
                    scrnipt_4.work_0(
                        self.dateEdit.dateTime().toString("dd-MM-yyyy")
                    )
                )
        self.weather_text.setText(text)
       # self.weather_text.move(515, 230)
        self.weather_text.setFixedWidth(400)



    """def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()"""

    """def get_directory(self):
        way = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")  
        print(way)    
        return way"""  


def application():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
