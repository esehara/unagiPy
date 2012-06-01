import datetime
from src.configure import * 

logfile = configure["LogFile"]

def write(category,string):
	openfile = open(logfile,mode="a",encoding="utf-8")
	openfile.write("[%s][%s] : %s \n" %(str(datetime.datetime.today()),category,string))
	openfile.close()

def test_main():
	write("test-category","test-string")

if __name__ == "__main__":
	test_main()
