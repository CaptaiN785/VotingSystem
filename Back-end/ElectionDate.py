from Module import *

class ElectionDate(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.POSTS = POSTS
        self.layout = QFormLayout()
        self.setLayout(self.layout)

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
        
        self.submit = QPushButton("Create election")
        self.submit.setIcon(QIcon("../images/tick.png"))
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



