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
        self.table.setRowCount(max(12, len(self.data)))
        self.table.setColumnCount(3)   
        self.table.setColumnWidth(0, 250) 
        self.table.setColumnWidth(1, 250) 
        self.table.setColumnWidth(2, 250)
        self.table.setMaximumHeight(400)
        self.table.setMaximumWidth(790)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(["Date", "Post", "Assembly"])
        for i in range(len(self.data)):
            for j in range(3):
                self.table.setItem(i, j, QTableWidgetItem(str(self.data[i][j])))

        self.verticalLayout_7.addWidget(self.table)
        self.verticalLayout_7.addStretch()

        self.setStyleSheet("""
            QTableWidget{
                color: blue;
                background-color: yellow;
                selection-color: yellow;
                selection-background-color: blue;
                font-size:16px;
                background-color: #646464;
                 border: 1px solid #fffff8;
            }
            
        """)
