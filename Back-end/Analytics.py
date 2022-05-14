from tkinter.messagebox import showwarning
from Module import *
import Database

class Analytics(QWidget):
    def __init__(self, MainWindow): 
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.setContentsMargins(100, 30, 100, 30)

        self.header = QLabel("Analytics")
        self.header.setStyleSheet("""
            font-size:40px;
            color:'#fff';
            margin:20px;
            font-family:cambria;
            margin-bottom:50px;
        """)
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addRow(self.header)

        self.dateLabel = QLabel("Select election ")
        self.past_election_list, self.eid_map = Database.get_past_election_list()
        self.election = QComboBox()
        self.election.addItem("Select an election")
        self.election.addItems(self.past_election_list)
        self.layout.addRow(self.dateLabel, self.election)
        
        self.btn = QPushButton("Search")
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout.addRow(self.btn)
        self.btn.clicked.connect(lambda: self.load_result())

        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        self.table.setRowCount(10)
        self.table.setColumnCount(2)   
        self.table.setHorizontalHeaderLabels(["Name", "Vote"])
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # self.table_header = self.table.horizontalHeader()
        # self.table_header.setSectionResizeMode(0, QHeaderView.strec)

        # use below for style sheet
        self.setStyleSheet("""
            QLabel{
                font-size:18px;
            }
            QComboBox{
                max-width:400px;
                padding:10px 20px;
                border:2px solid '#fff';
                font-size:16px;
            }
            QPushButton{
                max-width:200px;
                background:'#fff';
                color:'#0400c4';
                border:2px solid '#0400c4';
                padding:10px 20px;
                border-radius:20px;
                font-size:16px;
                margin-top:20px;
            }
            QPushButton:hover{
                background:'#0400c4';
                color:'#fff';
            }
        """)
    def load_result(self):
        if self.election.currentText() == "Select an election":
            showWarning("Please select a election")
            return;
        self.result = Database.get_result(self.eid_map[self.election.currentText()],self.election.currentText())
        print(self.result)
        for i in range(len(self.result)):
                self.table.setItem(i, 0, QTableWidgetItem(str(self.result[i][1])))
                self.table.setItem(i, 1, QTableWidgetItem(self.result[i][0]))
        # self.table.clearContents()

        



def showWarning(message, text="Warning"):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon('../images/logo.png'))
    msg.setWindowTitle(text)
    msg.setText(message)
    x = msg.exec()