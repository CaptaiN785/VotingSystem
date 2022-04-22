from Module import *
import conn

class AddVoterC(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.items = []
        self.Image = None
        self.setStyleSheet(f"color:'#fff';")
        self.Layout = QFormLayout()
        self.setLayout(self.Layout)
        self.setContentsMargins(50, 10, 50, 10)
        self.show()
        self.PIN = sorted(conn.PIN)
        self.AID = conn.AID
        self.ANAME = sorted(conn.ANAME)
        self.VID = conn.VID
        ############### database connectivity ######################
        
        #############################################################
        ############    complete UI     ######################
        self.label = QLabel("Add Voters")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setStyleSheet("font-size:40px;color:'#fff';font-weight:bold;font-family:cambria;")
        self.Layout.addRow(self.label)

        # Name
        self.nameLabel = QLabel("Enter your name")
        self.name = QLineEdit(placeholderText="Enter your name")
        self.items.append(self.nameLabel)
        self.items.append(self.name)
        self.Layout.addRow(self.nameLabel, self.name)

        # phone number
        self.phoneLabel = QLabel("Phone no.")
        self.phone = QLineEdit(placeholderText="10 digit mobile no.")
        self.items.append(self.phoneLabel)
        self.items.append(self.phone)
        self.Layout.addRow(self.phoneLabel, self.phone)

        # Email
        self.emailLabel = QLabel("Enter email")
        self.email = QLineEdit(placeholderText="email : abc@email.com")
        self.items.append(self.emailLabel)
        self.items.append(self.email)
        self.Layout.addRow(self.emailLabel, self.email)

        # DOB
        self.dobLabel = QLabel("Date of birth")
        self.dob = QDateEdit()
        self.dob.setStyleSheet("*{font-size:16px;max-width:400px;"+
                "border:2px solid '#fff';"+
                "padding:10px 0px; margin-top:20px;}")
        self.items.append(self.dobLabel)
        self.Layout.addRow(self.dobLabel, self.dob)
        self.dobVerified = False

        # Assembly
        self.assemblyLabel = QLabel("Select your assembly")
        self.assembly = QComboBox()
        self.assembly.insertItem(0,"Select you assembly")
        self.assembly.addItems(self.ANAME)
        self.items.append(self.assemblyLabel)
        self.items.append(self.assembly)
        self.Layout.addRow(self.assemblyLabel, self.assembly)

        # PIN codes
        self.pinLabel = QLabel("Enter your pin")
        self.pin = QComboBox()
        self.pin.insertItem(0, "Select your pin")
        self.pin.addItems(self.PIN)
        self.items.append(self.pinLabel)
        self.items.append(self.pin)
        self.Layout.addRow(self.pinLabel, self.pin)

        # Submit button
        self.submit = QPushButton(" Submit")
        self.submit.setIcon(QIcon("../images/tick.png"))
        self.submit.setStyleSheet("*{padding:10px 30px;border-radius:20px;max-width:300px;"+
        "font-size:16px;background:'#fff';border:2px solid '#0400c4';"+
        "color:'#0400c4';margin:50px 200px 0 200px;}"+
        "*:hover{ background:'#0400c4'; color:'#fff';}")
        self.Layout.addRow(self.submit)
        self.submit.clicked.connect(self.addVoter)

        for item in self.items:
            if type(item) == QLineEdit:
                item.setStyleSheet("*{font-size:16px;padding:10px 20px;color:'#fff';max-width:400px;margin-top:20px;}"+
                "*:active{ border-color:'#f00'; }")
            elif type(item) == QComboBox:
                item.setStyleSheet("padding:10px 20px;color:'#fff';max-width:400px;"+
                "margin-top:20px;font-size:16px;;")
            else:
                item.setStyleSheet("font-size:18px;color:'#fff';margin-top:20px;")

        ########       Side Panel for selecting image
        sidepanel = QWidget(self)
        sidepanel.setGeometry(720, 140, 250, 300)
        sidepanel.show()
        VBL = QVBoxLayout()
        sidepanel.setLayout(VBL)

        self.imageSelected = QPixmap("../images/user.png")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.imageSelected.scaledToHeight(200,Qt.TransformationMode.SmoothTransformation))
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.imageLabel.setStyleSheet("border:2px solid '#fff';padding:0px;min-height:200px;")

        self.imageSelector = QPushButton(" Select Image")
        self.imageSelector.setIcon(QIcon("../images/shareicon.png"))
        self.imageSelector.setStyleSheet(
            "*{ padding:10px 20px;border:2px solid '#fff';"+
            "border-radius:20px;"+
            " background:'#fff';color:'#0400c4';}"+
            "*:hover{ background:'#0400c4'; color:'#fff'; }"
            )
        self.imageSelector.setCursor(Qt.CursorShape.PointingHandCursor)
        self.imageSelector.clicked.connect(self.chooseImage)
        VBL.addWidget(self.imageLabel)
        VBL.addWidget(self.imageSelector)
        VBL.addStretch()

    ################################        adding voter to database
    def addVoter(self):
        if self.validated():
            try:
                voterid = self.generateVoterId()
                Name = self.name.text()
                Phone = int(self.phone.text())
                Email = self.email.text()
                DOB = self.dob.text()
                Assembly = int(self.AID[self.assembly.currentText()])
                Pin = self.pin.currentText()
                Image = self.Image
                # print(Image)
                # values = (voterid, Name, Phone, Email, DOB, Image, Pin, Assembly)
                # query = 'insert into voter values({}, "{}", {}, "{}", str_to_date("%\d-%m-%y","{}"), now(), "{}", "{}", {})'.format(voterid, Name, Phone, Email, DOB, Image, Pin, Assembly)
                self.conn = conn.conn
                cursor = self.conn.cursor()
                cursor.execute('insert into voter values(%d, %s, %d, %s, str_to_date("%d-%m-%y",%s), now(), %s, %s, %d)',(voterid, Name, Phone, Email, DOB, Image, Pin, Assembly,))
                self.conn.commit()
                print(cursor)
            except mysql.connector.Error as e:
                print("database error while uploading details", e)
    
    def validated(self):
        Name = self.name.text()
        Name = Name.strip()
        if len(Name) < 3 or len(Name) > 20:
            self.name.setFocus()
            showWarning("Please enter your correct name \n")
            return False

        Phone = self.phone.text()
        if Phone == "" or len(Phone) != 10 or not Phone.isnumeric():
            self.phone.setFocus()
            showWarning("Please enter your valid phone number \n")
            return False

        Email = self.email.text()
        if Email == "" or not "@" in Email or not "." in Email:
            self.email.setFocus()
            showWarning("Please enter valid email address \n")
            return False

        DOB = self.dob.text()
        if DOB == "01-01-2000" and not self.dobVerified:
            showWarning("Please verify your DOB")
            self.dobVerified = True
            return False
        
        Assembly = self.assembly.currentText()
        if Assembly not in self.ANAME:
            self.assembly.setFocus()
            showWarning("Please choose your assembly.")
            return False
        
        Pin = self.pin.currentText()
        if Pin not in self.PIN:
            self.pin.setFocus()
            showWarning("Please select your PIN")
            return False
        Image = self.Image
        if Image == None:
            showWarning("Please select image")
            return False
        # print(Name, Phone, Email, DOB, Assembly, Pin, Image)
        return True
    
    def chooseImage(self):
        fileName = QFileDialog.getOpenFileName(self,
        "Select Image", "", "Image Files (*.png *.jpg)")
        empty = ('', '') # empty filaName
        if fileName != empty:
            image, type = fileName
            self.imageSelected = QPixmap(image)
            self.imageLabel.setPixmap(self.imageSelected.scaledToHeight(200,Qt.TransformationMode.SmoothTransformation))
            self.Image = self.convertToBinaryData(image)

    def convertToBinaryData(self,filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
    def generateVoterId(self):
        vid = random.randint(10000000, 99999999)
        while vid in self.VID:
            vid = random.randint(10000000, 99999999)
        
        return vid

def showWarning(message):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon('../images/logo.png'))
    msg.setWindowTitle("Warning")
    msg.setText(message)
    x = msg.exec()
