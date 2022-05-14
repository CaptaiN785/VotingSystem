import this
from Module import *
from Home import *
from AddCandidate import *
from AddVoter import *
import Database
from Login import *

import ElectionDate
import Analytics

####################################
app = QApplication(sys.argv)
app.setStyle('Fusion')

# GUI FILE
from ui_new import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        def toggleMenu(self, maxWidth, enable):
            if enable:

                # GET WIDTH
                width = self.ui.frame_left_menu.width()
                maxExtend = maxWidth
                standard = 70

                # SET MAX WIDTH
                if width == 70:
                    widthExtended = maxExtend
                else:
                    widthExtended = standard

                # ANIMATION
                self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
                self.animation.setDuration(400)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.start()

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################
        # PAGE 1
        self.ui.btn_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        # PAGE 2
        self.ui.btn_AddVoter.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.AddVoter))
        # PAGE 3
        self.ui.btn_AddCandidate.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.AddCandidate))
        # PAGE 4
        self.ui.btn_ElectionDate.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ElectionDate))
        # Page 5
        self.ui.btn_Analytics.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Analytics))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        
       
        
        self.Login_panel = Login(self)
        self.login_btn = self.Login_panel.login_btn
        self.setCentralWidget(self.Login_panel)
        self.login_btn.clicked.connect(lambda: self.check_login())

    def check_login(self):
        if(self.Login_panel.get_username_password() == ("admin", "admin")):
            self.login_success()
        else:
            showWarning("Invalid username or password!")

    def login_success(self):
        ########################### ADD STACKED WIDGET ####################
        self.ui.verticalLayout_5.addWidget(self.ui.stackedWidget)
        self.ui.horizontalLayout_2.addWidget(self.ui.frame_pages)
        self.ui.verticalLayout.addWidget(self.ui.Content)
        self.setCentralWidget(self.ui.centralwidget)
        self.ui.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

def showWarning(message, text="Warning"):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon('../images/logo.png'))
    msg.setWindowTitle(text)
    msg.setText(message)
    x = msg.exec()


try:
    window = MainWindow()
    sys.exit(app.exec())
except SystemExit:
    print("Closing all programs")
