from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, user):
        super.__init__()
        self.user = user
