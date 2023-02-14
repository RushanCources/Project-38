import sqlite3
from datetime import date, datetime

conn = sqlite3.connect(r"Путь к базе данных")
cur = conn.cursor()
cur.execute("SELECT date_of_expiring FROM announcements_announcement")
dates = cur.fetchall()

for i in dates:
    if datetime.now().date() >= date.fromisoformat(i[0][:10]):
        cur.execute("DELETE FROM announcements_announcement WHERE date_of_expiring=?", (i[0],))

conn.commit()
conn.close()
