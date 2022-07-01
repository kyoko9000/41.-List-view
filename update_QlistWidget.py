# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        list = ["1", "23", "df", "sdf", "asdf", "sdfwer", "dfsf", "23", "df", "sdf"]
        for i in range(len(list)):
            self.text = QListWidgetItem(list[i])
            self.uic.listWidget.addItem(self.text)

        self.uic.listWidget.scrollToBottom()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
