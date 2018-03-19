import cx_Oracle
con=cx_Oracle.connect('system/1qazxsw2@localhost:1521/xe')
cur=con.cursor()

print con.version, con.version.split('.')


cur.execute("""
        SELECT * from SYS.ALL_ALL_TABLES""")

            
for row in cur:
    print(row)

cur.close()             
con.close()

