from bs4 import BeautifulSoup

def find(urls):
	results = ["http://127.0.0.1/virt/footlocker.ie/1/index.html","https://www.footlocker.ie/en/product/nike-air-vapormax-evo-menshoes/314206438104.html","https://m.jdsports.ie/product/white-nike-dunk-high-retro/16070128_jdsportsie/","https://www.footlocker.ie/en/product/~/316160325904.html","https://www.footlocker.ie/en/product/~/316700300904.html","https://www.footlocker.ie/en/product/~/314520929804.html","https://www.footlocker.ie/en/product/~/314520925604.html","https://www.footlocker.ie/en/product/~/314103840204.html","https://www.footlocker.ie/en/product/~/314103839404.html"]
	for url in results:
		if url not in urls:
			urls.append(url)

	return urls


