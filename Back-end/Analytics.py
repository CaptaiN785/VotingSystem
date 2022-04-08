from Module import *

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
        """)
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addRow(self.header)

        self.dateLabel = QLabel("Select date of election ")
        dates = ["12-03-2002", "30-11-2022"]
        self.date = QComboBox()
        self.date.addItems(dates)
        self.layout.addRow(self.dateLabel, self.date)
        
        self.btn = QPushButton("Search")
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout.addRow(self.btn)

        # Add from here












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