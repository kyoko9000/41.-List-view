# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(50, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_start.setFont(font)
        self.Button_start.setObjectName("Button_start")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 761, 461))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.Button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.Button_clear.setGeometry(QtCore.QRect(240, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_clear.setFont(font)
        self.Button_clear.setObjectName("Button_clear")
        self.Button_remove = QtWidgets.QPushButton(self.centralwidget)
        self.Button_remove.setGeometry(QtCore.QRect(430, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_remove.setFont(font)
        self.Button_remove.setObjectName("Button_remove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_start.setText(_translate("MainWindow", "Start"))
        self.Button_clear.setText(_translate("MainWindow", "Clear"))
        self.Button_remove.setText(_translate("MainWindow", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())