import sys
# pip install pyqt6
from pyexpat import model

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.Button_start.clicked.connect(self.show_list)
        self.uic.Button_clear.clicked.connect(self.show_clear)
        self.uic.Button_remove.clicked.connect(self.show_remove)

    def show_list(self):
        # add row
        self.uic.listWidget.addItem("hello")
        self.uic.listWidget.addItems(["hi", "tom"])
        self.uic.listWidget.insertItems(2, ["tony", "merry"])

    def show_clear(self):
        # clear all row
        self.uic.listWidget.clear()

    def show_remove(self):
        # remove row
        # self.uic.listWidget.takeItem(2)
        self.print_info()

    def print_info(self):
        # change color for row
        item = QListWidgetItem("hello")
        item.setForeground(QColor(0, 255, 0))
        item.setBackground(QColor(255, 0, 0))
        self.uic.listWidget.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
