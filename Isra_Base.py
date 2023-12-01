#importing libraries 
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import numpy as np
from random import randint
import time
import math
#creating the main gui window 
start = time.time()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 761, 451))
        self.graphicsView.setObjectName("graphicsView")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 490, 701, 71))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    #initialising the parameters 

        self.x = []
        self.y = []
        self.data_line = []

        self.pushButton.clicked.connect(lambda:self.start())
        self.pushButton_2.clicked.connect(lambda:self.stop ())

    # initialising the timers 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10) #msec
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    # initialising the push buttons
     
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))

    # updating the plot 

    def update_plot(self):
        self.x.append(time.time()-start)
        self.y.append(90*math.sin(10*time.time()-start)) 
        self.x= self.x[-100:]    
        self.y= self.y[-100:]   
        self.data_line.setData(self.x, self.y)

    def start(self):
        self.data_line = self.graphicsView.plot(self.x,self.y)
    def stop(self):
        self.x.clear()
        self.y.clear()
        self.graphicsView.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
