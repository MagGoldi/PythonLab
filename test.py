import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication

class Guitar_2(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(250, 55, 1200, 800)
        self.setWindowTitle('Гитара')

        self.First_button = QPushButton('Первая струна(клавиша 1)', self)
        self.First_button.resize(170, 50)
        self.First_button.move(40, 100)

class Guitar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(250, 55, 1200, 800)
        self.setWindowTitle('Гитара')

        self.First_button = QPushButton('Первая струна(клавиша 1)', self)
        self.First_button.resize(170, 50)
        self.First_button.move(40, 100)
        self.First_button.clicked.connect(self.show_window_2)

    def show_window_2(self):
        self.w2 = Guitar_2()
        self.w2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Guitar()
    ex.show()
    sys.exit(app.exec_())