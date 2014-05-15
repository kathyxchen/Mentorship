import sqlite3
import datetime
conn = sqlite3.connect('users.db')

c = conn.cursor()

def usersCreate(user, mail, pw):
	t = (user, mail, pw)
	c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", t)
	conn.commit()
	c.execute('SELECT last_insert_rowid()')
	return c.fetchone()

def usersUpdate(idNum, user, mail, pw):
	t = (idNum, user, mail, pw)
	c.execute("INSERT OR REPLACE INTO users (id, name, email, password) VALUES (?, ?, ?, ?)", t)
	conn.commit()

def usersDelete(idNum):
	t = idNum
	c.execute("DELETE from users WHERE id = ?", t)
	conn.commit()

def usersGetInfo(idNum):
	c.execute("SELECT * from users WHERE id = ?", t)
	return c.fetchall()

def reqCreate(userID, DT, rec, url, msg, proc):
	t = (userID, DT, rec, url, msg, proc)
	c.execute("INSERT INTO requests (user_id, datetime, recipient, sendURL, message, processed) VALUES (?, ?, ?, ?, ?, ?)", t)
	conn.commit()
	c.execute('SELECT last_insert_rowid()')
	return c.fetchone()

def reqUpdate(idNum, userID, DT, rec, url, msg, proc):
	t = (idNum, userID, DT, rec, url, msg, proc)
	c.execute("INSERT INTO requests (id, user_id, datetime, recipient, sendURL, message, processed) VALUES (?, ?, ?, ?, ?, ?, ?)", t)
	conn.commit()

def reqDelete(idNum):
	c.execute("DELETE from requests WHERE id = " + str(idNum))
	conn.commit()

def reqGetInfo(idNum):
	c.execute("SELECT * from requests WHERE id = " + str(idNum))
	return c.fetchall()	

def getByTime(fst, snd):
	time1 = datetime.datetime.strptime(fst, "%m/%d/%Y %H:%M")
	time2 = datetime.datetime.strptime(snd, "%m/%d/%Y %H:%M")
	c.execute("SELECT * from requests WHERE datetime BETWEEN time1 AND time2")
	return c.fetchall()