#!/usr/bin/python3.2
#-*- coding:utf-8 -*-
import postgresql
import cgitb
import sys,io

sys.stdout = io.TextIOWrapper(
		sys.stdout.buffer,encoding="utf-8")
print("Content-type: text/html")
print("Pragma: no-cache")
print("Cache-Control: no-cache")
print("Expires: Mon, 26 Jul 1997 05:00:00 GMT")
print()
print("""
		<!DOCTYPE HTML>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>UnagiPy</title>
		</head>
		<body>
		<h1> UnagiPy </h1>
		
		<ul>
			<li> <a href="set.py?comd=alldel">全部消す</a>
		</ul>

		<ul>
		""")
cgitb.enable()
db = postgresql.open("pq://postgres:postgres@localhost:5432/cloning")
table = db.prepare("SELECT * FROM urllist")()
for elem in table:
	if elem[4].rstrip() != "true":
		print("""<div>
					<h2> <a href='set.py?go=%i'>%s</a> </h2>
					""" %(elem[0],elem[1].rstrip().replace("<","").replace(">","")))
		print("%s" % elem[3])
		print("""<div>
					<a href='set.py?d=%i'>消す</a>
				</div>
			</div></li>""" % elem[0])
print("""
		</ul>
		</body>
		</html>
		""")
