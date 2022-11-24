from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication

class Guitar_2(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(250, 55, 1200, 800)
        self.setWindowTitle('Гитара')

        self.First_button = QPushButton('Первая струна(клавиша 1)', self)
        self.First_button.resize(170, 50)
        self.First_button.move(40, 100)

        self.Second_button = QPushButton('Вторая струна(клавиша 2)', self)
        self.Second_button.resize(170, 50)
        self.Second_button.move(40, 200)