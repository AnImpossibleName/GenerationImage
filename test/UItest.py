from PyQt6.QtWidgets import QApplication, QMainWindow
from GUI.LoginUI import Ui_login  # 导入由UI文件生成的Python代码


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())
