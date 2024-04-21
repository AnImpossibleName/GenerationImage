from PyQt6.QtWidgets import QApplication, QMainWindow
from GUI.MainWin import Ui_MainWindow  # 导入由UI文件生成的Python代码


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec())
