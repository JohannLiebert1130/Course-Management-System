# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacherMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

from src.common.database import Database
from src.common.utils import Utils
from src.model.accounts.account import Account
from src.model.courses.course import Course
from src.model.exams.exam import Exam
from src.model.student_courses import get_students_data, save_grade


class Ui_teacher_MainWindow(object):
    def setupUi(self, teacher_MainWindow):
        self.teacher_MainWindow = teacher_MainWindow
        self.teacher_MainWindow.resize(1368, 768)
        self.teacher_MainWindow.setWindowTitle("Course Management System")

        self.school = self.teacher_MainWindow.user.school
        self.teacher_id = self.teacher_MainWindow.user.user_id
        self.teacher_name = self.teacher_MainWindow.user.name

        self.centralwidget = QtWidgets.QWidget(teacher_MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.user_top_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_top_label.sizePolicy().hasHeightForWidth())
        self.user_top_label.setSizePolicy(sizePolicy)
        self.user_top_label.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.user_top_label.setText(f'Welcome, {self.teacher_id} {self.teacher_name}')
        self.horizontalLayout.addWidget(self.user_top_label)

        self.logout_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_button.sizePolicy().hasHeightForWidth())
        self.logout_button.setSizePolicy(sizePolicy)
        self.logout_button.setMaximumSize(QtCore.QSize(85, 16777215))
        self.logout_button.setIconSize(QtCore.QSize(20, 20))
        self.logout_button.setObjectName("logout_button")
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::tab:first { height: 45px;}")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.home_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.welcome_label = QtWidgets.QLabel(self.home_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.welcome_label.sizePolicy().hasHeightForWidth())
        self.welcome_label.setSizePolicy(sizePolicy)
        self.welcome_label.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.welcome_label.setText(f'Welcome, {self.teacher_id} {self.teacher_name}')
        self.verticalLayout_2.addWidget(self.welcome_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.last_login_label = QtWidgets.QLabel(self.home_tab)
        self.last_login_label.setStyleSheet("font: 12pt \"Sans Serif\";\n"
                                            "margin-right: 10px;")
        self.last_login_label.setObjectName("last_login_label")
        self.verticalLayout_2.addWidget(self.last_login_label, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.tabWidget.addTab(self.home_tab, "")
        self.query_tab = QtWidgets.QWidget()
        self.query_tab.setObjectName("query_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.query_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.query_tab)
        self.tabWidget_2.setStyleSheet("QTabBar::tab { height: 45px}")
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.courses_tab = QtWidgets.QWidget()
        self.courses_tab.setObjectName("courses_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.courses_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_21 = QtWidgets.QLabel(self.courses_tab)
        self.label_21.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)

        self.course_year_comboBox = QtWidgets.QComboBox(self.courses_tab)
        self.course_year_comboBox.setEnabled(True)
        self.course_year_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        years = Utils.create_year_generator()
        for year in years:
            self.course_year_comboBox.addItem(year)
        self.horizontalLayout_8.addWidget(self.course_year_comboBox)

        self.label_22 = QtWidgets.QLabel(self.courses_tab)
        self.label_22.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_8.addWidget(self.label_22)

        self.course_semester_comboBox = QtWidgets.QComboBox(self.courses_tab)
        self.course_semester_comboBox.setEnabled(True)
        self.course_semester_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_semester_comboBox.addItem("")
        self.course_semester_comboBox.addItem("1")
        self.course_semester_comboBox.addItem("2")
        self.horizontalLayout_8.addWidget(self.course_semester_comboBox)

        self.label = QtWidgets.QLabel(self.courses_tab)
        self.label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.course_name_comboBox = QtWidgets.QComboBox(self.courses_tab)
        self.course_name_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")

        courses_data = Course.read_courses(self.school, teacher_id=self.teacher_id)
        self.courses_id = list()
        for course_data in courses_data:
            self.course_name_comboBox.addItem(course_data[1])
            self.courses_id.append(course_data[0])

        self.horizontalLayout_8.addWidget(self.course_name_comboBox)

        self.course_query_button = QtWidgets.QPushButton('Query', self.courses_tab)
        self.course_query_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_query_button.clicked.connect(self.init_course_tab)
        self.horizontalLayout_8.addWidget(self.course_query_button)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.line_12 = QtWidgets.QFrame(self.courses_tab)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_3.addWidget(self.line_12)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.course_id_label = QtWidgets.QLabel(self.courses_tab)
        self.course_id_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.course_id_label.setObjectName("course_id_label")
        self.gridLayout_2.addWidget(self.course_id_label, 0, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.courses_tab)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 0, 1, 1, 1)
        self.teacher_label = QtWidgets.QLabel(self.courses_tab)
        self.teacher_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.teacher_label.setObjectName("teacher_label")
        self.gridLayout_2.addWidget(self.teacher_label, 0, 2, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.courses_tab)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 0, 3, 1, 1)
        self.class_time_label = QtWidgets.QLabel(self.courses_tab)
        self.class_time_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.class_time_label.setObjectName("class_time_label")
        self.gridLayout_2.addWidget(self.class_time_label, 0, 4, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.courses_tab)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 1, 0, 2, 3)
        self.line_9 = QtWidgets.QFrame(self.courses_tab)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 1, 4, 1, 1)
        self.school_label = QtWidgets.QLabel(self.courses_tab)
        self.school_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.school_label.setObjectName("school_label")
        self.gridLayout_2.addWidget(self.school_label, 2, 4, 2, 1)
        self.location_label = QtWidgets.QLabel(self.courses_tab)
        self.location_label.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.location_label.setObjectName("location_label")
        self.gridLayout_2.addWidget(self.location_label, 3, 0, 1, 3)
        self.line_11 = QtWidgets.QFrame(self.courses_tab)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_2.addWidget(self.line_11, 3, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.course_tableWidget = QtWidgets.QTableWidget(self.courses_tab)
        self.course_tableWidget.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.course_tableWidget.setObjectName("course_tableWidget")
        self.course_tableWidget.setColumnCount(6)

        self.course_tableWidget.setHorizontalHeaderLabels(['Student Name', 'Student ID', 'School', 'Class',
                                                           'Phone Number', 'Grade'])

        self.verticalLayout_3.addWidget(self.course_tableWidget)

        self.confirm_grade_button = QtWidgets.QPushButton('Confirm Grades', self.courses_tab)
        self.confirm_grade_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.confirm_grade_button.clicked.connect(self.confrim_grades)
        self.verticalLayout_3.addWidget(self.confirm_grade_button, 0, QtCore.Qt.AlignHCenter)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.print_button = QtWidgets.QPushButton(self.courses_tab)
        self.print_button.setMinimumSize(QtCore.QSize(130, 0))
        self.print_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.print_button.setObjectName("print_button")
        self.horizontalLayout_2.addWidget(self.print_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.grade_analysis_button = QtWidgets.QPushButton(self.courses_tab)
        self.grade_analysis_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.grade_analysis_button.setObjectName("grade_analysis_button")
        self.horizontalLayout_2.addWidget(self.grade_analysis_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget_2.addTab(self.courses_tab, "")
        self.exam_tab = QtWidgets.QWidget()
        self.exam_tab.setObjectName("exam_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.exam_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.exam_tab)
        self.label_18.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)

        self.exam_year_comboBox = QtWidgets.QComboBox(self.exam_tab)
        self.exam_year_comboBox.setEnabled(True)
        self.exam_year_comboBox.setStyleSheet("font: 10pt \"Sans Serif\";")

        years = Utils.create_year_generator()
        for year in years:
            self.exam_year_comboBox.addItem(year)

        self.horizontalLayout_6.addWidget(self.exam_year_comboBox)

        self.label_19 = QtWidgets.QLabel(self.exam_tab)
        self.label_19.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)

        self.exam_semester_comboBox = QtWidgets.QComboBox(self.exam_tab)
        self.exam_semester_comboBox.setEnabled(True)
        self.exam_semester_comboBox.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.exam_semester_comboBox.addItem(" ")
        self.exam_semester_comboBox.addItem("1")
        self.exam_semester_comboBox.addItem("2")
        self.horizontalLayout_6.addWidget(self.exam_semester_comboBox)

        self.exam_query_button = QtWidgets.QPushButton('Query', self.exam_tab)
        self.exam_query_button.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.exam_query_button.clicked.connect(self.init_exam_table)
        self.horizontalLayout_6.addWidget(self.exam_query_button)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.exam_tableWidget = QtWidgets.QTableWidget(self.exam_tab)
        self.exam_tableWidget.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.exam_tableWidget.setColumnCount(4)
        self.exam_tableWidget.setRowCount(0)
        self.exam_tableWidget.setHorizontalHeaderLabels(['Course ID', 'Course Name',
                                                         'Exam Time', 'Exam Location'])
        self.verticalLayout_7.addWidget(self.exam_tableWidget)

        self.tabWidget_2.addTab(self.exam_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_10.addWidget(self.label_25)

        self.evaluation_year_comboBox = QtWidgets.QComboBox(self.tab)
        self.evaluation_year_comboBox.setEnabled(True)
        self.evaluation_year_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        years = Utils.create_year_generator()
        for year in years:
            self.evaluation_year_comboBox.addItem(year)
        self.horizontalLayout_10.addWidget(self.evaluation_year_comboBox)

        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)

        self.evaluation_semester_comboBox = QtWidgets.QComboBox(self.tab)
        self.evaluation_semester_comboBox.setEnabled(True)
        self.evaluation_semester_comboBox.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.evaluation_semester_comboBox.addItem(" ")
        self.evaluation_semester_comboBox.addItem("1")
        self.evaluation_semester_comboBox.addItem("2")
        self.horizontalLayout_10.addWidget(self.evaluation_semester_comboBox)

        self.label_4 = QtWidgets.QLabel('Course', self.tab)
        self.label_4.setStyleSheet("font: 12pt \"Sans Serif\";")
        self.horizontalLayout_10.addWidget(self.label_4)

        self.course_comboBox = QtWidgets.QComboBox(self.tab)
        for course_data in courses_data:
            self.course_comboBox.addItem(course_data[1])
        self.horizontalLayout_10.addWidget(self.course_comboBox)

        self.evaluation_query_button = QtWidgets.QPushButton('Show Evaluation', self.tab)
        self.evaluation_query_button.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.horizontalLayout_10.addWidget(self.evaluation_query_button)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)

        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.evaluation_tableWidget = QtWidgets.QTableWidget(self.tab)

        self.evaluation_tableWidget.setColumnCount(1)
        self.evaluation_tableWidget.setRowCount(2)

        self.horizontalLayout_12.addWidget(self.evaluation_tableWidget)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.tabWidget_2.addTab(self.tab, "")
        self.personal_info_tab = QtWidgets.QWidget()
        self.personal_info_tab.setObjectName("personal_info_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.personal_info_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.info_tableWidget = QtWidgets.QTableWidget(self.personal_info_tab)
        self.info_tableWidget.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.info_tableWidget.setColumnCount(4)
        self.info_tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_tableWidget.setItem(6, 2, item)

        item = QtWidgets.QTableWidgetItem(self.teacher_id)
        self.info_tableWidget.setItem(0, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        item = QtWidgets.QTableWidgetItem(self.teacher_name)
        self.info_tableWidget.setItem(1, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        item = QtWidgets.QTableWidgetItem(self.teacher_MainWindow.user.gender)
        self.info_tableWidget.setItem(2, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        item = QtWidgets.QTableWidgetItem(self.teacher_MainWindow.user.birthday)
        self.info_tableWidget.setItem(3, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        item = QtWidgets.QTableWidgetItem(self.teacher_MainWindow.user.folk)
        self.info_tableWidget.setItem(4, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        item = QtWidgets.QTableWidgetItem(self.teacher_MainWindow.user.birth_place)
        self.info_tableWidget.setItem(5, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        item = QtWidgets.QTableWidgetItem(self.teacher_MainWindow.user.political_status)
        self.info_tableWidget.setItem(7, 1, item)
        self.verticalLayout_8.addWidget(self.info_tableWidget)

        self.tabWidget_2.addTab(self.personal_info_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.query_tab, "")
        self.change_pw_tab = QtWidgets.QWidget()
        self.change_pw_tab.setObjectName("change_pw_tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.change_pw_tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem9)
        self.old_password_line_edit = QtWidgets.QLineEdit(self.change_pw_tab)
        self.old_password_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.old_password_line_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.old_password_line_edit.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.old_password_line_edit.setInputMask("")
        self.old_password_line_edit.setText("")
        self.old_password_line_edit.setObjectName("old_password_line_edit")
        self.verticalLayout_10.addWidget(self.old_password_line_edit, 0, QtCore.Qt.AlignHCenter)
        self.new_password_line_edit = QtWidgets.QLineEdit(self.change_pw_tab)
        self.new_password_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.new_password_line_edit.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.new_password_line_edit.setObjectName("new_password_line_edit")
        self.verticalLayout_10.addWidget(self.new_password_line_edit, 0, QtCore.Qt.AlignHCenter)
        self.confirm_password_line_edit = QtWidgets.QLineEdit(self.change_pw_tab)
        self.confirm_password_line_edit.setMinimumSize(QtCore.QSize(250, 0))
        self.confirm_password_line_edit.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.confirm_password_line_edit.setObjectName("confirm_password_line_edit")
        self.verticalLayout_10.addWidget(self.confirm_password_line_edit, 0, QtCore.Qt.AlignHCenter)

        self.change_password_button = QtWidgets.QPushButton(self.change_pw_tab)
        self.change_password_button.setMinimumSize(QtCore.QSize(100, 0))
        self.change_password_button.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.change_password_button.clicked.connect(self.change_password)
        self.verticalLayout_10.addWidget(self.change_password_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem10)
        self.tabWidget.addTab(self.change_pw_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        teacher_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(teacher_MainWindow)
        self.statusbar.setObjectName("statusbar")
        teacher_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(teacher_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(teacher_MainWindow)

    def init_course_tab(self):
        course_name = self.course_name_comboBox.currentText()
        index = self.course_name_comboBox.currentIndex()
        try:
            course_info = Course.read_course(self.courses_id[index])
        except IndexError:
            msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
            msg_box.setWindowTitle('Sorry')
            msg_box.setText('You do not have any course')
            msg_box.exec_()
        except pymysql.Error as error:
            msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
            msg_box.setWindowTitle('Error')
            msg_box.setText(f'read courses failed!\nError: {error}')
            msg_box.exec_()
        else:
            for i in range(len(course_info)):
                if not course_info[i]:
                    course_info[i] = ''
            print('course info', course_info)
            self.course_id_label.setText('Course ID: ' + course_info[1])
            self.school_label.setText('School: ' + course_info[3])
            self.teacher_label.setText('Teacher Name: ' + course_info[5])
            self.class_time_label.setText('Class Time: ' + course_info[6])
            self.location_label.setText('Location: ' + course_info[7])

            students_data = get_students_data(course_info[0])
            self.init_course_table(students_data)

    def init_course_table(self, students_data):
        table = self.course_tableWidget
        table.setRowCount(0)

        for student_data in students_data:
            table.insertRow(table.rowCount())
            last_row = table.rowCount() - 1
            for i in range(table.columnCount()):
                if student_data[i]:
                    item = QtWidgets.QTableWidgetItem(str(student_data[i]))
                    table.setItem(last_row, i, item)

    def confrim_grades(self):
        table = self.course_tableWidget
        row_counts = table.rowCount()
        course_id = self.course_id_label.text()[11:]

        Database.initialize()
        try:
            for current_row in range(row_counts):
                if table.item(current_row, 5):
                    grade = int(table.item(current_row, 5).text())
                    student_id = table.item(current_row, 1).text()

                    save_grade(course_id, student_id, grade)
        except Exception as error:
            msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
            msg_box.setWindowTitle('Error')
            msg_box.setText(f'Confirm grades failed!\nError: {error}')
            msg_box.exec_()
        else:
            msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
            msg_box.setText(f'Confirm grades Successfully!')
            msg_box.exec_()

        Database.close()

    def init_exam_table(self):
        table = self.exam_tableWidget
        year = self.exam_year_comboBox.currentText()
        semester = self.exam_semester_comboBox.currentText()
        exams_data = Exam.read_exams(self.teacher_id, year, semester)
        table.setRowCount(0)

        for exam_data in exams_data:
            table.insertRow(table.rowCount())
            last_row = table.rowCount() - 1
            for i in range(table.columnCount()):
                if exam_data[i]:
                    item = QtWidgets.QTableWidgetItem(str(exam_data[i]))
                    table.setItem(last_row, i, item)

    def evaluation_query(self):
        pass

    def change_password(self):
        Database.initialize()
        account = Account.read_account(self.teacher_id)
        if Utils.check_hashed_password(self.old_password_line_edit.text(), self.teacher_id, account.password):
            try:
                Account.modify_account(self.teacher_id, self.new_password_line_edit.text(), 1, self.school)
            except pymysql.Error as error:
                msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
                msg_box.setWindowTitle('Error')
                msg_box.setText(f'read courses failed!\nError: {error}')
                msg_box.exec_()
            else:
                msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
                msg_box.setWindowTitle('Succress')
                msg_box.setText('Modified password successfully!')
                msg_box.exec_()
        else:
            msg_box = QtWidgets.QMessageBox(parent=self.teacher_MainWindow)
            msg_box.setWindowTitle('Error')
            msg_box.setText(f'The old password you input is wrong!')
            msg_box.exec_()
        Database.close()

    def retranslateUi(self, teacher_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        teacher_MainWindow.setWindowTitle(_translate("teacher_MainWindow", "Course Management System"))
        self.logout_button.setText(_translate("teacher_MainWindow", "Logout"))
        self.last_login_label.setText(_translate("teacher_MainWindow", "Last login: 2018-XX-XX 12:00 Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("teacher_MainWindow", "Home"))
        self.label_21.setText(_translate("teacher_MainWindow", "Year:"))

        self.label_22.setText(_translate("teacher_MainWindow", "Semester:"))
        self.label.setText(_translate("teacher_MainWindow", "My Courses:"))

        self.course_id_label.setText(_translate("teacher_MainWindow", "Course ID: "))
        self.teacher_label.setText(_translate("teacher_MainWindow", "Teacher Name: "))
        self.class_time_label.setText(_translate("teacher_MainWindow", "Class Time: "))
        self.school_label.setText(_translate("teacher_MainWindow", "School: "))
        self.location_label.setText(_translate("teacher_MainWindow", "Location: "))

        __sortingEnabled = self.course_tableWidget.isSortingEnabled()
        self.course_tableWidget.setSortingEnabled(False)

        self.course_tableWidget.setSortingEnabled(__sortingEnabled)
        self.print_button.setText(_translate("teacher_MainWindow", "Print"))
        self.grade_analysis_button.setText(_translate("teacher_MainWindow", "Grades Analysis"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.courses_tab),
                                    _translate("teacher_MainWindow", "My Courses"))
        self.label_18.setText(_translate("teacher_MainWindow", "Year:"))
        self.label_19.setText(_translate("teacher_MainWindow", "Semester:"))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.exam_tab),
                                    _translate("teacher_MainWindow", "Exam Query"))
        self.label_25.setText(_translate("teacher_MainWindow", "Year:"))
        self.label_26.setText(_translate("teacher_MainWindow", "Semester:"))

        self.course_comboBox.setItemText(0, _translate("teacher_MainWindow", "Java"))
        self.course_comboBox.setItemText(1, _translate("teacher_MainWindow", "C++ GUI Programming"))
        self.course_comboBox.setItemText(2, _translate("teacher_MainWindow", "Data Structures and Algorithms"))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab),
                                    _translate("teacher_MainWindow", " My Courses Evaluation"))
        item = self.info_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("teacher_MainWindow", "New Row"))
        item = self.info_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        item = self.info_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        item = self.info_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        item = self.info_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("teacher_MainWindow", "New Column"))
        __sortingEnabled = self.info_tableWidget.isSortingEnabled()
        self.info_tableWidget.setSortingEnabled(False)
        item = self.info_tableWidget.item(0, 0)
        item.setText(_translate("teacher_MainWindow", "Teacher ID:"))
        item = self.info_tableWidget.item(0, 2)
        item.setText(_translate("teacher_MainWindow", "School:"))
        item = self.info_tableWidget.item(1, 0)
        item.setText(_translate("teacher_MainWindow", "Name:"))
        item = self.info_tableWidget.item(1, 2)
        item.setText(_translate("teacher_MainWindow", "Department:"))
        item = self.info_tableWidget.item(2, 0)
        item.setText(_translate("teacher_MainWindow", "Gender:"))
        item = self.info_tableWidget.item(2, 2)
        item.setText(_translate("teacher_MainWindow", "Position:"))
        item = self.info_tableWidget.item(3, 0)
        item.setText(_translate("teacher_MainWindow", "Birth Date:"))
        item = self.info_tableWidget.item(3, 2)
        item.setText(_translate("teacher_MainWindow", "Phone No.:"))
        item = self.info_tableWidget.item(4, 0)
        item.setText(_translate("teacher_MainWindow", "Folk:"))
        item = self.info_tableWidget.item(5, 0)
        item.setText(_translate("teacher_MainWindow", "Hometown:"))
        item = self.info_tableWidget.item(6, 0)
        item.setText(_translate("teacher_MainWindow", "Political Status:"))
        self.info_tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.personal_info_tab),
                                    _translate("teacher_MainWindow", "Personal Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query_tab),
                                  _translate("teacher_MainWindow", "Information Query"))
        self.old_password_line_edit.setPlaceholderText(_translate("teacher_MainWindow", "Old Password"))
        self.new_password_line_edit.setPlaceholderText(_translate("teacher_MainWindow", "New Password"))
        self.confirm_password_line_edit.setPlaceholderText(_translate("teacher_MainWindow", "Confirm Password"))
        self.change_password_button.setText(_translate("teacher_MainWindow", "Change"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.change_pw_tab),
                                  _translate("teacher_MainWindow", "Change Password"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    teacher_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_teacher_MainWindow()
    ui.setupUi(teacher_MainWindow)
    teacher_MainWindow.show()
    sys.exit(app.exec_())
