import sys

from qt_core import *

from gui.windows.ui_main_window import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ = "__main__":