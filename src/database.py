from src.configure import *

def data_filter(array):
	if len(array["title"]) > 255: array["title"] = array["title"][:255]
	if len(array["url"]) > 255: array["url"] = array["url"][:255]
	return array

def postgresql(array):
	import postgresql
	db = postgresql.open("pq://postgres:postgres@localhost:5432/cloning")
	checkurl = db.prepare("SELECT * FROM urllist WHERE url=$1")
	mkdata = db.prepare("INSERT INTO urllist VALUES (nextval('cloning_seq'),$1,$2,$3,'false')")
	for elem in array:
		if len(checkurl(elem["url"])) is 0:
			elem = data_filter(elem)
			mkdata(elem["title"],elem["url"],elem["details"])

