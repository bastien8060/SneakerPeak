import sneakers as s
import error as log
import pickle, os, sys
from dictdiffer import diff, patch, swap, revert
from time import sleep as delay



try:
	if "-v" in sys.argv[1]:
		os.environ["logging"] = "on"
	else:
		os.environ["logging"] = "off"
except:
	pass

try:
	with open('scan.save', 'rb') as f:
		saves = pickle.load(f)
except:
	print("Initializing for first run.\n")
	saves = {}
	delay(1)



while True:
	try:
		with open('scan.save', 'rb') as f:
			saves = pickle.load(f)
	except:
		pass

	urls = ["https://www.footlocker.ie/en/product/nike-air-vapormax-evo-menshoes/314206438104.html","https://m.jdsports.ie/product/white-nike-dunk-high-retro/16070128_jdsportsie/","https://www.footlocker.ie/en/product/~/316160325904.html","https://www.footlocker.ie/en/product/~/316700300904.html","https://www.brownthomas.com/brown-thomas-navigation-catalog/air-max-90-trainers/1000327103.html"]

	for url in urls:
		sneaker = s.get(url)



		if sneaker == "error":
			 break
		if sneaker.exist:
			if url not in saves:
				print("New Link never seen.")
				saves[url] = sneaker.obj
			else:
				for i in list(diff(saves[url],sneaker.obj)):  
					if (i[0] == 'change'):
						if i[1] == "sizes" or "instock" or "exist" or "limited":
							print("\n\n\n\nNew drop!")
							print(sneaker.obj)
							print(f"product name is `{sneaker.title}`")
							print(sneaker.url) 
						else:
							print(f"\n\n\n{i[1]} changed to {i[2][1]}")  
							print(sneaker.obj) 
							print(f"product name is `{sneaker.title}`")  
							print(sneaker.url) 
					elif (i[0] == 'add'):
						print("\n\n\n\nNew Drop!")
						print(sneaker.obj)
						print(f"product name is `{sneaker.title}`")
						print(sneaker.url) 
					else:
						print(i)
					#print(i)
				saves[url] = sneaker.obj





			

			log.set.log(f"source is `{sneaker.source}`")

			log.set.log(f"price is `{sneaker.price}`")

			log.set.log(f"colors: `{sneaker.colors}`")

			log.set.log(f"sizes are:")
			for i in sneaker.sizes:
				log.set.log(f"	- Size {i}")

			if sneaker.limited:
				log.set.log("Those sneakers are Limited!")

			if sneaker.instock:
				log.set.log("Those sneakers are in stock!")
			else:
				log.set.log("Those sneakers are not in stock!")
		else:
			if url in saves:
				del saves[url]
			log.set.log(f"url is `{sneaker.url}`")
			log.set.log(f"source is `{sneaker.source}`")
			log.set.warning("The page doesn't exist anymore!")
			log.set.log("\033[93mOut of stock\033[0m")

		with open('scan.save', 'wb') as f:
			pickle.dump(saves, f)









		log.set.log("\n________________________________________________________________________________\n")


with open('scan.save', 'wb') as f:
	print("\nSaving before exiting...")
	delay(1)
	pickle.dump(saves, f)

"""
if sneaker.exist:
		print(f"product name is `{sneaker.title}`")

		print(f"source is `{sneaker.source}`")

		print(f"price is `{sneaker.price}`")

		print(f"colors: `{sneaker.colors}`")

		print(f"sizes are:")
		for i in sneaker.sizes:
			print(f"	- Size {i}")

		if sneaker.limited:
			print("Those sneakers are Limited!")

		if sneaker.instock:
			print("Those sneakers are in stock!")
		else:
			print("Those sneakers are not in stock!")
	else:
		print(f"url is `{sneaker.url}`")
		print(f"source is `{sneaker.source}`")
		log.set.warning("The page doesn't exist anymore!")
		log.set.warning("Out of stock")
"""


