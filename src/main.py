import sys
from PyQt5 import QtWidgets

from UI.adminMain import Ui_admin_MainWindow
from UI.loginDialog import Ui_login_dialog
from UI.studentMain import Ui_student_MainWindow
from UI.teacherMain import Ui_teacher_MainWindow


def check_login():
    login_dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    responce = login_dialog.exec_()
    if responce == QtWidgets.QDialog.Accepted:
        return True, login_dialog.identity_flag
    else:
        return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    is_valid_login, identity = check_login()
    
    if is_valid_login:
        if identity == 0:
            admin_MainWindow = QtWidgets.QMainWindow()
            ui = Ui_admin_MainWindow()
            ui.setupUi(admin_MainWindow)
            admin_MainWindow.show()
        elif identity == 1:
            teacher_MainWindow = QtWidgets.QMainWindow()
            ui = Ui_teacher_MainWindow()
            ui.setupUi(teacher_MainWindow)
            teacher_MainWindow.show()
        elif identity == 2:
            student_MainWindow = QtWidgets.QMainWindow()
            ui = Ui_student_MainWindow()
            ui.setupUi(student_MainWindow)
            student_MainWindow.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
