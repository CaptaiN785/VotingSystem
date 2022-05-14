from Module import *
import Database

class AddCandidateC(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.setContentsMargins(50, 10, 50, 10)
        self.Image = None

        self.header = QLabel("Add Candidate")
        self.header.setStyleSheet("""
                    font-size:40px;
                    color:'#fff';
                    font-weight: bold;
                    font-family:cambria;
                    margin-bottom:50px;
                """)
        self.header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addRow(self.header)
        self.setStyleSheet("""
                  QLineEdit{
                      padding:10px 20px;
                      font-size:16px;
                      color:'#fff';
                      border:2px solid '#fff';
                      margin-top:20px;
                      max-width:400px;
                  }
                  QLabel{
                      font-size:18px;
                      color:'#fff';
                      margin-top:20px;
                  }
                  QPushButton{
                      font-size:16px;
                      padding:10px;
                      max-width:150px;
                      color: rgb(255, 255, 255);
                      border-radius:20px;
                      margin-top:20px;
                      background-color: rgb(35, 35, 35);
                  }
                  QPushButton:hover{
                          background-color: rgb(19, 81, 143) 
                          }
                  QComboBox{
                      font-size:16px;
                      padding:10px 20px;
                      color:'#fff';
                      border:2px solid '#fff';
                      margin-top:20px;
                      max-width:400px;
                  }
              """)



        self.vidlabel = QLabel("Enter voter id")
        self.vid = QLineEdit(placeholderText="Voter ID number")
        self.layout.addRow(self.vidlabel, self.vid)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.searchBtn = QPushButton(" Search")

        self.searchBtn.setIcon(QIcon("../images/search.png"))
        self.searchBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout.addRow(self.searchBtn)
        self.searchBtn.clicked.connect(self.loadAdditionalUI)

    def loadAdditionalUI(self):
        # Taking election name for adding in that election.
        self.electionName, self.electionMap = Database.get_upcoming_election_list()
        voterid = self.vid.text().strip()
        if not voterid.isdigit():
            showWarning("Entered voter ID is not valid.")
            return

        voter_list = Database.get_voterid_list()
        if not voterid in voter_list:
            showWarning("No record found.")
            return
        
        if len(self.electionName) == 0:
            showWarning("There is no election in future.")
            return

        self.vid.setEnabled(False)
        self.searchBtn.hide()

        self.frame = QWidget(self)
        self.frame.show()
        self.Layout = QFormLayout()
        self.frame.setLayout(self.Layout)
        self.layout.addWidget(self.frame)
        info = Database.get_voter_info(voterid)
        self.info = QLabel("{} \n{}".format(info["name"], info["dob"]))# showing name and dob for clarification
        # self.info.setEnabled(False)
        self.image = QPixmap(Database.get_voter_photo(voterid))
        self.imageUI = QLabel()
        self.imageUI.setPixmap(self.image.scaled(100, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.Layout.addRow(self.info, self.imageUI)
        self.electionlabel = QLabel("Select election")        
        self.election = QComboBox()
        self.election.addItems(self.electionName)
        # self.election.activated.connect(self.itemChanged)
        self.Layout.addRow(self.electionlabel,  self.election)
        
        # self.symbol = QPushButton("  Select symbol")
        # self.symbol.clicked.connect(self.chooseImage)
        # self.symbol.setIcon(QIcon("../images/shareicon.png"))
        # self.symbol.setStyleSheet("border-radius:0px;font-size:14px; padding:5px 30px;")

        self.sLabel = QLabel("Symbol")
        self.symbolLabel = QLabel()
        print(self.electionMap)
        symbol = Database.get_next_symbol(self.electionMap[self.election.currentText()])
        self.symbolLabel.setPixmap(QPixmap(symbol).scaled(80, 80, transformMode=Qt.TransformationMode.SmoothTransformation))
        self.Layout.addRow(self.sLabel, self.symbolLabel)

        self.submit = QPushButton("  Submit")
        self.submit.setIcon(QIcon("../images/tick.png"))
        self.submit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submit.clicked.connect(self.add_candidate)

        self.reset = QPushButton("Reset")
        self.reset.setIcon(QIcon("../images/cross.png"))
        self.reset.setCursor(Qt.CursorShape.PointingHandCursor)
        self.reset.clicked.connect(self.resetAll)
        self.Layout.addRow(self.reset,self.submit)

    def itemChanged(self):
        symbol = Database.get_next_symbol(self.electionMap[self.election.currentText()])
        self.symbolLabel.setPixmap(QPixmap(symbol).scaled(80, 80, transformMode=Qt.TransformationMode.SmoothTransformation))

    def chooseImage(self):
        fileName = QFileDialog.getOpenFileName(self,
        "Select Image", "", "Image Files (*.png *.jpg)")
        empty = ('', '') # empty filaName
        if fileName != empty:
            image, type = fileName
            self.imageSelected = QPixmap(image)
            self.symbolLabel.setPixmap(self.imageSelected.scaled(80, 80,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
            self.Image = self.convertToBinaryData(image)

    def convertToBinaryData(self,filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData    
    
    def add_candidate(self):
        vid = int(self.vid.text())
        eid = self.electionMap[self.election.currentText()]
        symbol = Database.get_next_symbol(eid)

        if(Database.add_candidate(vid, eid, symbol)):
            showWarning("Candidate added succesfully", "Success")
            self.resetAll()
        else:
            showWarning("Error adding candidate.")

    def resetAll(self):
        self.layout.removeRow(self.frame)
        self.vid.setEnabled(True)
        self.searchBtn.show()

def showWarning(message, text="Warning"):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon('../images/logo.png'))
    msg.setWindowTitle(text)
    msg.setText(message)
    x = msg.exec()
