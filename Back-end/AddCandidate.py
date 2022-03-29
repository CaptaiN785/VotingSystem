from Module import *

class AddCandidate(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.setContentsMargins(100, 10, 100, 50)
        self.Image = None
        self.POSTS = POSTS

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
                background:'#0400c4';
                color:'#fff';
                border:2px solid '#fff';
                border-radius:20px;
                margin-top:20px;
            }
            QPushButton:hover{
                background:'#fff';
                color:'#0400c4';
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
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.heading = QLabel("Add candidate")
        self.heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.heading.setStyleSheet("font-size:40px;font-family:cambria; font-weight:bold;")
        self.layout.addRow(self.heading)

        self.vidlabel = QLabel("Enter voter id")
        self.vid = QLineEdit(placeholderText="Voter ID number")
        self.layout.addRow(self.vidlabel, self.vid)

        self.searchBtn = QPushButton(" Search")
        self.searchBtn.setIcon(QIcon("../images/search.png"))
        self.searchBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout.addRow(self.searchBtn)
        self.searchBtn.clicked.connect(self.loadAdditionalUI)

    def loadAdditionalUI(self):
        self.vid.setEnabled(False)
        self.searchBtn.hide()

        self.info = QLabel()
        self.info.setText("Mukesh Kumar Thakur \n01-01-2000")
        # self.info.setEnabled(False)

        self.image = QPixmap("../images/addmember.png")
        self.imageUI = QLabel()
        self.imageUI.setPixmap(self.image.scaled(100, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.layout.addRow(self.info, self.imageUI)
    
        self.postlabel = QLabel("Select post ")        
        self.post = QComboBox()
        self.post.addItems(self.POSTS)
        self.layout.addRow(self.postlabel,  self.post)
        
        self.symbol = QPushButton("  Select symbol")
        self.symbol.clicked.connect(self.chooseImage)
        self.symbol.setIcon(QIcon("../images/shareicon.png"))
        self.symbol.setStyleSheet("border-radius:0px;font-size:14px; padding:5px 30px;")
        self.symbolLabel = QLabel()
        self.symbolLabel.setPixmap(QPixmap("images/addmember.png").scaled(80, 80, transformMode=Qt.TransformationMode.SmoothTransformation))
        self.layout.addRow(self.symbol,self.symbolLabel)

        self.submit = QPushButton("  Submit")
        self.submit.setIcon(QIcon("../images/tick.png"))
        self.submit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout.addRow(self.submit)

    def chooseImage(self):
        fileName = QFileDialog.getOpenFileName(self,
        "Select Image", "", "Image Files (*.png *.jpg)")
        empty = ('', '') # empty filaName
        if fileName != empty:
            image, type = fileName
            self.imageSelected = QPixmap(image)
            self.symbolLabel.setPixmap(self.imageSelected.scaled(80, 80,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
            self.Image = self.convertToBinaryData(image)

    def convertToBinaryData(self,filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData    