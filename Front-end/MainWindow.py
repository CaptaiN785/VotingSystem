from Module import *
import DownloadVoterID
import CandidateList

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self, parnet=None):
        super().__init__()
        self.setWindowTitle("Election Commision of India")
        self.setWindowIcon(QIcon("../images/logo.png"))
        self.setFixedSize(1000, 700)
        self.setStyleSheet("background:'#151236'; color:'#fff';")
        self.show()

        self.topBar()

    def topBar(self):
        self.topBar = QWidget(self)
        self.setMenuWidget(self.topBar)
        self.menuBarLayout = QHBoxLayout()
        self.topBar.setLayout(self.menuBarLayout)

        self.homeButton = QPushButton(" Home")
        self.homeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.homeButton.setIcon(QIcon("../images/homeicon.png"))
        # self.homeButton.clicked.connect(lambda: changeWindow(Home.Home(self), self.homeButton))
        self.menuBarLayout.addWidget(self.homeButton)

        self.downloadVoterID = QPushButton("Download voter id")
        self.downloadVoterID.setIcon(QIcon("../images/shareicon.png"))
        self.downloadVoterID.setCursor(Qt.CursorShape.PointingHandCursor)
        self.menuBarLayout.addWidget(self.downloadVoterID)
        self.downloadVoterID.clicked.connect(lambda: changeWindow(DownloadVoterID.DownloadVoterID(self), self.downloadVoterID))
        
        self.checkCandidate = QPushButton("Candidate list")
        self.checkCandidate.setIcon(QIcon("../images/addmember.png"))
        self.checkCandidate.setCursor(Qt.CursorShape.PointingHandCursor)
        self.menuBarLayout.addWidget(self.checkCandidate)
        self.checkCandidate.clicked.connect(lambda: changeWindow(CandidateList.CandidateList(self), self.checkCandidate))
        

        self.electionResult = QPushButton("Election result")
        self.electionResult.setIcon(QIcon("../images/analytics.png"))
        self.electionResult.setCursor(Qt.CursorShape.PointingHandCursor)
        self.menuBarLayout.addWidget(self.electionResult)


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

    def toggle(self, btnClicked):
        css = """
            background:'#0400c4';
            color:'#fff';
        """
        self.homeButton.setStyleSheet(None)
        self.downloadVoterID.setStyleSheet(None)
        self.checkCandidate.setStyleSheet(None)
        # self.timeElection.setStyleSheet(None)
        # self.analytics.setStyleSheet(None)
        btnClicked.setStyleSheet(css)

def changeWindow(screen,btnClicked):
    window.setCentralWidget(screen)
    window.toggle(btnClicked)

if __name__ == '__main__':
    window = MainWindow()
    sys.exit(app.exec())
