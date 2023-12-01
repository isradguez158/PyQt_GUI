#importing libraries 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPalette
from pyqtgraph import PlotWidget
import numpy as np
from random import randint
import time
import math
#creating the main gui window 
start = time.time()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GUI")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label1 =  QtWidgets.QLabel(MainWindow)
        self.label1.setText("<font color=red><font size=24> Isra GUI </font>")
        self.label1.setAutoFillBackground(True)
        self.label1.setGeometry(QtCore.QRect(450, 20, 500, 100))

        self.label2 =  QtWidgets.QLabel(MainWindow)
        self.label2.setText("<font color=blue><font size=24> Plot 1 </font>")
        self.label2.setAutoFillBackground(True)
        self.label2.setGeometry(QtCore.QRect(20, 100, 300, 80))

        self.label3 = QtWidgets.QLabel(MainWindow)
        self.label3.setText("<font color=blue><font size=24> Plot 2 </font>")
        self.label3.setAutoFillBackground(True)
        self.label3.setGeometry(QtCore.QRect(550, 100, 300, 80))

        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 200, 500, 500))
        self.graphicsView.setBackground('white')
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView2 = PlotWidget(self.centralwidget)
        self.graphicsView2.setGeometry(QtCore.QRect(550, 200, 500, 500))
        self.graphicsView2.setBackground('white')
        self.graphicsView2.setObjectName("graphicsView")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(250, 800, 700, 70))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.pushButton = QtWidgets.QPushButton(self.splitter)
        #self.pushButton.setGeometry(550, 500, 50, 50) 

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)

        '''
        button = QtWidgets.QPushButton('PyQt5 button', self.centralwidget)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.setGeometry(550, 500, 50, 50) 
        '''


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
        self.sample=30
        self.x = []
        self.x = [0 for i in range(self.sample)] 
        self.y = []
        self.y = [0 for i in range(self.sample)] 
        self.data_line = []
        self.data_line = [0 for i in range(self.sample)] 

        self.y2 = []
        self.y2 = [0 for i in range(self.sample)] 
        self.data_line2 = []
        self.data_line3 = []
        self.data_line2 = []
        self.data_line2 = [0 for i in range(self.sample)] 
        self.data_line3 = []
        self.data_line3 = [0 for i in range(self.sample)] 


        self.pushButton.clicked.connect(lambda:self.start())
        self.pushButton_2.clicked.connect(lambda:self.stop())

    # initialising the timers 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50) #msec
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
        self.x= self.x[-self.sample:]   

        self.y2.append(90*math.cos(10*time.time()-start))   
        self.y2= self.y2[-self.sample:]   
        self.data_line2.setData(self.x, self.y2)
        self.data_line3.setData(self.x, self.y)

        self.y.append(50*math.sin(10*time.time()-start))  
        self.y= self.y[-self.sample:]   
        self.data_line.setData(self.x, self.y)


    def reset_vec(self):
        self.x = []
        self.x = [time.time()-start for i in range(self.sample)] 
        self.y = []
        self.y = [0 for i in range(self.sample)] 
        self.data_line = []
        self.data_line = [0 for i in range(self.sample)] 

        self.y2 = []
        self.y2 = [0 for i in range(self.sample)] 
        self.data_line2 = []
        self.data_line3 = []
        self.data_line2 = []
        self.data_line2 = [0 for i in range(self.sample)] 
        self.data_line3 = []
        self.data_line3 = [0 for i in range(self.sample)] 
    def start(self):
        self.stop()
        self.data_line2 = self.graphicsView2.plot(self.x,self.y2, pen={'color':'r', 'width':4})
        self.data_line3 = self.graphicsView2.plot(self.x,self.y, pen={'color':'g', 'width':4})
        self.data_line = self.graphicsView.plot(self.x,self.y, pen={'color':'b', 'width':4})

    def stop(self):
        self.reset_vec()
        self.graphicsView.clear()
        self.graphicsView2.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    

    MainWindow.show()
    t= time.time()
    sys.exit(app.exec_())
    
    while(True):
        t = time.time()
        t_p=0
        if(t-t_p>.01):
            t_p=t
            print(t)


