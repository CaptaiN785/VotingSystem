from Module import *
import Database

class Login(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        MainWindow.setFixedSize(500,500)
        self.setContentsMargins(50, 50, 50, 50)
        self.show()
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.heading = QLabel("Login")
        self.heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addRow(self.heading)

        self.username = QLineEdit(placeholderText="Enter username")
        self.layout.addRow(self.username)

        self.password = QLineEdit(placeholderText="Enter password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addRow(self.password)

        self.login_btn = QPushButton("Login")
        self.layout.addRow(self.login_btn)

        self.setStyleSheet("""
            *{
                font-family:cambria;
            }
            QLabel{
                max-width:400px;
                color:'#fff';
                font-size:40px;
                margin: 30px;
                font-family:cambria;
                font-weight:bold;
            }
            QLineEdit{
                max-width:400px;
                font-size:16px;
                color:'#fff';
                border-radius:5px;
                padding:10px;
                border:2px solid '#fff';
                margin:10px 0;
            }
          
            QPushButton{
                      font-size:18px;
                      padding:10px;
                      max-width:400px;
                      color: rgb(255, 255, 255);
                      border-radius:20px;
                      margin-top:20px;
                      background-color: rgb(35, 35, 35);
                  }
                  QPushButton:hover{
                          background-color: rgb(19, 81, 143) 
                          }
        """)
    def get_username_password(self):
        return self.username.text(), self.password.text()