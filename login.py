"""
    Ausgelagertes Programm

    Autor:  M. Schloßmacher, A. Liebig ,S. Kaulen ,L. Bergstein
    Datum:  09.12.2020
"""

import mysql.connector
import psutil
from datetime import datetime
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="monitoring"
)
#Login in datenbank

def login():
    try:
        cpumax = 100
        cpumin = 0
        rammax = 100
        rammin = 0
        #zurücksetzen der Auslastungswerte
        while True:            
            
            time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu = psutil.cpu_percent(1)
            ram = psutil.virtual_memory().percent
            #Auslesen der Auslastung mit psutil
            if cpumax >= cpu:
                cpumax = cpu
            if cpumin <= cpu:
                cpumin = cpu
            if rammax >= ram:
                rammax = ram
            if rammin <= ram:
                rammin = ram
            #Abgleich der min und max auslastung
            sql = "INSERT INTO desktop1 (TIMESTAMP, CPU, CMAX, CMIN, RAM, RMAX, RMIN) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            #festlegen der zu übertragenden Daten
            mycursor = mydb.cursor()
            val = (time_str, cpu, cpumin, cpumax, ram , rammin, rammax)
            mycursor.execute(sql, val)
            #senden an die Datenbank


            time.sleep(10)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")


            
            

    except KeyboardInterrupt:
        print("... Abbruch!")
