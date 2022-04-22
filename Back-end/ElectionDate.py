from Module import *
import Database
import datetime
class ElectionDate(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.POSTS = POSTS
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.assemblyList, self.assemblyMap = Database.get_assembly_list() #
        # assemblyList has assembly name
        # assemblyMap has name as key and aid as value in its dictionary

        self.header = QLabel("Set Election Date")
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.header.setStyleSheet("font-size:40px;font-family:cambria;font-weight:bold;")
        self.layout.addRow(self.header)
        self.setContentsMargins(100, 30, 100, 30)

        self.nameLabel = QLabel("Add election name")
        self.name = QLineEdit(placeholderText="Enter election name")
        self.layout.addRow(self.nameLabel, self.name)

        self.dateLabel = QLabel("Select election date")
        self.date = QDateEdit()
        self.layout.addRow(self.dateLabel, self.date)

        self.postLabel = QLabel("Select post")
        self.post = QComboBox()
        self.post.addItems(self.POSTS)
        self.layout.addRow(self.postLabel, self.post)

        self.assemblyLabel = QLabel("Select assembly")
        self.assembly = QComboBox()
        self.assembly.addItems(self.assemblyList)
        self.layout.addRow(self.assemblyLabel, self.assembly)

        self.submit = QPushButton("Create election")
        self.submit.setIcon(QIcon("../images/tick.png"))
        self.submit.setMaximumWidth(400)
        self.submit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submit.clicked.connect(self.add_election)
        self.layout.addRow(self.submit)

        self.setStyleSheet("""
            QLabel{
                font-size:18px;
                color:'#fff';
                margin-top:20px;
            }
            QLineEdit,QDateEdit, QComboBox{
                margin-top:20px;
                padding:10px 20px;
                font-size:16px;
                border:2px solid '#fff';
                max-width:400px;
            }
            QPushButton{
                padding:10px 30px;
                margin-top:40px;
                background:'#fff';
                color:'#0400c4';
                border:2px solid '#0400c4';
                border-radius:20px;
                font-size:16px;
            }
            QPushButton:hover{
                background:'#0400c4';
                color:'#fff';
            }
        """)
    
    def add_election(self):
        print("inside add electio.")
        name = self.name.text()
        date = self.date.text()
        ed = datetime.datetime(day = int(date[0:2]), month=int(date[3:5]), year=int(date[-4:]))
        now = datetime.datetime.now()
        if ed < now :
            showWarning("Please check the election date.")
            return
        post = self.post.currentText()
        assembly = self.assembly.currentText()
        aid = self.assemblyMap[assembly]

        if Database.add_election_detail(name, date, post, aid):
            showWarning("Election details added succesfully.", "Success")
        else:
            showWarning("Unable to add election details.")

        self.name.setText("")

def showWarning(message, text="Warning"):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon('../images/logo.png'))
    msg.setWindowTitle(text)
    msg.setText(message)
    x = msg.exec()
