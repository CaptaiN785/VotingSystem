from Module import *

class DownloadVoterID(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.Layout = QFormLayout()
        self.setLayout(self.Layout)

        self.header = QLabel("Download VoterID Card")
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.header.setStyleSheet("""
            font-size:40px;
            color:'#fff';
            font-family:cambria;
            font-weight:bold;
        """)
        self.Layout.addWidget(self.header)

        # Add from here
        
        

        # use below for stylesheet
        self.setStyleSheet("""
            QLabel{

            }
            QPushButton{

            }
        """)
