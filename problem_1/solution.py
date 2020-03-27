import validators

class URL_Splitter:
	def __init__(self, url):
		self.url = url
		self.sep = self.url.split('/', 3)

	def split(self):
		self.protocol = self.protocol()
		self.domain = self.domain()
		self.path = self.path()
		return "\nProtocol: {} \nDomain: {} \nPath: {}\n".format(self.protocol, self.domain, self.path)

	def protocol(self):
		return self.sep[0][:-1]

	def domain(self):
		return self.sep[2]

	def path(self):
		return self.sep[3]

if __name__ == "__main__":
	ask_url = input("Please input a url to be split: ")
	while validators.url(ask_url) != True:
		ask_url = input("INVALID url, please input another url: ")
	url = URL_Splitter(ask_url)
	print(url.split())