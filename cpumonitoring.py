"""
    Programm zum Auslesen der CPU- und RAM-
    Auslastung und Export in MySQL

    Autor:  M. Schloßmacher, A. Liebig ,S. Kaulen ,L. Bergstein
    Datum:  09.12.2020
"""

import csv
import psutil
from datetime import datetime
import mysql.connector
import time
import login
#import des ausgelageten Programms

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="monitoring"
)

print(mydb)

login.login()
#Ausgelagertes Programm
