from pip._vendor import requests

path = "ip_addr"
wordlist = "directory-list-2.3-medium.txt"
extenstions = ["js", "css", "py", "txt", "html"]
file = open(wordlist, "r")
len_of_path = len(path)
class main():

	for line in file:
		path = path + line.strip()
		res = requests.get(path)
		stat_cod = res.status_code
		if stat_cod in [200, 301, 403]:
			print(path + " " + str(stat_cod))
		for extion in extenstions:
			req = requests.get(path + "." + extion)
			req_stat_cod = req.status_code
			if req_stat_cod in [200, 301, 403]:
				print(path + " " + str(req_stat_cod))
		path = path[:len_of_path]

