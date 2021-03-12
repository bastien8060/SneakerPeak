import error as log
import htmlmin, subprocess, re, sys, os, requests
from bs4 import BeautifulSoup

sys.setrecursionlimit(1000)
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
def nextword(target, source):
	for i, w in enumerate(source):
		if w == target:
			#print(source[i+1])
			return source[i+1]



#BASIC CONSTRUCTOR

class sneaker:
	def __init__(self, source, url):
		self.url = url
		self.source = source
		infos = scrapesneaker(source, url)
		if infos["exist"]:
			self.price = infos["price"]
			self.sizes = infos["sizes"]
			self.colors = infos["colors"]
			self.limited = infos["limited"]
			self.title = infos["title"]
			self.instock = infos["instock"]
			self.obj = infos
		else:
			self.instock = False
		self.exist = infos["exist"]
		self.obj = infos



#JDSPORTS METHODS:

class jdsports:

	def price(content):
		return content.select("button")[0].attrs["data-price"]

	def sizes(content):
		result = []
		for i in content.div.select("button", text=True, recursive=False):
			if hasNumbers(i.text.strip()):
				result.append((re.sub("[^0-9]", "", i.text.strip())))
		return result

	def title(content):
		return content.select('h1')[0].text.strip()

	def instock(content):
		if jdsports.sizes(content) == []:
			return False
		return True

	def colors(content):
		found = False
		result = ["Not Detected"]
		for i in content.select("h3"):
			if i.text.strip() == "Colour:":
				element = i
				found = True
		if found:
			result = [element.next_sibling]

		return ', '.join(result)

	def limited(content):
		limited = False
		if "is limited" in content.text:
			limited = True
		return limited


	def scrape(baseurl):
		url = baseurl+"/stock/?_=16154193570"

		#headers = {'user-agent': 'curl/7.70.0',"Host": "m.jdsports.ie","accept": "*/*","Accept-Encoding": "gzip, deflate, br",}
		#source = requests.get(url, headers=headers).content.decode()

		sourcepage = subprocess.check_output(['curl', '-s', baseurl]).decode()
		pagesoup = BeautifulSoup(htmlmin.minify(sourcepage.replace("\n","").replace("\t",""),remove_empty_space=True),features="lxml")

		sourceapi = subprocess.check_output(['curl', '-s', url]).decode()
		apisoup = BeautifulSoup(htmlmin.minify(sourceapi.replace("\n","").replace("\t",""),remove_empty_space=True),features="lxml")

		return {"exist":True,"title":jdsports.title(pagesoup),"price":jdsports.price(apisoup),"sizes":jdsports.sizes(apisoup),"colors":jdsports.colors(pagesoup),"limited":jdsports.limited(pagesoup),"instock":jdsports.instock(apisoup)}






#JDSPORTS METHODS:

class footlocker:

	def price(content):
		i = content.find_all("div", {"class": "ProductPrice"})[0].find_all('span')[0]
		return i.text.replace(" ","").replace(",",".")

		
	def sizes(content):
		allsizes = []
		for i in content.find_all("div", {"class":"ProductSize--europe"}):
			allsizes.append(i.text)
		return allsizes


	def title(content):
		for i in content.find_all("nav", {"class": "c-breadcrumbs"}):
			return i.text.strip("Home>").strip("Home >")

	def instock(content):
		if jdsports.sizes(content) == []:
			return False
		return True

	def colors(content):
		result = ["Not Detected"]
		element = ""
		for i in content.find_all("div", {"class":"ProductDetails-description"}):
			for ij in i.find_all("li"):
				if "Color:" in ij.text:
					if element == "":
						element = ij
			if "Color:" in i.text:
				if element == "":
					element = i

		color = element.text.strip("Color: ").strip("Color:").strip("Color")
			
		if len(color) > 20 or color == None or color == "None":
			color = nextword('Color:', content.find_all("div", {"class":"ProductDetails-description"}).text)
		return color

	def limited(content):
		limited = False
		if "limited" in content:
			limited = True
		return limited


	def scrape(baseurl):
		#headers = {'user-agent': 'curl/7.70.0',"Host": "m.jdsports.ie","accept": "*/*","Accept-Encoding": "gzip, deflate, br",}
		#source = requests.get(url, headers=headers).content.decode()

		try:
			sourcepageraw = subprocess.check_output(['curl', '-s', baseurl]).decode()
			if sourcepageraw == "":
				log.set.warning("Warning: page response was empty. Trying second method.")
				sourcepageraw = requests.get(baseurl).content.decode()
				if sourcepageraw == "":
					try:
						log.set.error("Error: page response is still empty with method two.\nExiting...",0)
					except:
						exit(0)
		except:
			log.set.warning("Warning: page returned an error. Trying second method.")

		sourcepage = BeautifulSoup(htmlmin.minify(sourcepageraw.replace("\n","").replace("\t",""),remove_empty_space=True),features="lxml")

		#return {"exist":True,"title":footlocker.title(sourcepage),"price":footlocker.price(sourcepage),"sizes":footlocker.sizes(sourcepage),"instock":footlocker.instock(sourcepage),"colors":footlocker.colors(sourcepage),"limited":footlocker.limited(sourcepage)}
			

		try:
			return {"exist":True,"title":footlocker.title(sourcepage),"price":footlocker.price(sourcepage),"sizes":footlocker.sizes(sourcepage),"instock":footlocker.instock(sourcepage),"colors":footlocker.colors(sourcepage),"limited":footlocker.limited(sourcepage)}
		except Exception as e:
			if sourcepage.find("div",{"class":"Page--productNotFound"}):
				return {"exist":False}
			else:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(f"\n\n{exc_type, fname, exc_tb.tb_lineno}\n\n")
				print("Bug occured. Writting page source to `tmp.source`.")
				with open("tmp.source","w") as f:
					f.write(sourcepageraw)
				print("Leaving...")
				exit(1)
	












#Main scrape FUNCTION

def scrapesneaker(source,url):
	data = {}
	if source == "jdsports":
		data = jdsports.scrape(url)
	elif source == "footlocker":
		data = footlocker.scrape(url)

	if (data == {}):
		log.set.error(f"`{source}` returned no data",0)
	return data

		

def get(url):
	source = ""
	if "jdsports." in url:
		source = "jdsports"


	elif "brownthomas." in url:
		source = "brownthomas"


	elif "footlocker." in url:
		source = "footlocker"

	try:
		result = sneaker(source, url)
		return result
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		log.set.log(f"{exc_type, fname, exc_tb.tb_lineno}\n\n")
		return "error"

	

