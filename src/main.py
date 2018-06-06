import sys
from PyQt5 import QtWidgets

from src.view.adminMain import Ui_admin_MainWindow
from src.view.loginDialog import Ui_login_dialog
from src.view.mainWindow import MainWindow
from src.view.studentMain import Ui_student_MainWindow
from src.view.teacherMain import Ui_teacher_MainWindow


def check_login():
    login_dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    responce = login_dialog.exec_()
    if responce == QtWidgets.QDialog.Accepted:
        return True, login_dialog.user
    else:
        return False, login_dialog.user


def main():
    app = QtWidgets.QApplication(sys.argv)
    is_valid_login, user = check_login()
    
    if is_valid_login:
        if user.user_type == 0:
            admin_MainWindow = MainWindow(user)
            ui = Ui_admin_MainWindow()
            ui.setupUi(admin_MainWindow)
            admin_MainWindow.show()
        elif user.user_type == 1:
            teacher_MainWindow = MainWindow(user)
            ui = Ui_teacher_MainWindow()
            ui.__init__(teacher_MainWindow)
            teacher_MainWindow.show()
        elif user.user_type == 2:
            student_MainWindow = MainWindow(user)
            ui = Ui_student_MainWindow()
            ui.setupUi(student_MainWindow)
            student_MainWindow.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
