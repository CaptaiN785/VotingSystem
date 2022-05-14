from Module import *
import Database

class HomeC(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.verticalLayout_7 = QVBoxLayout()
        self.setLayout(self.verticalLayout_7)
        self.setContentsMargins(100, 30, 100, 30)

        self.logo = QPixmap("../images/eci-logo.png")
        self.logolabel = QLabel()
        self.logolabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.logolabel.setPixmap(self.logo.scaled(500, 120, Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
        self.verticalLayout_7.addWidget(self.logolabel)
        
        # election  ->  candidateid, post ,date, vote
        # Table for upcoming election
        self.data = Database.get_upcoming_election_table_detail()
        self.table = QTableWidget()
        self.table.setRowCount(16)
        self.table.setColumnCount(3)   
        self.table.setColumnWidth(0, 245) 
        self.table.setColumnWidth(1, 250) 
        self.table.setColumnWidth(2, 250)
        self.table.setMaximumHeight(300)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(["Date", "Post", "Assembly"])
        # self.table.setItem()
        self.verticalLayout_7.addWidget(self.table)
        self.verticalLayout_7.addStretch()

        self.setStyleSheet("""
            QTableWidget{
                border:2px solid '#fff';
                margin-top:30px;
                padding:0px;
                background:'#85fbff';
            }
            QTableWidget{
                color:'#000';
            }
        """)
