# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import src.logger
import urllib.request
import json

"""
	Module Init.
"""
def get_soup(url):
	return BeautifulSoup(urllib.request.urlopen(url).read().decode("UTF-8"))

def log_write(string):
	src.logger.write("Parse",string)

"""
	Write Parser Define.
"""

def hatena_parser(url):
	log_write("Parsing Hatena BookMark Entry")

	return_array = []
	soup = get_soup(url).find_all("blockquote")
	for entry_elem in soup:
		return_array.append(
						{
							"title":entry_elem.cite["title"]
							,"url":entry_elem["cite"]
							,"details":entry_elem.text.replace("続きを読む","").replace(" ","")
						})
	return return_array


def hacker_parser(url):
	log_write("Parsing HackerNews Rss")
	
	return_array = []
	soup = get_soup(url).find_all("item")
	for entry_elem in soup:
		return_array.append(
				{"title":entry_elem.title.text
				,"url":entry_elem.link.text
				,"details":entry_elem.description.text
				})
	return return_array

def twitter_url(url):
	data = urllib.request.urlopen("http://search.twitter.com/search.json?q=%E8%AB%96%E6%96%87+http&rpp=20&include_entities=true&result_type=recent").read().decode("UTF-8")
	jsondata = json.loads(data)
	urlmatch = re.compile("(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)")
	for target_data in jsondata["results"]:
		short_url = target_data["text"].group(0)
