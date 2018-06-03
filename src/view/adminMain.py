# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import datetime

import pymysql
from PyQt5 import QtCore, QtWidgets

from src.common.database import Database
from src.model.accounts.account import Account
from src.model.courses.course import Course
from src.model.students.student import Student
from src.model.teachers.teacher import Teacher


def create_year_generator():
    now = datetime.datetime.now()
    count = now.year - 2010
    for i in range(count+1):
        yield f'{2010+i}-{2010+i+1}'


class Ui_admin_MainWindow(object):
    def setupUi(self, admin_MainWindow):
        self.admin_MainWindow = admin_MainWindow
        self.admin_MainWindow.resize(1368, 768)
        self.admin_MainWindow.setWindowTitle("Course Management System")

        self.centralwidget = QtWidgets.QWidget(admin_MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label.setText(f'Welcome, {self.admin_MainWindow.user.user_id} {self.admin_MainWindow.user.name}')
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)

        self.logout_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_button.sizePolicy().hasHeightForWidth())
        self.logout_button.setSizePolicy(sizePolicy)
        self.logout_button.setMaximumSize(QtCore.QSize(85, 16777215))
        self.logout_button.setIconSize(QtCore.QSize(20, 20))
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.home_tab = QtWidgets.QWidget()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.home_tab)

        self.welcome_label = QtWidgets.QLabel(self.home_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.welcome_label.sizePolicy().hasHeightForWidth())
        self.welcome_label.setSizePolicy(sizePolicy)
        self.welcome_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.welcome_label.setText(f'Welcome, {self.admin_MainWindow.user.user_id} {self.admin_MainWindow.user.name}')

        self.verticalLayout_3.addWidget(self.welcome_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.last_login_label = QtWidgets.QLabel(self.home_tab)
        self.last_login_label.setStyleSheet("font: 12pt \"Sans Serif\";\n"
                                            "margin-right: 10px;")
        self.verticalLayout_3.addWidget(self.last_login_label, 0, QtCore.Qt.AlignRight)
        self.tab_widget.addTab(self.home_tab, "")
        self.course_tab = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.course_tab)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_6 = QtWidgets.QLabel(self.course_tab)
        self.label_6.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.horizontalLayout_2.addWidget(self.label_6)

        self.course_school_comboBox = QtWidgets.QComboBox(self.course_tab)
        self.course_school_comboBox.setEnabled(False)
        self.course_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.course_school_comboBox.addItem(admin_MainWindow.user.school)
        self.horizontalLayout_2.addWidget(self.course_school_comboBox)

        self.label_24 = QtWidgets.QLabel(self.course_tab)
        self.label_24.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.horizontalLayout_2.addWidget(self.label_24)

        self.course_year_comboBox = QtWidgets.QComboBox(self.course_tab)
        self.course_year_comboBox.setEnabled(True)
        self.course_year_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")

        years = create_year_generator()
        for year in years:
            self.course_year_comboBox.addItem(year)

        self.horizontalLayout_2.addWidget(self.course_year_comboBox)
        self.label_23 = QtWidgets.QLabel(self.course_tab)
        self.label_23.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.horizontalLayout_2.addWidget(self.label_23)

        self.course_semester_comboBox = QtWidgets.QComboBox(self.course_tab)
        self.course_semester_comboBox.setEnabled(True)
        self.course_semester_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_semester_comboBox.addItem("")
        self.course_semester_comboBox.addItem("1")
        self.course_semester_comboBox.addItem("2")
        self.horizontalLayout_2.addWidget(self.course_semester_comboBox)

        self.course_id_lineEdit = QtWidgets.QLineEdit(self.course_tab)
        self.course_id_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.horizontalLayout_2.addWidget(self.course_id_lineEdit)
        self.course_name_lineEdit = QtWidgets.QLineEdit(self.course_tab)
        self.course_name_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout_2.addWidget(self.course_name_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.course_tab)
        self.label_5.setText("")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.teacher_lineEdit = QtWidgets.QLineEdit(self.course_tab)
        self.teacher_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout_2.addWidget(self.teacher_lineEdit)

        self.course_query_button = QtWidgets.QPushButton(self.course_tab)
        self.course_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")

        self.course_query_button.clicked.connect(
            lambda: self.init_table(table=self.course_tableWidget,
                                    type_str='course',
                                    data=Course.read_courses(self.admin_MainWindow.user.school),
                                    school_pos=2
                                    )
        )

        self.horizontalLayout_2.addWidget(self.course_query_button)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.course_tableWidget = QtWidgets.QTableWidget(self.course_tab)
        self.course_tableWidget.setColumnCount(10)
        self.course_tableWidget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.course_tableWidget.setItem(0, 2, item)

        self.course_tableWidget.setHorizontalHeaderLabels(['Course ID', 'Course Name', 'School', 'Teacher Name',
                                                           'Class Time', 'Location', 'Year', 'Semester', '', ''])

        self.verticalLayout_2.addWidget(self.course_tableWidget)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.print_course_button = QtWidgets.QPushButton(self.course_tab)
        self.print_course_button.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.horizontalLayout_3.addWidget(self.print_course_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tab_widget.addTab(self.course_tab, "")
        self.enroll_tab = QtWidgets.QWidget()
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.enroll_tab)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_11 = QtWidgets.QLabel(self.enroll_tab)
        self.label_11.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.horizontalLayout_4.addWidget(self.label_11)

        self.confirm_school_comboBox = QtWidgets.QComboBox(self.enroll_tab)
        self.confirm_school_comboBox.setEnabled(False)
        self.confirm_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.confirm_school_comboBox.addItem(self.admin_MainWindow.user.school)
        self.horizontalLayout_4.addWidget(self.confirm_school_comboBox)

        self.label_27 = QtWidgets.QLabel(self.enroll_tab)
        self.label_27.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27)

        self.confrim_year_comboBox = QtWidgets.QComboBox(self.enroll_tab)
        self.confrim_year_comboBox.setEnabled(False)
        self.confrim_year_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")

        current_year = datetime.datetime.now().year
        year = f'{current_year}-{current_year+1}'
        self.confrim_year_comboBox.addItem(year)
        self.horizontalLayout_4.addWidget(self.confrim_year_comboBox)

        self.label_28 = QtWidgets.QLabel(self.enroll_tab)
        self.label_28.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_4.addWidget(self.label_28)

        self.confirm_semester_comboBox = QtWidgets.QComboBox(self.enroll_tab)
        self.confirm_semester_comboBox.setEnabled(False)
        self.confirm_semester_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.confirm_semester_comboBox.setObjectName("confirm_semester_comboBox")
        self.confirm_semester_comboBox.addItem("1")
        self.horizontalLayout_4.addWidget(self.confirm_semester_comboBox)

        self.label_12 = QtWidgets.QLabel(self.enroll_tab)
        self.label_12.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.confirm_course_comboBox = QtWidgets.QComboBox(self.enroll_tab)
        self.confirm_course_comboBox.setObjectName("confirm_course_comboBox")
        self.horizontalLayout_4.addWidget(self.confirm_course_comboBox)

        self.confirm_query_button = QtWidgets.QPushButton('Query', self.enroll_tab)
        self.confirm_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.confirm_query_button.setObjectName("confirm_query_button")
        self.horizontalLayout_4.addWidget(self.confirm_query_button)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.confirm_tableWidget = QtWidgets.QTableWidget(self.enroll_tab)
        self.confirm_tableWidget.setObjectName("confirm_tableWidget")
        self.confirm_tableWidget.setColumnCount(5)
        self.confirm_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.confirm_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.confirm_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.confirm_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.confirm_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.confirm_tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.confirm_tableWidget)
        self.confirm_button = QtWidgets.QPushButton(self.enroll_tab)
        self.confirm_button.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.confirm_button.setObjectName("confirm_button")
        self.verticalLayout_4.addWidget(self.confirm_button, 0, QtCore.Qt.AlignHCenter)
        self.tab_widget.addTab(self.enroll_tab, "")
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

        self.teacher_school_comboBox = QtWidgets.QComboBox(self.teacher_tab)
        self.teacher_school_comboBox.setEnabled(False)
        self.teacher_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.teacher_school_comboBox.setObjectName("teacher_school_comboBox")
        self.teacher_school_comboBox.addItem(self.admin_MainWindow.user.school)
        self.horizontalLayout_6.addWidget(self.teacher_school_comboBox)

        self.teacher_id_lineEdit = QtWidgets.QLineEdit(self.teacher_tab)
        self.teacher_id_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.teacher_id_lineEdit)
        self.teacher_name_lineEdit = QtWidgets.QLineEdit(self.teacher_tab)
        self.teacher_name_lineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.horizontalLayout_6.addWidget(self.teacher_name_lineEdit)

        self.position_lineEdit = QtWidgets.QLineEdit(self.teacher_tab)
        self.position_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.position_lineEdit.setObjectName("position_lineEdit")
        self.horizontalLayout_6.addWidget(self.position_lineEdit)

        self.teacher_query_button = QtWidgets.QPushButton(self.teacher_tab)
        self.teacher_query_button.setStyleSheet("font: 12pt \"Sans Serif\";")

        self.teacher_query_button.clicked.connect(
            lambda: self.init_table(table=self.teacher_tableWidget,
                                    type_str='teacher',
                                    data=Teacher.read_teachers(self.admin_MainWindow.user.school),
                                    school_pos=8
                                    )
        )
        self.horizontalLayout_6.addWidget(self.teacher_query_button)

        self.label_4 = QtWidgets.QLabel(self.teacher_tab)
        self.horizontalLayout_6.addWidget(self.label_4)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.teacher_tableWidget = QtWidgets.QTableWidget(self.teacher_tab)
        self.teacher_tableWidget.setColumnCount(13)
        self.teacher_tableWidget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.teacher_tableWidget.setItem(0, 8, item)

        self.teacher_tableWidget.setHorizontalHeaderLabels(['Teacher ID', 'Teacher Name', 'ID', 'Gender',
                                                             'Birthday', 'Birth Place', 'Folk', 'Political Status',
                                                             'School', 'Position', 'Phone', '', ''])
        self.verticalLayout_7.addWidget(self.teacher_tableWidget)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.teacher_print_button = QtWidgets.QPushButton(self.teacher_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teacher_print_button.sizePolicy().hasHeightForWidth())
        self.teacher_print_button.setSizePolicy(sizePolicy)
        self.teacher_print_button.setMinimumSize(QtCore.QSize(150, 0))
        self.teacher_print_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.teacher_print_button.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.teacher_print_button.setObjectName("teacher_print_button")
        self.horizontalLayout_5.addWidget(self.teacher_print_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)

        self.auto_gen_teacher_button = QtWidgets.QPushButton('Auto-Generate Accounts', self.teacher_tab)
        self.auto_gen_teacher_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.auto_gen_teacher_button.clicked.connect(self.generate_all_teachers)
        self.horizontalLayout_5.addWidget(self.auto_gen_teacher_button)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tab_widget.addTab(self.teacher_tab, "")
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

        self.student_school_comboBox = QtWidgets.QComboBox(self.student_tab)
        self.student_school_comboBox.setEnabled(False)
        self.student_school_comboBox.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.student_school_comboBox.setObjectName("student_school_comboBox")
        self.student_school_comboBox.addItem(self.admin_MainWindow.user.school)
        self.horizontalLayout_9.addWidget(self.student_school_comboBox)

        self.major_lineEdit = QtWidgets.QLineEdit(self.student_tab)
        self.major_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.major_lineEdit.setObjectName("major_lineEdit")
        self.horizontalLayout_9.addWidget(self.major_lineEdit)
        self.class_lineEdit = QtWidgets.QLineEdit(self.student_tab)
        self.class_lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.class_lineEdit.setObjectName("class_lineEdit")
        self.horizontalLayout_9.addWidget(self.class_lineEdit)
        self.student_id_lineEdit = QtWidgets.QLineEdit(self.student_tab)
        self.student_id_lineEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.student_id_lineEdit.setObjectName("student_id_lineEdit")
        self.horizontalLayout_9.addWidget(self.student_id_lineEdit)
        self.student_name_lineEdit = QtWidgets.QLineEdit(self.student_tab)
        self.student_name_lineEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.student_name_lineEdit.setObjectName("student_name_lineEdit")
        self.horizontalLayout_9.addWidget(self.student_name_lineEdit)

        self.student_query_button = QtWidgets.QPushButton(self.student_tab)
        self.student_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")

        self.student_query_button.clicked.connect(
            lambda: self.init_table(table=self.student_tableWidget,
                                    type_str='student',
                                    data=Student.read_students(self.admin_MainWindow.user.school),
                                    school_pos=8
                                    )
        )
        self.horizontalLayout_9.addWidget(self.student_query_button)

        self.label_7 = QtWidgets.QLabel(self.student_tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.student_tableWidget = QtWidgets.QTableWidget(self.student_tab)
        self.student_tableWidget.setColumnCount(14)
        self.student_tableWidget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.student_tableWidget.setItem(0, 8, item)

        self.student_tableWidget.setHorizontalHeaderLabels(['Student ID', 'Student Name', 'ID', 'Gender',
                                                            'Birthday', 'Birth Place', 'Folk', 'Political Status',
                                                            'School', 'Department', 'Class', 'Phone',
                                                            '', ''])
        self.verticalLayout_8.addWidget(self.student_tableWidget)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.student_print_button = QtWidgets.QPushButton(self.student_tab)
        self.student_print_button.setMinimumSize(QtCore.QSize(150, 0))
        self.student_print_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.student_print_button.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.student_print_button.setObjectName("student_print_button")
        self.horizontalLayout_7.addWidget(self.student_print_button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)

        self.auto_gen_student_button = QtWidgets.QPushButton(self.student_tab)
        self.auto_gen_student_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.auto_gen_student_button.setObjectName("auto_gen_student_button")
        self.auto_gen_student_button.clicked.connect(self.generate_all_students)
        self.horizontalLayout_7.addWidget(self.auto_gen_student_button)

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.tab_widget.addTab(self.student_tab, "")
        self.grade_tab = QtWidgets.QWidget()
        self.grade_tab.setObjectName("grade_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.grade_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.grade_tab)
        self.label_2.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.grade_comboBox = QtWidgets.QComboBox(self.grade_tab)
        self.grade_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.grade_comboBox.setObjectName("grade_comboBox")
        self.grade_comboBox.addItem("")
        self.grade_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.grade_comboBox)
        self.grade_lineEdit = QtWidgets.QLineEdit(self.grade_tab)
        self.grade_lineEdit.setMaximumSize(QtCore.QSize(140, 16777215))
        self.grade_lineEdit.setStyleSheet("")
        self.grade_lineEdit.setText("")
        self.grade_lineEdit.setObjectName("grade_lineEdit")
        self.horizontalLayout_8.addWidget(self.grade_lineEdit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)

        self.grade_query_button = QtWidgets.QPushButton(self.grade_tab)
        self.grade_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.grade_query_button.setObjectName("grade_query_button")
        self.horizontalLayout_8.addWidget(self.grade_query_button)

        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.grade_tableWidget = QtWidgets.QTableWidget(self.grade_tab)
        self.grade_tableWidget.setObjectName("grade_tableWidget")
        self.grade_tableWidget.setColumnCount(4)
        self.grade_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_5.addWidget(self.grade_tableWidget)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.pushButton = QtWidgets.QPushButton(self.grade_tab)
        self.pushButton.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.pushButton_2 = QtWidgets.QPushButton(self.grade_tab)
        self.pushButton_2.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.tab_widget.addTab(self.grade_tab, "")
        self.account_tab = QtWidgets.QWidget()
        self.account_tab.setObjectName("account_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.account_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.account_tab)
        self.label_3.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.account_type_comboBox = QtWidgets.QComboBox(self.account_tab)
        self.account_type_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.account_type_comboBox.setObjectName("account_type_comboBox")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.account_type_comboBox)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)

        self.account_query_button = QtWidgets.QPushButton(self.account_tab)
        self.account_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")

        self.account_query_button.clicked.connect(
            lambda: self.init_table(table=self.account_tableWidget,
                                    type_str='account',
                                    data=Account.read_accounts(self.admin_MainWindow.user.school),
                                    school_pos=3
                                    )
        )
        self.horizontalLayout_11.addWidget(self.account_query_button)

        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.account_tableWidget = QtWidgets.QTableWidget(self.account_tab)

        self.account_tableWidget.setColumnCount(6)
        self.account_tableWidget.setRowCount(1)

        self.account_tableWidget.setHorizontalHeaderLabels(['User ID', 'Password', 'User Type', 'School', '', ''])
        self.verticalLayout_6.addWidget(self.account_tableWidget)

        self.tab_widget.addTab(self.account_tab, "")
        self.verticalLayout.addWidget(self.tab_widget)
        admin_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(admin_MainWindow)
        self.statusbar.setObjectName("statusbar")
        admin_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(admin_MainWindow)

    def init_table(self, table, type_str, data, school_pos):
        table.setRowCount(1)
        for entity in data:
            last_row = table.rowCount() - 1
            for i in range(table.columnCount() - 2):
                if entity[i]:
                    item = QtWidgets.QTableWidgetItem(str(entity[i]))
                    if i == school_pos:
                        item.setFlags(QtCore.Qt.ItemIsEditable)
                    table.setItem(last_row, i, item)

            modify_button = QtWidgets.QPushButton("Modify")
            delete_button = QtWidgets.QPushButton("Delete")
            modify_button.clicked.connect(lambda: self.modify(type_str))
            delete_button.clicked.connect(lambda: self.delete(type_str))
            table.setCellWidget(last_row, table.columnCount() - 2, modify_button)
            table.setCellWidget(last_row, table.columnCount() - 1, delete_button)

            table.insertRow(table.rowCount())

        create_button = QtWidgets.QPushButton("Create")
        create_button.clicked.connect(lambda: self.create(type_str))
        table.setCellWidget(table.rowCount() - 1, table.columnCount() - 2, create_button)

        item = QtWidgets.QTableWidgetItem(self.admin_MainWindow.user.school)
        item.setFlags(QtCore.Qt.ItemIsEditable)
        table.setItem(table.rowCount() - 1, school_pos, item)

    def create(self, type_str):
        if type_str == 'teacher':
            table = self.teacher_tableWidget
            create_func = Teacher.create_teacher
            school_pos = 8
        elif type_str == 'student':
            table = self.student_tableWidget
            create_func = Student.create_student
            school_pos = 8
        elif type_str == 'course':
            table = self.course_tableWidget
            create_func = Course.create_course
            school_pos = 2
        else:
            table = self.account_tableWidget
            create_func = Account.create_account
            school_pos = 3

        last_row = table.rowCount() - 1
        column_count = table.columnCount()

        data = list()
        if type_str == 'account':
            for i in range(column_count - 2):
                if table.item(last_row, i) is None or table.item(last_row, i).text() == '':
                    data.append(None)
                else:
                    value = table.item(last_row, i).text()
                    value = int(value) if i == 2 else value
                    data.append(value)
        else:
            for i in range(column_count - 2):
                if table.item(last_row, i) is None or table.item(last_row, i).text() == '':
                    data.append(None)
                else:
                    data.append(table.item(last_row, i).text())

        try:
            Database.initialize()
            print('creating...data:', data)
            create_func(*data)
            Database.close()
        except:
            msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
            msg_box.setWindowTitle('Error')
            msg_box.setText(f'Create {type_str} failed!\nPlease check the information you input')
            msg_box.exec_()
        else:
            self.update_row(table, type_str, school_pos)
            msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
            msg_box.setText(f'Created {type_str} Successfully!')
            msg_box.exec_()

    def update_row(self, table, type_str, school_pos):
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

        modify_button.clicked.connect(lambda: self.modify(type_str))
        delete_button.clicked.connect(lambda: self.delete(type_str))

        table.setCellWidget(row_count - 1, table.columnCount() - 2, modify_button)
        table.setCellWidget(row_count - 1, table.columnCount() - 1, delete_button)

    def modify(self, type_str):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to modify it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            if type_str == 'teacher':
                table = self.teacher_tableWidget
                modify_func = Teacher.modify_teacher
            elif type_str == 'student':
                table = self.student_tableWidget
                modify_func = Student.modify_student
            elif type_str == 'course':
                table = self.course_tableWidget
                modify_func = Course.modify_course
            else:
                table = self.account_tableWidget
                modify_func = Account.modify_account

            current_row = table.currentRow()
            column_count = table.columnCount()
            data = list()
            for i in range(column_count -2):
                if table.item(current_row, i) is None or table.item(current_row, i).text() == '':
                    data.append(None)
                else:
                    data.append(table.item(current_row, i).text())

            try:
                Database.initialize()
                modify_func(*data)
                Database.close()
            except:
                msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
                msg_box.setText(f'Modify {type_str} failed!\nplease check the information you input')
                msg_box.setWindowTitle('Error')
                msg_box.exec_()
            else:
                msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
                msg_box.setText(f'Modified {type_str} Successfully!')
                msg_box.exec_()

    def delete(self, type_str):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Warning', 'Do you really want to delete it?',
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                        parent=self.admin_MainWindow)
        response = msg_box.exec_()
        if response == QtWidgets.QMessageBox.Yes:
            if type_str == 'teacher':
                table = self.teacher_tableWidget
                delete_func = Teacher.delete_teacher
            elif type_str == 'student':
                table = self.student_tableWidget
                delete_func = Student.delete_student
            elif type_str == 'course':
                table = self.course_tableWidget
                delete_func = Course.delete_course
            else:
                table = self.account_tableWidget
                delete_func = Account.delete_account

            current_row = table.currentRow()
            try:
                delete_func(table.item(current_row, 0).text())
                table.removeRow(current_row)
            except:
                msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
                msg_box.setWindowTitle('Error')
                msg_box.setText(f'Delete {type_str} failed!\nPlease check the information you input')
                msg_box.exec_()
            else:
                msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
                msg_box.setText(f'Deleted {type_str} Successfully!')
                msg_box.exec_()

    def generate_all_teachers(self):
        try:
            teachers_data = Teacher.read_teachers(self.admin_MainWindow.user.school)
            accounts_data = list()
            for teacher_data in teachers_data:
                account_data = list()
                account_data.extend([teacher_data[0], '000000', 1])
                account_data.append(self.admin_MainWindow.user.school)
                accounts_data.append(account_data)

            Account.create_accounts(accounts_data)
        except pymysql.DataError as error:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', str(error),
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        except ValueError as error:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', str(error),
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        else:
            msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
            msg_box.setText('Generated Successfully!')
            msg_box.exec_()

    def generate_all_students(self):
        try:
            students_data = Student.read_students(self.admin_MainWindow.user.school)
            accounts_data = list()
            for student_data in students_data:
                account_data = list()
                account_data.extend([student_data[0], '000000', 2])
                account_data.append(self.admin_MainWindow.user.school)
                accounts_data.append(account_data)

            Account.create_accounts(accounts_data)
        except pymysql.DataError as error:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', str(error),
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        except ValueError as error:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, 'Error', str(error),
                                            parent=self.admin_MainWindow)
            msg_box.exec_()
        else:
            msg_box = QtWidgets.QMessageBox(parent=self.admin_MainWindow)
            msg_box.setText('Generated Successfully!')
            msg_box.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.logout_button.setText(_translate("admin_MainWindow", "Logout"))
        self.last_login_label.setText(_translate("admin_MainWindow", "Last login: 2018-XX-XX 12:00 Location"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.home_tab), _translate("admin_MainWindow", "Home"))
        self.label_6.setText(_translate("admin_MainWindow", "School:"))
        self.course_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))
        self.label_24.setText(_translate("admin_MainWindow", "Year:"))
        self.label_23.setText(_translate("admin_MainWindow", "Semester:"))
        self.course_id_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Course ID"))
        self.course_name_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Course Name"))
        self.teacher_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Teacher"))
        self.course_query_button.setText(_translate("admin_MainWindow", "Query"))

        self.print_course_button.setText(_translate("admin_MainWindow", "Print"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.course_tab),
                                   _translate("admin_MainWindow", "Course Management"))
        self.label_11.setText(_translate("admin_MainWindow", "School:"))
        self.confirm_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))
        self.label_27.setText(_translate("admin_MainWindow", "Year:"))

        self.label_28.setText(_translate("admin_MainWindow", "Semester:"))

        self.label_12.setText(_translate("admin_MainWindow", "Course:"))
        item = self.confirm_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin_MainWindow", "Student Name"))
        item = self.confirm_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin_MainWindow", "Student ID"))
        item = self.confirm_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin_MainWindow", "School"))
        item = self.confirm_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin_MainWindow", "Class"))
        item = self.confirm_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("admin_MainWindow", "Checkbox"))
        self.confirm_button.setText(_translate("admin_MainWindow", "Confrim"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.enroll_tab),
                                   _translate("admin_MainWindow", "Confirm Enrollment"))
        self.label_9.setText(_translate("admin_MainWindow", "School:"))
        self.teacher_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))
        self.teacher_id_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Teacher ID"))
        self.teacher_name_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Teacher Name"))
        self.position_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Position"))
        self.teacher_query_button.setText(_translate("admin_MainWindow", "Qeury"))
        self.label_4.setText(_translate("admin_MainWindow", "留空则不以其为关键词进行查询"))

        __sortingEnabled = self.teacher_tableWidget.isSortingEnabled()
        self.teacher_tableWidget.setSortingEnabled(False)

        self.teacher_tableWidget.setSortingEnabled(__sortingEnabled)
        self.teacher_print_button.setText(_translate("admin_MainWindow", "Print"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.teacher_tab),
                                   _translate("admin_MainWindow", "Teacher Management"))
        self.label_10.setText(_translate("admin_MainWindow", "School:"))
        self.student_school_comboBox.setItemText(0, _translate("admin_MainWindow", "Information"))
        self.major_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Major"))
        self.class_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Class"))
        self.student_id_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Student ID"))
        self.student_name_lineEdit.setPlaceholderText(_translate("admin_MainWindow", "Student Name"))
        self.student_query_button.setText(_translate("admin_MainWindow", "Query"))
        self.label_7.setText(_translate("admin_MainWindow", "留空则不以其为关键词进行查询"))

        self.student_print_button.setText(_translate("admin_MainWindow", "Print"))
        self.auto_gen_student_button.setText(_translate("admin_MainWindow", "Auto-Generate Accounts"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.student_tab),
                                   _translate("admin_MainWindow", "Student Management"))
        self.label_2.setText(_translate("admin_MainWindow", "Query Grades By:"))
        self.grade_comboBox.setItemText(0, _translate("admin_MainWindow", "Course ID"))
        self.grade_comboBox.setItemText(1, _translate("admin_MainWindow", "Student ID"))
        self.grade_query_button.setText(_translate("admin_MainWindow", "Query"))
        item = self.grade_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin_MainWindow", "Student Name"))
        item = self.grade_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin_MainWindow", "Student ID"))
        item = self.grade_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin_MainWindow", "Class"))
        item = self.grade_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin_MainWindow", "Grade"))
        self.pushButton.setText(_translate("admin_MainWindow", "Print"))
        self.pushButton_2.setText(_translate("admin_MainWindow", "Grade Analysis"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.grade_tab),
                                   _translate("admin_MainWindow", "Grade Management"))
        self.label_3.setText(_translate("admin_MainWindow", "Account Type:"))
        self.account_type_comboBox.setItemText(0, _translate("admin_MainWindow", "Admin"))
        self.account_type_comboBox.setItemText(1, _translate("admin_MainWindow", "Teacher"))
        self.account_type_comboBox.setItemText(2, _translate("admin_MainWindow", "Student"))
        self.account_query_button.setText(_translate("admin_MainWindow", "Query"))

        self.tab_widget.setTabText(self.tab_widget.indexOf(self.account_tab),
                                   _translate("admin_MainWindow", "Account Management"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    admin_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_admin_MainWindow()
    ui.setupUi(admin_MainWindow)
    admin_MainWindow.show()
    sys.exit(app.exec_())

