import sqlite3
from os import path
import pandas as pd


def readSqliteData(filepath):
    if path.isfile(filepath):
        dbcon = sqlite3.connect(filepath)
    else:
        print(" file does not exist!")
        exit(-1)
    table = "data"
    query = "pragma table_info(" + table + ")"
    cursor = dbcon.cursor()
    cursor.execute(query)
    row = cursor.fetchone()

    query = "select * from " + table + ";"
    cursor = dbcon.cursor()
    cursor.execute(query)

    data = []
    row = cursor.fetchone()
    while row:
        data.append((row[1], row[3]))
        row = cursor.fetchone()
    dfObj = pd.DataFrame(data, columns=["text", "class_label"])
    cursor.close()
    dbcon.close()
    return dfObj
