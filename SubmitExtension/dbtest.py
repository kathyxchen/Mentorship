import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()

def getEmails():
	c.execute('SELECT email FROM users')
	return c.fetchall() 

def getNumUsers():
	c.execute('SELECT COUNT(*) FROM users')
	return c.fetchone()

def insertDrop():
	t = ("Robert');DROP TABLE users", 'email', 'pass')
	c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', t)
	conn.commit()

def insertThree():
	c.execute("INSERT INTO users (name, email, password) VALUES ('foo', 'b', 'c')")
	c.execute("INSERT INTO users (name, email, password) VALUES ('bar', 'b', 'c')")
	c.execute("INSERT INTO users (name, email, password) VALUES ('baz', 'b', 'c')")
	conn.commit()

def insertFourth():
	c.execute("SELECT COUNT(*) FROM users WHERE name = 'foo'")
	x = c.fetchone()
	if (x[0] == 0):
		print "inserting"
		c.execute("INSERT INTO users (name, email, password) VALUES ('foo', 'b', 'c')")
		conn.commit()

