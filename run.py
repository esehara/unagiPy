import src.configure
import src.logger
import src.filter
import src.database

def run():
	src.logger.write("Start","Runnning UnagiPy")
	input_result = []
	src.logger.write("Read","Reading Data.")
	for conf in src.configure.configure["ParseData"]:input_result.append(src.filter.blacklist_url(conf))
	src.logger.write("Save","DataBase Save.")
	for data in input_result:src.configure.configure["SaveDatabase"](data)

if __name__ == "__main__":run()
