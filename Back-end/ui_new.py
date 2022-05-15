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
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        ######################### TOP BAR ############################
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))  # updated to maximum size upto 40 from 400
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
        self.frame_toggle.setStyleSheet("background-color: rgb(20, 80, 140);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
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
        self.Btn_Toggle.setMinimumSize(QtCore.QSize(70, 40))

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
        self.horizontalLayout.addStretch(1)
        self.horizontalLayout.setSpacing(2)


        ############### WINNDOW TITLE####################



        ##########TOP FRAME BUTTONS###############
        self.Min_btn = QtWidgets.QPushButton()
        self.horizontalLayout.addWidget(self.Min_btn, alignment=QtCore.Qt.AlignmentFlag.AlignTop )
        self.Min_btn.setMinimumSize(QtCore.QSize(50, 30))
        self.Min_btn.setIcon(QIcon("../images/icon_minimize.svg"))
        self.Min_btn.setIconSize(QtCore.QSize(18, 18))
        self.Min_btn.setObjectName("Min_btn")
        self.Min_btn.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "border: 0px solid;"
                                            "padding-left: 5px; padding-right: 5px;"
                                            "padding-top: 5px; padding-bottom: 5px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(20, 80, 140);"
                                            "}")

        self.Max_btn = QtWidgets.QPushButton()
        self.horizontalLayout.addWidget(self.Max_btn, alignment=QtCore.Qt.AlignmentFlag.AlignTop )
        self.Max_btn.setMinimumSize(QtCore.QSize(50, 30))
        self.Max_btn.setIcon(QIcon("../images/icon_maximize.svg"))
        self.Max_btn.setIconSize(QtCore.QSize(12, 12))
        self.Max_btn.setObjectName("Max_btn")
        self.Max_btn.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "border: 0px solid;"
                                            "padding-left: 5px; padding-right: 5px;"
                                            "padding-top: 5px; padding-bottom: 5px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(20, 80, 140);"
                                            "}")

        self.Close_btn = QtWidgets.QPushButton()
        self.horizontalLayout.addWidget(self.Close_btn, alignment=QtCore.Qt.AlignmentFlag.AlignTop )
        self.Close_btn.setMinimumSize(QtCore.QSize(50, 30))
        self.Close_btn.setIcon(QIcon("../images/icon_close.svg"))
        self.Close_btn.setIconSize(QtCore.QSize(12, 12))
        self.Close_btn.setObjectName("Close_btn")
        self.Close_btn.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "border: 0px solid;"
                                            "padding-left: 5px; padding-right: 5px;"
                                            "padding-top: 5px; padding-bottom: 5px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(240, 20, 36);"
                                            "}")

        ######################## MAIN CONTENT #########################
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Content.setObjectName("Content")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ##################### SIDE MENU FRAME################################
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(190, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        ###################### BUTTON FOR HOME############################
        self.btn_Home = QtWidgets.QPushButton("     Home")
        self.verticalLayout_3.addWidget(self.btn_Home)
        self.btn_Home.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_Home.setIcon(QIcon("../images/homeicon.png"))
        self.btn_Home.setIconSize(QtCore.QSize(24, 24))
        self.btn_Home.setObjectName("btn_Home")
        self.verticalLayout_3.addWidget(self.btn_Home)

        ###################### BUTTON TO ADD VOTER ###################
        self.btn_AddVoter = QtWidgets.QPushButton("     Add Voter")
        self.btn_AddVoter.setIconSize(QtCore.QSize(24, 24))
        self.verticalLayout_3.addWidget(self.btn_AddVoter)
        self.btn_AddVoter.setIcon(QIcon("../images/addmember.png"))
        self.btn_AddVoter.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_AddVoter.setObjectName("btn_AddVoter")
        self.verticalLayout_3.addWidget(self.btn_AddVoter)

        ###################### BUTTON TO ADD CANDIDATE ###################
        self.btn_AddCandidate = QtWidgets.QPushButton("     Add Candidate")
        self.btn_AddCandidate.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_AddCandidate.setIconSize(QtCore.QSize(24, 24))
        self.btn_AddCandidate.setObjectName("btn_AddCandidate")
        self.verticalLayout_3.addWidget(self.btn_AddCandidate)
        self.btn_AddCandidate.setIcon(QIcon("../images/plusicon.png"))

        ################ Button to set election  #################3
        self.btn_ElectionDate = QtWidgets.QPushButton("     Election Date")
        self.btn_ElectionDate.setIconSize(QtCore.QSize(24, 24))
        self.btn_ElectionDate.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_AddCandidate.setObjectName("btn_ElectionDate")
        self.verticalLayout_3.addWidget(self.btn_ElectionDate)
        self.btn_ElectionDate.setIcon(QIcon("../images/tick.png"))

        #########################    Button to add analytics ###################
        self.btn_Analytics = QtWidgets.QPushButton("     Analytics")
        self.verticalLayout_3.addWidget(self.btn_Analytics)
        self.btn_Analytics.setIconSize(QtCore.QSize(24, 24))
        self.btn_Analytics.setMinimumSize(QtCore.QSize(70, 40))
        self.btn_Analytics.setIcon(QIcon("../images/analytics.png"))
        self.btn_Home.setObjectName("btn_Analytics")
        self.verticalLayout_3.addWidget(self.btn_Analytics)
        self.verticalLayout_3.addStretch(1)

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

    def clean(self):
        self.btn_Home.setStyleSheet("QPushButton {"
                                    "color: rgb(255, 255, 255);"
                                    "text-align: left;"
                                    "font-size: 18px;"
                                    "height: 48px;"
                                    "border: 0px solid;"
                                    "font-family:cambria;"
                                    "padding-left: 20px; padding-right: 3px;"
                                    "padding-top: 1px; padding-bottom: 1px;"
                                    "}"
                                    "QPushButton:hover {"
                                    "    background-color: rgb(20, 80, 140);"
                                    "}")
        self.btn_AddVoter.setStyleSheet("QPushButton {"
                                        "color: rgb(255, 255, 255);"
                                        "text-align: left;"
                                        "font-size: 18px;"
                                        "height: 48px;"
                                        "border: 0px solid;"
                                        "font-family:cambria;"
                                        "padding-left: 20px; padding-right: 3px;"
                                        "padding-top: 1px; padding-bottom: 1px;"
                                        "}"
                                        "QPushButton:hover {"
                                        "    background-color: rgb(20, 80, 140);"
                                        "}")
        self.btn_AddCandidate.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "text-align: left;"
                                            "font-size: 18px;"
                                            "height: 48px;"
                                            "border: 0px solid;"
                                            "font-family:cambria;"
                                            "padding-left: 20px; padding-right: 3px;"
                                            "padding-top: 1px; padding-bottom: 1px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(20, 80, 140);"
                                            "}")
        self.btn_ElectionDate.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "text-align: left;"
                                            "font-size: 18px;"
                                            "height: 48px;"
                                            "border: 0px solid;"
                                            "font-family:cambria;"
                                            "padding-left: 20px; padding-right: 3px;"
                                            "padding-top: 1px; padding-bottom: 1px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(20, 80, 140);"
                                            "}")
        self.btn_Analytics.setStyleSheet("QPushButton {"
                                         "color: rgb(255, 255, 255);"
                                         "text-align: left;"
                                         "font-size: 18px;"
                                         "height: 48px;"
                                         "border: 0px solid;"
                                         "font-family:cambria;"
                                         "padding-left: 20px; padding-right: 3px;"
                                         "padding-top: 1px; padding-bottom: 1px;"
                                         "}"
                                         "QPushButton:hover {"
                                         "    background-color: rgb(20, 80, 140);"
                                         "}")

    def button1(self):
        self.stackedWidget.setCurrentWidget(self.Home)
        self.clean()
        self.btn_Home.setStyleSheet("QPushButton {"
                                    "color: rgb(255, 255, 255);"
                                    "text-align: left;"
                                    "font-size: 18px;"
                                    "height: 48px;"
                                    "border-width: 0px;"
                                    "font-family:cambria;"
                                    "padding-left: 20px; padding-right: 3px;"
                                    "padding-top: 1px; padding-bottom: 1px;"
                                    "}"
                                    "QPushButton:hover {"
                                    "    background-color: rgb(20, 80, 140);"
                                    "}")

    def button2(self):
        self.stackedWidget.setCurrentWidget(self.AddVoter)
        self.clean()
        self.btn_AddVoter.setStyleSheet("QPushButton {"
                                        "color: rgb(255, 255, 255);"
                                        "text-align: left;"
                                        "font-size: 18px;"
                                        "height: 48px;"
                                        "border-width: 0px;"
                                        "font-family:cambria;"
                                        "padding-left: 20px; padding-right: 3px;"
                                        "padding-top: 1px; padding-bottom: 1px;"
                                        "}"
                                        "QPushButton:hover {"
                                        "    background-color: rgb(20, 80, 140);"
                                        "}")

    def button3(self):
        self.stackedWidget.setCurrentWidget(self.AddCandidate)
        self.clean()
        self.btn_AddCandidate.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "text-align: left;"
                                            "font-size: 18px;"
                                            "height: 48px;"
                                            "border-width: 0px;"
                                            "font-family:cambria;"
                                            "padding-left: 20px; padding-right: 3px;"
                                            "padding-top: 1px; padding-bottom: 1px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(20, 80, 140);"
                                            "}")

    def button4(self):
        self.stackedWidget.setCurrentWidget(self.ElectionDate)
        self.clean()
        self.btn_ElectionDate.setStyleSheet("QPushButton {"
                                            "color: rgb(255, 255, 255);"
                                            "text-align: left;"
                                            "font-size: 18px;"
                                            "height: 48px;"
                                            "border-width: 0px;"
                                            "font-family:cambria;"
                                            "padding-left: 20px; padding-right: 3px;"
                                            "padding-top: 1px; padding-bottom: 1px;"
                                            "}"
                                            "QPushButton:hover {"
                                            "    background-color: rgb(20, 80, 140);"
                                            "}")

    def button5(self):
        self.stackedWidget.setCurrentWidget(self.Analytics)
        self.clean()
        self.btn_Analytics.setStyleSheet("QPushButton {"
                                         "color: rgb(255, 255, 255);"
                                         "text-align: left;"
                                         "font-size: 18px;"
                                         "height: 48px;"
                                         "border-width: 0px;"
                                         "font-family:cambria;"
                                         "padding-left: 20px; padding-right: 3px;"
                                         "padding-top: 1px; padding-bottom: 1px;"
                                         "}"
                                         "QPushButton:hover {"
                                         "    background-color: rgb(20, 80, 140);"
                                         "}")

    def login_success(self, MainWindow):
        ########################### ADD STACKED WIDGET ####################
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setMaximumWidth(1920)
        MainWindow.setFixedHeight(1080)
        MainWindow.showMaximized()
        MainWindow.setWindowTitle('Voting Application')
