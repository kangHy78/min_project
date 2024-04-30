import sqlite3


con = sqlite3.connect("local.sqlite")

cur = con.cursor()

# cur.execute("INSERT INTO admins VALUES (1, 'admin', '1234')")


cur.execute("DELETE FROM cafes WHERE id=1")


con.commit()

cur.close()
con.close()



