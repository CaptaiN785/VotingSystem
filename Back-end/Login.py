from Module import *
import Database

class Login(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.setContentsMargins(50, 50, 50, 50)
        MainWindow.width = 500
        MainWindow.height = 500
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
                max-width:400px;
                padding:10px;
                color:'#fff';
                font-size:18px;
            }
        """)
    def get_username_password(self):
        return self.username.text(), self.password.text()