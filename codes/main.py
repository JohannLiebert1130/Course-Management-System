import sys
from PyQt5 import QtWidgets

from loginDialog import Ui_login_dialog
from studentMain import Ui_student_MainWindow


def check_login():
    login_dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    responce = login_dialog.exec_()
    if responce == QtWidgets.QDialog.Accepted:
        return True
    else:
        return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    if check_login():
        student_MainWindow = QtWidgets.QMainWindow()
        ui = Ui_student_MainWindow()
        ui.setupUi(student_MainWindow)
        student_MainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
