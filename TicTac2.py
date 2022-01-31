from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    buttonStatus_1 = True
    buttonStatus_2 = True
    buttonStatus_3 = True
    buttonStatus_4 = True
    buttonStatus_5 = True
    buttonStatus_6 = True
    buttonStatus_7 = True
    buttonStatus_8 = True
    buttonStatus_9 = True
    step = 0

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
        self.ui.pushButton_Rst.clicked.connect(self.btnClicked_Rst)
    # processing buttons

    def btnClicked_1(self):
        if self.buttonStatus_1: 
            self.ui.pushButton_1.setText('O')
            self.buttonStatus_1 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_2(self):
        if self.buttonStatus_2: 
            self.ui.pushButton_2.setText('O')
            self.buttonStatus_2 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_3(self):
        if self.buttonStatus_3: 
            self.ui.pushButton_3.setText('O')
            self.buttonStatus_3 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_4(self):
        if self.buttonStatus_4: 
            self.ui.pushButton_4.setText('O')
            self.buttonStatus_4 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_5(self):
        if self.buttonStatus_5: 
            self.ui.pushButton_5.setText('O')
            self.buttonStatus_5 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_6(self):
        if self.buttonStatus_6: 
            self.ui.pushButton_6.setText('O')
            self.buttonStatus_6 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_7(self):
        if self.buttonStatus_7: 
            self.ui.pushButton_7.setText('O')
            self.buttonStatus_7 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_8(self):
        if self.buttonStatus_8: 
            self.ui.pushButton_8.setText('O')
            self.buttonStatus_8 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_9(self):
        if self.buttonStatus_9: 
            self.ui.pushButton_9.setText('O')
            self.buttonStatus_9 = False
            self.step += 1
            self.gameLogic()

    def btnClicked_Rst(self):
        for n in range(1,9):
            getattr(self.ui,'pushButton_%s'% n).setText(' ')
        self.buttonStatus_1 = True
        self.buttonStatus_2 = True
        self.buttonStatus_3 = True
        self.buttonStatus_4 = True
        self.buttonStatus_5 = True
        self.buttonStatus_6 = True
        self.buttonStatus_7 = True
        self.buttonStatus_8 = True
        self.buttonStatus_9 = True
        self.step = 0
    
    def gameLogic(self):
        match self.step:
            case 1:
                if self.buttonStatus_4:
                    self.ui.pushButton_4.setText('X')
                    self.buttonStatus_4 = False
                else:
                    self.ui.pushButton_1.setText('X')
                    self.buttonStatus_1 = False
            case 2:
                if not self.buttonStatus_2:
                    self.ui.pushButton_7.setText('X')
                    self.buttonStatus_7 = False
                if not self.buttonStatus_5:
                    self.ui.pushButton_6.setText('X')
                    self.buttonStatus_6 = False
                if not self.buttonStatus_7:
                    self.ui.pushButton_2.setText('X')
                    self.buttonStatus_2 = False
                if not self.buttonStatus_6:
                    self.ui.pushButton_5.setText('X')
                    self.buttonStatus_5 = False
        self.step +=1


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
