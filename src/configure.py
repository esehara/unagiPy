configure = {}

"""
	Log Data
"""

configure["LogFile"] = "/var/log/unagipy/log.txt"

#Fix it !!
configure["Blacklist"] = "/home/esehara/Python/unagipy/dat/blacklist.txt"

from src.database import * 
configure["SaveDatabase"] = postgresql
configure["DatabaseConfig"] = {
		"url":"pq://postgres:postgres@localhost:5432/cloning"
		}
"""
	What do you read site ?
"""

from src.parse import *
configure["ParseData"] = [hatena_parser("http://b.hatena.ne.jp/entrylist?threshold=2"),
						  hacker_parser("http://feeds.feedburner.com/hacker-news-feed?format=xml")]
