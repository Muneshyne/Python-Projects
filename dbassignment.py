

import os
import sqlite3

conn = sqlite3.connect('styles.db')

with conn:
      cur = conn.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS tbl_style( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_sName TEXT, \
            col_sPerson TEXT \
            )")
      conn.commit()
conn.close()
#created the table with a column named col_style

conn = sqlite3.connect('styles.db')

with conn:
      cur = conn.cursor()
      cur.execute("INSERT INTO tbl_style(col_sName, col_sPerson) VALUES (?,?)", \
                  ('Blue', 'Jack')) # always add the , between values
      conn.commit()
conn.close()


def writeData():
      data = '\nHello World!'
      with open('Hello.txt', 'a') as f:  #a = append
            f.write(data)
            f.close()


def openFile():
      with open('Hello.txt','r') as f:
            data = f.read()
            print(data)
            f.close()




if __name__ == "__main__":
      writeData()
      openFile()
