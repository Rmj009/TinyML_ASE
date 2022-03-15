import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QPushButton,QGridLayout,QLineEdit)
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QFont

# /// https://shengyu7697.github.io/python-pyqt-tutorial/

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('InitForm') #p1db
        self.setGeometry(50, 50, 200, 150)
        self.mylabel = QLabel('note >>>', self)
        # self.mylabel.move(10, 50)
        self.mylabel.setFont(QFont('Arial', 18))
        self.mylabel.setStyleSheet("background-color: yellow")
        self.mylabel.setStyleSheet("background-color: #ffff00");
        self.mylabel.setStyleSheet("background-color: rgb(255,255,0)");

        self.mybutton = QPushButton('Btn', self)
        self.mybutton.move(60, 50)
        self.mybutton.clicked.connect(self.onButtonClick)
        ####################
        gridlayout = QGridLayout()
        self.setLayout(gridlayout)
        # 1 Label
        self.mylabel = QLabel('Modulation:', self)
        gridlayout.addWidget(self.mylabel, 0, 0)
        self.mylineedit = QLineEdit(self)
        gridlayout.addWidget(self.mylineedit, 0, 1)
        # 2 Label
        self.mylabel2 = QLabel('PA:', self)
        gridlayout.addWidget(self.mylabel2, 1, 0)
        self.mylineedit2 = QLineEdit(self)
        # self.mylineedit2.setEchoMode(QLineEdit.Password) ＃打馬賽克
        gridlayout.addWidget(self.mylineedit2, 1, 1)
        # 3 Label
        self.mylabel = QLabel('stablity:', self)
        gridlayout.addWidget(self.mylabel, 2, 0)
        self.mylineedit = QLineEdit(self)
        gridlayout.addWidget(self.mylineedit, 2, 1)




    def onButtonClick(self):
            self.mybutton.setText('btn-clicked !!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())



def QtTellTime():

    now = QDate.currentDate()
    print(now.toString(Qt.ISODate))
    print(now.toString(Qt.DefaultLocaleLongDate))
    datetime = QDateTime.currentDateTime()
    print(datetime.toString())

    time = QTime.currentTime()

    print(time.toString(Qt.DefaultLocaleLongDate))

if __name__ == '__main__':
    QtTellTime()
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
