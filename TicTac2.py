from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.btnClicked_1)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)
        self.ui.pushButton_9.clicked.connect(self.btnClicked_9)
        self.ui.pushButton_10.clicked.connect(self.btnClicked_10)
    # processing buttons

    def btnClicked_1(self):
        self.ui.pushButton_1.setText('O')

    def btnClicked_2(self):
        self.ui.pushButton_2.setText('O')

    def btnClicked_3(self):
        self.ui.pushButton_3.setText('O')

    def btnClicked_4(self):
        self.ui.pushButton_4.setText('O')

    def btnClicked_5(self):
        self.ui.pushButton_5.setText('O')

    def btnClicked_6(self):
        self.ui.pushButton_6.setText('O')

    def btnClicked_7(self):
        self.ui.pushButton_7.setText('O')

    def btnClicked_8(self):
        self.ui.pushButton_8.setText('O')

    def btnClicked_9(self):
        self.ui.pushButton_9.setText('O')

    def btnClicked_10(self):
        self.ui.pushButton_1.setText(' ')
        self.ui.pushButton_2.setText(' ')
        self.ui.pushButton_3.setText(' ')
        self.ui.pushButton_4.setText(' ')
        self.ui.pushButton_5.setText(' ')
        self.ui.pushButton_6.setText(' ')
        self.ui.pushButton_7.setText(' ')
        self.ui.pushButton_8.setText(' ')
        self.ui.pushButton_9.setText(' ')


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
