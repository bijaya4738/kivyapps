
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=ADARSHA;UID=sa;PWD=Test123')
cursor = cnxn.cursor()
cursor.execute("select AccountNo ,Agent_Id,MonthlyAmount from Account")
rows = cursor.fetchall()
for row in rows:
    print row.AccountNo
