import re
from src.configure import *

is_url = re.compile("^http")
filter_url = []
for line in open(configure["Blacklist"],encoding="UTF-8").readlines():
	if is_url.match(line):filter_url.append(line.rstrip())

def blacklist_url(array):
	def is_ok_url(string):
		global filter_url
		for fi in filter_url:
			if string.find(fi) is not -1:return ""
		return string
	filter_result = []
	for el in array:
		is_result = is_ok_url(el["url"])
		if is_result is not "":filter_result.append(el)
	return filter_result

if __name__ == "__main__":
	print("""
			Test blacklist_url()
		""")
	TestData = [
				{"url":"http://hogehoge/entry/hoge"}
				,{"url":"http://akb48matome.com/hogehogehoge"}
				,{"url":"http://hoget.com/hoge"}
				]
	print(str(TestData))
	print(str(blacklist_url(TestData)))
