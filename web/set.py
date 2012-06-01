#!/ur/bin/env python3
# -*- coding:utf-8 -*-

import sys,io,time
import cgi,cgitb
import os
import postgresql
cgitb.enable()
sys.stdout = io.TextIOWrapper(
		sys.stdout.buffer,encoding="utf-8")

class Controller:
	def __init__(self):
		self.cgi_value = cgi.parse_qs(os.environ['QUERY_STRING']) if 'QUERY_STRING' in os.environ else {}
	
def goback():
	print("Content-type: text/html")
	print("Location: index.py")
	print()
	
def main():
	con = Controller()
	db = postgresql.open("pq://postgres:postgres@localhost:5432/cloning")
	if "d" in con.cgi_value:
		db.execute("UPDATE urllist set display='true' WHERE id=%s" % con.cgi_value["d"][0])
		goback()
	if "go" in con.cgi_value:
		go_url = db.prepare("SELECT * FROM urllist WHERE id=%s" % con.cgi_value["go"][0])()
		db.execute("UPDATE urllist set display='true' WHERE id=%s" % con.cgi_value["go"][0])
		print("Content-type: text/html")
		print("Location: " + go_url[0][2])
		print()
	if "comd" in con.cgi_value:
		if con.cgi_value["comd"][0] == "alldel":
			db.execute("UPDATE urllist set display='true' WHERE display='false'")
			goback()

if __name__ == "__main__":main()
