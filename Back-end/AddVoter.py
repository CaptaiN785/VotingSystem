from Module import *
import Database

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
        self.defaultImage = QPixmap("../images/user.png") # default user image in  adding voter
        self.show()

        ############### database connectivity ######################
        
        ############    complete UI     ######################
        self.header = QLabel("Add Voter")
        self.header.setStyleSheet("""
                            font-size:40px;
                            color:'#fff';
                            font-weight: bold;
                            font-family:cambria;
                            margin-bottom:50px;
                        """)
        self.header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.Layout.addRow(self.header)

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
                      color: rgb(255, 255, 255);
                      border-radius:20px;
                      margin-top:20px;
                      background-color: rgb(35, 35, 35);
                  }
                  QPushButton:hover{
                          background-color: rgb(19, 81, 143) 
                          }
                  QComboBox{
                      font-size:16px;
                      padding:10px 20px;
                      color:'#fff';
                      border:2px solid '#fff';
                      margin-top:20px;
                      max-width:400px;
                  }
                  QDateEdit
                        {
                        padding:10px 20px;
                      font-size:16px;
                      color:'#fff';
                      border:2px solid '#fff';
                      margin-top:20px;
                      max-width:400px;
                        }

              """)
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
        self.items.append(self.dobLabel)
        self.Layout.addRow(self.dobLabel, self.dob)
        self.dobVerified = False

        # Assembly
        self.assemblyLabel = QLabel("Select your assembly")
        self.assembly = QComboBox()
        self.assembly.insertItem(0,"Select your assembly")
        self.assemblyList = Database.get_assembly_list()[0]
        self.assembly.addItems(self.assemblyList)
        self.items.append(self.assemblyLabel)
        self.items.append(self.assembly)
        self.Layout.addRow(self.assemblyLabel, self.assembly)

        # PIN codes
        self.pinLabel = QLabel("Enter your pin")
        self.pin = QComboBox()
        self.pin.insertItem(0, "Select your pin")
        self.PINS = Database.get_pin_list()
        self.pin.addItems(self.PINS)
        self.items.append(self.pinLabel)
        self.items.append(self.pin)
        self.Layout.addRow(self.pinLabel, self.pin)

        # Submit button
        self.submit = QPushButton(" Submit")
        self.submit.setIcon(QIcon("../images/tick.png"))
        self.Layout.addRow(self.submit)
        self.submit.clicked.connect(self.addVoter)

        for item in self.items:
            if type(item) == QLineEdit:
                item.setStyleSheet("*{font-size:16px;padding:10px 20px;color:'#fff';max-width:400px;margin-top:20px;}"+
                "*:active{ border-color:'#fff'; }")
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

        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.defaultImage.scaledToHeight(200,Qt.TransformationMode.SmoothTransformation))
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.imageLabel.setStyleSheet("border:2px solid '#fff';padding:0px;min-height:200px;")

        self.imageSelector = QPushButton(" Select Image")
        self.imageSelector.setIcon(QIcon("../images/shareicon.png"))
        self.imageSelector.setCursor(Qt.CursorShape.PointingHandCursor)
        self.imageSelector.clicked.connect(self.chooseImage)
        VBL.addWidget(self.imageLabel)
        VBL.addWidget(self.imageSelector)
        VBL.addStretch()

    ########################adding voter to database
    def addVoter(self):
        Name = self.name.text()
        Phone = self.phone.text()
        Email = self.email.text()
        DOB = self.dob.text()
        Assembly = self.assembly.currentText()
        Pin = self.pin.currentText()
        Image = self.Image
        status, info = Database.add_voter(Name, Phone, Email, DOB, Assembly, Pin, Image)
        if(status):
            save_image(info["voterid"], info["name"], info["phone"], info["email"], DOB, Assembly, Pin)
            self.reset()
            showWarning("Voter is added.", text="Sucess")
        else:
            showWarning("Error in adding voter.")
        

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
    
    def reset(self):
        self.name.setText("")
        self.phone.setText("")
        self.email.setText("")
        self.assembly.currentText()
        self.pin.currentText()
        self.Image = None
        self.imageLabel.setPixmap(self.defaultImage.scaledToHeight(200,Qt.TransformationMode.SmoothTransformation))

def showWarning(message, text="Warning"):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon('../images/logo.png'))
    msg.setWindowTitle(text)
    msg.setText(message)
    x = msg.exec()

def save_image(voterid, name, mobile, email, dob, assembly, pin):
    background = PIL.Image.open('../images/background.png')
    screen = ImageDraw.Draw(background)

    my_font = ImageFont.truetype('calibri.ttf', 20)
    big_font = ImageFont.truetype('calibri.ttf', 60)

    screen.text((100, 20), "Voter information", font=big_font, fill=(0, 0, 0))

    screen.text((30, 100), "VoterID  : {}".format(voterid),font=my_font, fill =(0, 0, 0))
    screen.text((30, 130), "Name     : {}".format(name),font=my_font, fill =(0, 0, 0))
    screen.text((30, 160), "Mobile   : {}".format(mobile),font=my_font, fill =(0, 0, 0))
    screen.text((30, 190), "Email   : {}".format(email),font=my_font, fill =(0, 0, 0))
    screen.text((30, 220), "DOB     : {}".format(dob),font=my_font, fill =(0, 0, 0))
    screen.text((30, 250), "Assembly: {}".format(assembly),font=my_font, fill =(0, 0, 0))
    screen.text((30, 280), "PIN     : {}".format(pin),font=my_font, fill =(0, 0, 0))

    desktop = pathlib.Path.home() / 'Desktop'
    background.save(os.path.join(desktop, name+".png"))
