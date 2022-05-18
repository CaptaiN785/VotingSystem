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
        self.setWindowTitle('Login')
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clean()


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


        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: toggleMenu(self, 190, True))
        self.ui.btn_Home.clicked.connect(self.ui.button1)
        self.ui.btn_AddVoter.clicked.connect(self.ui.button2)
        self.ui.btn_AddCandidate.clicked.connect(self.ui.button3)
        self.ui.btn_ElectionDate.clicked.connect(self.ui.button4)
        self.ui.btn_Analytics.clicked.connect(self.ui.button5)
        # MINIMIZE
        self.ui.Min_btn.clicked.connect(lambda: self.showMinimized())
        # MAXIMIZE/RESTORE
        self.ui.Max_btn.clicked.connect(lambda: self.showMaximized())

        # CLOSE APPLICATION
        self.ui.Close_btn.clicked.connect(lambda: self.close())
        self.show()


        self.Login_panel = Login(self)
        self.login_btn = self.Login_panel.login_btn
        self.setCentralWidget(self.Login_panel)
        self.login_btn.clicked.connect(lambda: self.check_login())

    def check_login(self):
        if(self.Login_panel.get_username_password() == ("admin", "admin")):
            self.ui.login_success(self)
        else:
            showWarning("Invalid username or password!")


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
