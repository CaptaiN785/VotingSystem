from Module import *
import Database
import datetime
class ElectionDate(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.POSTS = Database.POSTS
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.assemblyList, self.assemblyMap = Database.get_assembly_list() #
        # assemblyList has assembly name
        # assemblyMap has name as key and aid as value in its dictionary

        self.header = QLabel("Set Election Date")
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.header.setStyleSheet("font-size:40px;font-family:cambria;font-weight:bold;color: #fff;")
        self.layout.addRow(self.header)
        self.setContentsMargins(100, 30, 100, 30)

        self.nameLabel = QLabel("Add election name")
        self.name = QLineEdit(placeholderText="name(only alphanum or _ and no space)")
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
    
    def add_election(self):
        print("inside add electio.")
        name = self.name.text()
        if len(name) < 3:
            showWarning("Please check election name.")
            return
        date = self.date.text()
        ed = datetime.date(int(date[-4:]), int(date[3:5]), int(date[0:2]))
        now = datetime.date.today()
        if ed < now:
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
