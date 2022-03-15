import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hello world')
        self.setGeometry(50, 50, 200, 150)


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
