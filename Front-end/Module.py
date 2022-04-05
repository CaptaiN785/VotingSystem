############     All is PyQt6 package       ###################
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import mysql.connector
import re
import random

import datetime
import cv2
# import face_recognition

LOGO_PATH = "../images/eci-logo.png"
POSTS = ["MLA", "Mukhiya", "Ward Member"]