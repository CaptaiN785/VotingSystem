from Module import *

class CandidateList(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.Layout = QFormLayout()
        self.setLayout(self.Layout)

        self.header = QLabel("Candidate List")
        self.header.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.header.setStyleSheet("""
            font-size:40px;
            color:'#fff';
            font-family:cambria; 
            font-weight:bold; 
        """)
        self.Layout.addWidget(self.header)

        # add from here




        # use it for stylesheet
        self.setStyleSheet("""

        """)