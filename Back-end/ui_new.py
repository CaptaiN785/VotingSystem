from PyQt6 import QtCore, QtGui, QtWidgets
from Home import *
from AddVoter import *
from AddCandidate import *
from ElectionDate import *
from Analytics import *
from Login import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        ######################### TOP BAR ############################
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40)) # updated to maximum size upto 40 from 400
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        ######################### FRAME TOGGLE ############################
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        ######################### TOGGLE BUTTON ############################
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;"
                                      "font-size:24px;")
        self.Btn_Toggle.setText("\u2261")
        self.Btn_Toggle.setObjectName("Btn_Toggle")

        #################### TOP FRAME ########################################
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)

        ######################## MAIN CONTENT #########################
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Content.setObjectName("Content")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")


        ##################### TOP MENU FRAME################################
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        ######################### LEFT MENU FRAME ###########################
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMinimumSize(QtCore.QSize(70, 200)) # left menu size policy
        self.frame_top_menus.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_top_menus.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")


        ###################### BUTTON FOR HOME############################
        self.btn_Home = QtWidgets.QPushButton()
        self.verticalLayout_3.addWidget(self.btn_Home)
        self.btn_Home.setMinimumSize(QtCore.QSize(70, 40))
        # self.btn_Home.setText(u"\u2261")
        self.btn_Home.setIcon(QIcon("../images/homeicon.png"))
        self.btn_Home.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_Home.setObjectName("btn_Home")
        self.verticalLayout_4.addWidget(self.btn_Home)


        ###################### BUTTON TO ADD VOTER ###################
        self.btn_AddVoter = QtWidgets.QPushButton()

        self.verticalLayout_3.addWidget(self.btn_AddVoter)
        self.btn_AddVoter.setIcon(QIcon("../images/addmember.png"))
        self.btn_AddVoter.setMinimumSize(QtCore.QSize(70, 40))
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        self.btn_AddVoter.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_AddVoter.setObjectName("btn_AddVoter")
        self.verticalLayout_4.addWidget(self.btn_AddVoter)


        ###################### BUTTON TO ADD CANDIDATE ###################
        self.btn_AddCandidate = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_AddCandidate.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_AddCandidate.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_AddCandidate.setObjectName("btn_AddCandidate")
        self.verticalLayout_4.addWidget(self.btn_AddCandidate)
        self.btn_AddCandidate.setIcon(QIcon("../images/plusicon.png"))

        ################ Button to set election  #################3
        self.btn_ElectionDate = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_ElectionDate.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_ElectionDate.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_AddCandidate.setObjectName("btn_ElectionDate")
        self.verticalLayout_4.addWidget(self.btn_ElectionDate)
        self.btn_ElectionDate.setIcon(QIcon("../images/tick.png"))

        #########################    Button to add analytics ###################
        self.btn_Analytics = QtWidgets.QPushButton()
        self.verticalLayout_3.addWidget(self.btn_Analytics)
        self.btn_Analytics.setMinimumSize(QtCore.QSize(70, 40))
        # self.btn_Home.setText(u"\u2261")
        self.btn_Analytics.setIcon(QIcon("../images/analytics.png"))
        self.btn_Analytics.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(35, 35, 35);\n"
                                            "    border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}")
        self.btn_Home.setObjectName("btn_Analytics")
        self.verticalLayout_4.addWidget(self.btn_Analytics)


        ########################### ADD FRAMES ###########################
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")


        ############## ADD BUTTONS TO STACKED WIDGET #####################
        self.Home = HomeC(MainWindow)
        self.Home.setObjectName("Home")
        self.stackedWidget.addWidget(self.Home)

        self.AddVoter = AddVoterC(MainWindow)
        self.AddVoter.setObjectName("AddVoter")
        self.stackedWidget.addWidget(self.AddVoter)

        self.AddCandidate = AddCandidateC(MainWindow)
        self.AddCandidate.setObjectName("AddCandidate")
        self.stackedWidget.addWidget(self.AddCandidate)

        self.ElectionDate = ElectionDate(MainWindow)
        self.ElectionDate.setObjectName("ElectionDate")
        self.stackedWidget.addWidget(self.ElectionDate)

        self.Analytics = Analytics(MainWindow)
        self.Analytics.setObjectName("Analytics")
        self.stackedWidget.addWidget(self.Analytics)

        # self.verticalLayout.setObjectName("verticalLayout")
