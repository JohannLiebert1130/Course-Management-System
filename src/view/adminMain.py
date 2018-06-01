# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

from src.common.database import Database
from src.model.accounts.account import Account
from src.model.courses.course import Course
from src.model.students.student import Student
from src.model.teachers.teacher import Teacher



class Ui_admin_MainWindow(object):
    def setupUi(self, admin_MainWindow):
        self.admin_MainWindow = admin_MainWindow
        admin_MainWindow.setObjectName("admin_MainWindow")
        admin_MainWindow.resize(1368, 768)
        self.centralwidget = QtWidgets.QWidget(admin_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.logout_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_button.sizePolicy().hasHeightForWidth())
        self.logout_button.setSizePolicy(sizePolicy)
        self.logout_button.setMaximumSize(QtCore.QSize(85, 16777215))
        self.logout_button.setStyleSheet("")
        self.logout_button.setIconSize(QtCore.QSize(20, 20))
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.home_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.welcome_label = QtWidgets.QLabel(self.home_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.welcome_label.sizePolicy().hasHeightForWidth())
        self.welcome_label.setSizePolicy(sizePolicy)
        self.welcome_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout_3.addWidget(self.welcome_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.last_login_label = QtWidgets.QLabel(self.home_tab)
        self.last_login_label.setStyleSheet("font: 12pt \"Sans Serif\";\n"
                                            "margin-right: 10px;")
        self.last_login_label.setObjectName("last_login_label")
        self.verticalLayout_3.addWidget(self.last_login_label, 0, QtCore.Qt.AlignRight)
        self.tabWidget.addTab(self.home_tab, "")
        self.course_tab = QtWidgets.QWidget()
        self.course_tab.setObjectName("course_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.course_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.course_tab)
        self.label_6.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)

        self.course_management_school_comboBox = QtWidgets.QComboBox(self.course_tab)
        self.course_management_school_comboBox.setEnabled(False)
        self.course_management_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.course_management_school_comboBox.setObjectName("modify_course_school_comboBox")
        self.course_management_school_comboBox.addItem(admin_MainWindow.user.school)

        self.horizontalLayout_2.addWidget(self.course_management_school_comboBox)

        self.label_24 = QtWidgets.QLabel(self.course_tab)
        self.label_24.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_2.addWidget(self.label_24)
        self.course_year_comboBox = QtWidgets.QComboBox(self.course_tab)
        self.course_year_comboBox.setEnabled(True)
        self.course_year_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_year_comboBox.addItem("2015-2016")
        self.course_year_comboBox.addItem("2016-2017")
        self.horizontalLayout_2.addWidget(self.course_year_comboBox)
        self.label_23 = QtWidgets.QLabel(self.course_tab)
        self.label_23.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_2.addWidget(self.label_23)
        self.course_semester_comboBox = QtWidgets.QComboBox(self.course_tab)
        self.course_semester_comboBox.setEnabled(True)
        self.course_semester_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_semester_comboBox.addItem("1")
        self.course_semester_comboBox.addItem("2")
        self.horizontalLayout_2.addWidget(self.course_semester_comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.course_table_widget = QtWidgets.QTableWidget(self.course_tab)
        self.course_table_widget.setObjectName("course_table_widget")

        self.course_table_widget.setColumnCount(10)
        self.course_table_widget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.course_table_widget.setItem(0, 2, item)

        self.course_table_widget.setHorizontalHeaderLabels(['Course ID', 'Course Name', 'School', 'Teacher Name',
                                                            'Class Time', 'Location', 'Year', 'Semester', '', ''])

        self.verticalLayout_2.addWidget(self.course_table_widget)

        courses_data = Course.read_courses(self.admin_MainWindow.user.school)

        actions = [self.modify_course, self.delete_course, self.create_new_course]

        course_info = [self.course_table_widget, courses_data, 2, actions]

        self.init_table(*course_info)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.course_tab)
        self.pushButton_3.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.course_tab)
        self.pushButton_4.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.course_tab, "")
        self.enroll_tab = QtWidgets.QWidget()
        self.enroll_tab.setObjectName("enroll_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.enroll_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.enroll_tab)
        self.label_11.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)

        self.confirm_tab_school_comboBox = QtWidgets.QComboBox(self.enroll_tab)
        self.confirm_tab_school_comboBox.setEnabled(False)
        self.confirm_tab_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.confirm_tab_school_comboBox.addItem(admin_MainWindow.user.school)
        self.horizontalLayout_4.addWidget(self.confirm_tab_school_comboBox)

        self.label_27 = QtWidgets.QLabel(self.enroll_tab)
        self.label_27.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27)
        self.comboBox_14 = QtWidgets.QComboBox(self.enroll_tab)
        self.comboBox_14.setEnabled(False)
        self.comboBox_14.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_14)
        self.label_28 = QtWidgets.QLabel(self.enroll_tab)
        self.label_28.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_4.addWidget(self.label_28)
        self.comboBox_15 = QtWidgets.QComboBox(self.enroll_tab)
        self.comboBox_15.setEnabled(False)
        self.comboBox_15.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_15)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.enroll_tab)
        self.label_12.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.comboBox_5 = QtWidgets.QComboBox(self.enroll_tab)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_10.addWidget(self.comboBox_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.enroll_tab)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.tableWidget_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.enroll_tab)
        self.pushButton_7.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.enroll_tab, "")
        self.teacher_tab = QtWidgets.QWidget()
        self.teacher_tab.setObjectName("teacher_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.teacher_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.teacher_tab)
        self.label_9.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)

        self.teacher_tab_school_comboBox = QtWidgets.QComboBox(self.teacher_tab)
        self.teacher_tab_school_comboBox.setEnabled(False)
        self.teacher_tab_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.teacher_tab_school_comboBox.addItem(admin_MainWindow.user.school)
        self.horizontalLayout_6.addWidget(self.teacher_tab_school_comboBox)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.teacher_table_widget = QtWidgets.QTableWidget(self.teacher_tab)
        self.teacher_table_widget.setObjectName("teacher_table_widget")

        self.teacher_table_widget.setColumnCount(13)
        self.teacher_table_widget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.teacher_table_widget.setItem(0, 8, item)

        self.teacher_table_widget.setHorizontalHeaderLabels(['Teacher ID', 'Teacher Name', 'ID', 'Gender',
                                                             'Birthday', 'Birth Place', 'Folk', 'Political Status',
                                                             'School', 'Position', 'Phone', '', ''])

        self.verticalLayout_7.addWidget(self.teacher_table_widget)

        teachers_data = Teacher.read_teachers(self.admin_MainWindow.user.school)

        actions = [self.modify_teacher, self.delete_teacher, self.create_new_teacher]

        teachers_info = [self.teacher_table_widget, teachers_data, 8, actions]

        self.init_table(*teachers_info)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(self.teacher_tab)
        self.pushButton.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.pushButton_5 = QtWidgets.QPushButton(self.teacher_tab)
        self.pushButton_5.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.teacher_tab, "")
        self.student_tab = QtWidgets.QWidget()
        self.student_tab.setObjectName("student_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.student_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.student_tab)
        self.label_10.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)

        self.student_tab_school_comboBox = QtWidgets.QComboBox(self.student_tab)
        self.student_tab_school_comboBox.setEnabled(False)
        self.student_tab_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.student_tab_school_comboBox.addItem(admin_MainWindow.user.school)
        self.horizontalLayout_9.addWidget(self.student_tab_school_comboBox)

        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.student_table_widget = QtWidgets.QTableWidget(self.student_tab)
        self.student_table_widget.setObjectName("student_table_widget")

        self.student_table_widget.setColumnCount(14)
        self.student_table_widget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.student_table_widget.setItem(0, 8, item)

        self.student_table_widget.setHorizontalHeaderLabels(['Student ID', 'Student Name', 'ID', 'Gender',
                                                             'Birthday', 'Birth Place', 'Folk', 'Political Status',
                                                             'School', 'Department', 'Class', 'Phone',
                                                             '', ''])

        self.verticalLayout_8.addWidget(self.student_table_widget)

        self.verticalLayout_7.addWidget(self.teacher_table_widget)

        students_data = Student.read_students(self.admin_MainWindow.user.school)

        actions = [self.modify_student, self.delete_student, self.create_new_student]

        students_info = [self.student_table_widget, students_data, 8, actions]

        self.init_table(*students_info)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.pushButton_2 = QtWidgets.QPushButton(self.student_tab)
        self.pushButton_2.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.pushButton_6 = QtWidgets.QPushButton(self.student_tab)
        self.pushButton_6.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.student_tab, "")
        self.grade_tab = QtWidgets.QWidget()
        self.grade_tab.setObjectName("grade_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.grade_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.label_2 = QtWidgets.QLabel(self.grade_tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.grade_tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.pushButton_8 = QtWidgets.QPushButton(self.grade_tab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.grade_tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.pushButton_9 = QtWidgets.QPushButton(self.grade_tab)
        self.pushButton_9.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.grade_tab, "")
        self.account_tab = QtWidgets.QWidget()
        self.account_tab.setObjectName("account_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.account_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.account_tab)
        self.label_3.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.account_tab)
        self.comboBox_2.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.account_tableWidget = QtWidgets.QTableWidget(self.account_tab)

        self.account_tableWidget.setColumnCount(6)
        self.account_tableWidget.setRowCount(1)

        self.account_tableWidget.setHorizontalHeaderLabels(['User ID', 'Password', 'User Type', 'School', '', ''])

        self.verticalLayout_6.addWidget(self.account_tableWidget)

        accounts_data = Account.read_accounts(self.admin_MainWindow.user.school)

        actions = [self.modify_account, self.delete_account, self.create_new_account]

        accounts_info = [self.account_tableWidget, accounts_data, 3, actions]

        self.init_table(*accounts_info)

        self.tabWidget.addTab(self.account_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        admin_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(admin_MainWindow)
        self.statusbar.setObjectName("statusbar")
        admin_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(admin_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(admin_MainWindow)

    @staticmethod
    def welcome_info(admin_MainWindow):
        return f'Welcome, {admin_MainWindow.user.user_id} {admin_MainWindow.user.name}'

    def init_table(self, table, data, school_pos, actions):
        for entity in data:
            print(entity)
            last_row = table.rowCount() - 1
            for i in range(table.columnCount() - 2):
                item = QtWidgets.QTableWidgetItem(entity[i])
                if i == school_pos:
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(last_row, i, item)

            modify_button = QtWidgets.QPushButton("Modify")
            delete_button = QtWidgets.QPushButton("Delete")
            modify_button.clicked.connect(actions[0])
            delete_button.clicked.connect(actions[1])
            table.setCellWidget(last_row, table.columnCount() - 2, modify_button)
            table.setCellWidget(last_row, table.columnCount() - 1, delete_button)

            table.insertRow(table.rowCount())

        create_button = QtWidgets.QPushButton("Create")
        create_button.clicked.connect(actions[2])
        table.setCellWidget(table.rowCount() - 1, table.columnCount() - 2, create_button)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        table.setItem(table.rowCount() - 1, school_pos, item)

    def create_new_teacher(self):
        last_row = self.teacher_table_widget.rowCount() - 1

        teacher_data = list()
        for i in range(11):
            if self.teacher_table_widget.item(last_row, i) is None \
                    or self.teacher_table_widget.item(last_row, i).text() == '':
                teacher_data.append(None)
                item = QtWidgets.QTableWidgetItem()
                self.teacher_table_widget.setItem(last_row, i, item)
            else:
                teacher_data.append(self.teacher_table_widget.item(last_row, i).text())
        print(teacher_data)
        try:
            Database.initialize()
            Teacher.create_teacher(*teacher_data)
            Database.close()
        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create teacher failed!\n'
                                                                                     'please check the information you input',
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        else:
            print(self.teacher_table_widget.item(last_row, 2).text())

            self.update_row(self.teacher_table_widget, 8)

    def create_new_student(self):
        last_row = self.student_table_widget.rowCount() - 1

        student_data = list()
        for i in range(12):
            if self.student_table_widget.item(last_row, i) is None \
                    or self.student_table_widget.item(last_row, i).text() == '':
                student_data.append(None)
                item = QtWidgets.QTableWidgetItem()
                self.student_table_widget.setItem(last_row, i, item)
            else:
                student_data.append(self.student_table_widget.item(last_row, i).text())

        print(student_data)
        try:
            Database.initialize()
            Student.create_student(*student_data)
            Database.close()
        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create student failed!\n'
                                                                                     'please check the information you input',
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        else:
            self.update_row(self.student_table_widget, 8)

    def create_new_course(self):
        last_row = self.course_table_widget.rowCount() - 1

        course_data = list()
        for i in range(8):
            if self.course_table_widget.item(last_row, i) is None \
                    or self.course_table_widget.item(last_row, i).text() == '':
                course_data.append(None)
                item = QtWidgets.QTableWidgetItem()
                self.course_table_widget.setItem(last_row, i, item)
            else:
                course_data.append(self.course_table_widget.item(last_row, i).text())

        print(course_data)
        try:
            Database.initialize()
            Course.create_course(*course_data)
            Database.close()
        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create course failed!\n'
                                                                                     'please check the information you input',
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        else:
            self.update_row(self.course_table_widget, 2)

    def create_new_account(self):
        last_row = self.account_tableWidget.rowCount() - 1

        account_data = list()
        for i in range(4):
            if self.account_tableWidget.item(last_row, i) is None \
                    or self.account_tableWidget.item(last_row, i).text() == '':
                account_data.append(None)
                item = QtWidgets.QTableWidgetItem()
                self.account_tableWidget.setItem(last_row, i, item)
            else:
                account_data.append(self.account_tableWidget.item(last_row, i).text())

        print(account_data)
        try:
            Database.initialize()
            Account.create_account(*account_data)
            Database.close()
        except:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create account failed!\n'
                                            'please check the information you input', parent=self.admin_MainWindow)
            msg_box.exec_()
        else:
            self.update_row(self.account_tableWidget, 3)

    def update_row(self, table, school_pos):
        row_count = table.rowCount()
        table.insertRow(row_count - 1)

        for i in range(table.columnCount() - 2):
            text = table.item(row_count, i).text()
            if text and text != '':
                item = QtWidgets.QTableWidgetItem(text)
                if i == school_pos:
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                table.setItem(row_count - 1, i, item)

            table.setItem(row_count, i, None)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        table.setItem(row_count, school_pos, item)

        modify_button = QtWidgets.QPushButton("Modify")
        delete_button = QtWidgets.QPushButton("Delete")
        if table == self.student_table_widget:
            modify_button.clicked.connect(self.modify_student)
            delete_button.clicked.connect(self.delete_student)
        elif table == self.teacher_table_widget:
            modify_button.clicked.connect(self.modify_teacher)
            delete_button.clicked.connect(self.delete_teacher)
        elif table == self.student_table_widget:
            modify_button.clicked.connect(self.modify_course)
            delete_button.clicked.connect(self.delete_course)
        elif table == self.account_tableWidget:
            modify_button.clicked.connect(self.modify_account)
            delete_button.clicked.connect(self.delete_account)

        table.setCellWidget(row_count - 1, table.columnCount() - 2, modify_button)
        table.setCellWidget(row_count - 1, table.columnCount() - 1, delete_button)

    def modify_teacher(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to modify it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.teacher_table_widget.currentRow()
            teacher_data = list()
            for i in range(11):
                if self.teacher_table_widget.item(current_row, i) is None \
                        or self.teacher_table_widget.item(current_row, i).text() == '':
                    teacher_data.append(None)
                else:
                    teacher_data.append(self.teacher_table_widget.item(current_row, i).text())

            try:
                Database.initialize()
                Teacher.modify_teacher(*teacher_data)
                Database.close()
            except ValueError:
                msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create teacher failed!\n'
                                                                                         'please check the information you input',
                                                parent=self.admin_MainWindow)
                msg_box.exec_()

    def modify_course(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to modify it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.course_table_widget.currentRow()
            course_data = list()
            for i in range(11):
                if self.course_table_widget.item(current_row, i) is None \
                        or self.course_table_widget.item(current_row, i).text() == '':
                    course_data.append(None)
                else:
                    course_data.append(self.course_table_widget.item(current_row, i).text())

            try:
                Database.initialize()
                Course.modify_course(*course_data)
                Database.close()
            except ValueError:
                msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create course failed!\n'
                                                'please check the information you input', parent=self.admin_MainWindow)
                msg_box.exec_()

    def modify_student(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to modify it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.student_table_widget.currentRow()
            student_data = list()
            for i in range(11):
                if self.student_table_widget.item(current_row, i) is None \
                        or self.student_table_widget.item(current_row, i).text() == '':
                    student_data.append(None)
                else:
                    student_data.append(self.student_table_widget.item(current_row, i).text())

            try:
                Database.initialize()
                Student.modify_student(*student_data)
                Database.close()
            except ValueError:
                msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create student failed!\n'
                                                                                         'please check the information you input',
                                                parent=self.admin_MainWindow)
                msg_box.exec_()

    def modify_account(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to modify it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.account_tableWidget.currentRow()
            account_data = list()
            for i in range(11):
                if self.account_tableWidget.item(current_row, i) is None \
                        or self.account_tableWidget.item(current_row, i).text() == '':
                    account_data.append(None)
                else:
                    account_data.append(self.account_tableWidget.item(current_row, i).text())

            try:
                Database.initialize()
                Account.modify_account(*account_data)
                Database.close()
            except ValueError:
                msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', 'Create account failed!\n'
                                                'please check the information you input', parent=self.admin_MainWindow)
                msg_box.exec_()

    def delete_teacher(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to delete it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.teacher_table_widget.currentRow()
            Teacher.delete_teacher(self.teacher_table_widget.item(current_row, 0).text())
            self.teacher_table_widget.removeRow(current_row)

    def delete_student(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to delete it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.student_table_widget.currentRow()
            Student.delete_student(self.student_table_widget.item(current_row, 0).text())
            self.student_table_widget.removeRow(current_row)

    def delete_course(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to delete it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.course_table_widget.currentRow()
            Course.delete_course(self.course_table_widget.item(current_row, 0).text())
            self.course_table_widget.removeRow(current_row)

    def delete_account(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to delete it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            current_row = self.account_tableWidget.currentRow()
            Account.delete_account(self.account_tableWidget.item(current_row, 0).text())
            self.account_tableWidget.removeRow(current_row)

    def retranslateUi(self, admin_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        admin_MainWindow.setWindowTitle(_translate("admin_MainWindow", "Course Management System"))
        self.label.setText(_translate("admin_MainWindow", Ui_admin_MainWindow.welcome_info(admin_MainWindow)))
        self.logout_button.setText(_translate("admin_MainWindow", "Logout"))
        self.welcome_label.setText(_translate("admin_MainWindow", Ui_admin_MainWindow.welcome_info(admin_MainWindow)))
        self.last_login_label.setText(_translate("admin_MainWindow", "Last login: 2018-XX-XX 12:00 Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("admin_MainWindow", "Home"))
        self.label_6.setText(_translate("admin_MainWindow", "School:"))
        self.label_24.setText(_translate("admin_MainWindow", "Year:"))
        self.label_23.setText(_translate("admin_MainWindow", "Semester:"))

        self.pushButton_3.setText(_translate("admin_MainWindow", "Course Query"))
        self.pushButton_4.setText(_translate("admin_MainWindow", "Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.course_tab),
                                  _translate("admin_MainWindow", "Course Management"))
        self.label_11.setText(_translate("admin_MainWindow", "School:"))
        self.confirm_tab_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))
        self.label_27.setText(_translate("admin_MainWindow", "Year:"))
        self.comboBox_14.setItemText(0, _translate("admin_MainWindow", "2015-2016"))
        self.comboBox_14.setItemText(1, _translate("admin_MainWindow", "2016-2017"))
        self.label_28.setText(_translate("admin_MainWindow", "Semester:"))
        self.comboBox_15.setItemText(0, _translate("admin_MainWindow", "1"))
        self.comboBox_15.setItemText(1, _translate("admin_MainWindow", "2"))
        self.label_12.setText(_translate("admin_MainWindow", "Course:"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("admin_MainWindow", "Student Name"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("admin_MainWindow", "Student ID"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("admin_MainWindow", "School"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("admin_MainWindow", "Class"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("admin_MainWindow", "Checkbox"))
        self.pushButton_7.setText(_translate("admin_MainWindow", "Confrim"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.enroll_tab),
                                  _translate("admin_MainWindow", "Confirm Enrollment"))
        self.label_9.setText(_translate("admin_MainWindow", "School:"))
        self.teacher_tab_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))

        self.pushButton.setText(_translate("admin_MainWindow", "Teacher Query"))
        self.pushButton_5.setText(_translate("admin_MainWindow", "Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teacher_tab),
                                  _translate("admin_MainWindow", "Teacher Management"))
        self.label_10.setText(_translate("admin_MainWindow", "School:"))
        self.student_tab_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))

        self.pushButton_2.setText(_translate("admin_MainWindow", "Student Query"))
        self.pushButton_6.setText(_translate("admin_MainWindow", "Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.student_tab),
                                  _translate("admin_MainWindow", "Student Management"))
        self.label_2.setText(_translate("admin_MainWindow", "Show Grades By:"))
        self.comboBox.setItemText(0, _translate("admin_MainWindow", "Course ID"))
        self.comboBox.setItemText(1, _translate("admin_MainWindow", "Student ID"))
        self.pushButton_8.setText(_translate("admin_MainWindow", "Show"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin_MainWindow", "Student Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin_MainWindow", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin_MainWindow", "Class"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin_MainWindow", "Grade"))
        self.pushButton_9.setText(_translate("admin_MainWindow", "Grade Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.grade_tab),
                                  _translate("admin_MainWindow", "Grade Management"))
        self.label_3.setText(_translate("admin_MainWindow", "Account Type:"))
        self.comboBox_2.setItemText(0, _translate("admin_MainWindow", "Teacher"))
        self.comboBox_2.setItemText(1, _translate("admin_MainWindow", "Student"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account_tab),
                                  _translate("admin_MainWindow", "Account Management"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    admin_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_admin_MainWindow()
    ui.setupUi(admin_MainWindow)
    admin_MainWindow.show()
    sys.exit(app.exec_())
