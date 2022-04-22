from Module import *
import Database

class ElectionDate(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.POSTS = POSTS
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        assemblyList, assemblyMap = Database.get_assembly_list() #
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
        self.assembly.addItems(assemblyList)
        self.layout.addRow(self.assemblyLabel, self.assembly)

        self.submit = QPushButton("Create election")
        self.submit.setIcon(QIcon("../images/tick.png"))
        self.submit.setMaximumWidth(400)
        self.submit.setCursor(Qt.CursorShape.PointingHandCursor)
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



