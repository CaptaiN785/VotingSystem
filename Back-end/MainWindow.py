from Module import *
from Color import *

import AddCandidate
import AddVoter
import Home
import ElectionDate
import Analytics

####################################
app = QApplication(sys.argv)
app.setStyle('Fusion')

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("Election commission India")
        self.setWindowIcon(QIcon("logo.png"))
        self.setStyleSheet(f"background:{PRIMARY_COLOR}; color:'#fff';")
        # self.setFixedSize(1000, 700)

        self.showMaximized()

        self.topBar = QWidget(self)
        self.topBar.setGeometry(0,0, 1000, 70)
        self.topBar.setStyleSheet("""
                *{
                    background:'#fff';
                }
                QPushButton{
                    background:'#fff';
                    border: 2px solid '#0400c4';
                    border-radius:5px;
                    color:'#0400c4';
                    font-size:16px;
                    padding:5px;
                }
                QPushButton:hover{
                    background:'#0400c4';
                    color:'#fff';
                }
            """)
        self.setMenuWidget(self.topBar)
        self.lyt = QHBoxLayout()
        self.topBar.setLayout(self.lyt)

        self.homeButton = QPushButton("  Home")
        self.homeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.homeButton.setIcon(QIcon("homeicon.png"))
        self.homeButton.clicked.connect(lambda: changeWindow(Home.Home(self), self.homeButton))
        self.lyt.addWidget(self.homeButton)
        
        self.addVoter = QPushButton("  Add Voter")
        self.addVoter.setCursor(Qt.CursorShape.PointingHandCursor)
        self.addVoter.setIcon(QIcon("plusicon.png"))
        self.addVoter.clicked.connect(lambda: changeWindow(AddVoter.AddVoter(self), self.addVoter))
        self.lyt.addWidget(self.addVoter)

        self.addCandidate = QPushButton("  Add Candidate")
        self.addCandidate.setCursor(Qt.CursorShape.PointingHandCursor)
        self.addCandidate.setIcon(QIcon("addmember.png"))
        self.addCandidate.clicked.connect(lambda: changeWindow(AddCandidate.AddCandidate(self), self.addCandidate))
        self.lyt.addWidget(self.addCandidate)

        self.timeElection = QPushButton("  Set election date")
        self.timeElection.setCursor(Qt.CursorShape.PointingHandCursor)
        self.timeElection.setIcon(QIcon("tick.png"))
        self.timeElection.clicked.connect(lambda: changeWindow(ElectionDate.ElectionDate(self), self.timeElection))
        self.lyt.addWidget(self.timeElection)

        self.analytics = QPushButton("  Analytics")
        self.analytics.setCursor(Qt.CursorShape.PointingHandCursor)
        self.analytics.setIcon(QIcon("analytics.png"))
        self.analytics.clicked.connect(lambda: changeWindow(Analytics.Analytics(self), self.analytics))
        self.lyt.addWidget(self.analytics)


    def toggle(self, btnClicked):
        css = """
            background:'#0400c4';
            color:'#fff';
        """
        self.homeButton.setStyleSheet(None)
        self.addVoter.setStyleSheet(None)
        self.addCandidate.setStyleSheet(None)
        self.timeElection.setStyleSheet(None)
        self.analytics.setStyleSheet(None)
        btnClicked.setStyleSheet(css)

def changeWindow(screen,btnClicked):
    window.setCentralWidget(screen)
    window.toggle(btnClicked)

try:
    window = MainWindow()
    window.setCentralWidget(Home.Home(window))
    window.toggle(window.homeButton)
    sys.exit(app.exec())
except SystemExit:
    print("Closing all programs")
    