from Module import *
from Color import *

from Home import*
from AddCandidate import*
from AddVoter import*

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

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


try:
    window = MainWindow()
    sys.exit(app.exec())
except SystemExit:
    print("Closing all programs")
