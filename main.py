import sneakers as s
import error as log
import pickle, os, sys
from dictdiffer import diff, patch, swap, revert
from time import sleep as delay
import findsneakers as peaker



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
	print("Initializing scan list for first run.\n")
	saves = {}
	delay(1)

try:
	with open('url.save', 'rb') as f:
		urls = pickle.load(f)
except:
	print("Initializing url list for first run.\n")
	urls = []
	delay(1)



while True:
	try:
		with open('scan.save', 'rb') as f:
			saves = pickle.load(f)
	except:
		pass


	urls = peaker.find(urls)


	for url in urls:
		sneaker = s.get(url)

		if sneaker == "error":
			 break
		if sneaker.exist:
			if url not in saves:
				print("New Link never seen.")
				saves[url] = sneaker.obj
			else:












				if saves[url] != sneaker.obj:
					print("!")
					print("\n________________________________________________________________________________")
				for i in list(diff(saves[url],sneaker.obj)):  
					#print("\n\ndiff\n\n")
					if (i[0] == 'change'):
						if i[1] == "sizes" or i[1] == "instock" or i[1] == "exist" or i[1] == "limited":
							print("\n\n\n\nNew drop!")
							print(f"\n\n\n{i[1]} changed to {i[2][1]}") 
							print(f"before: {saves[url][i[1]]}")
							print(f"after: {sneaker.obj[i[1]]}")
							print(f"product name is `{sneaker.title}`")
							print(sneaker.url) 
						else:
							print(f"\n\n\n{i[1]} changed to {i[2][1]}")
							try:
								print(f"before: {saves[url][i[1][0]]}")
							except:
								print(f"before: {saves[url][i[1]]}")
							try:
								print(f"after: {sneaker.obj[i[1][0]]}")
							except:
								print(f"after: {sneaker.obj[i[1]]}")
							print(f"product name is `{sneaker.title}`")  
							print(sneaker.url) 
					elif (i[0] == 'add'):
						print("\n\n\n\nNew Drop!")
						print(i[1],"added!",i[1],"is",i[2][0][1])
						print(f"before: {saves[url][i[1]]}")
						print(f"after: {sneaker.obj[i[1]]}")
						print(f"product name is `{sneaker.title}`")
						print(sneaker.url) 
					else:
						print(i)
					#print(i)
				saves[url] = sneaker.obj









			log.set.log(f"product name is `{sneaker.title}`")

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
			#if url in saves:
				#del saves[url]
			log.set.log(f"url is `{sneaker.url}`")
			log.set.log(f"source is `{sneaker.source}`")
			log.set.warning("The page doesn't exist anymore!")
			log.set.log("\033[93mOut of stock\033[0m")
			print("。",end="")

		with open('scan.save', 'wb') as f:
			pickle.dump(saves, f)

		with open('url.save', 'wb') as f:
			pickle.dump(url, f)








		print(".",end="")
		sys.stdout.flush()
		log.set.log("\n________________________________________________________________________________\n")



with open('scan.save', 'wb') as f:
	print("\nSaving before exiting...")
	delay(1)
	pickle.dump(saves, f)

with open('url.save', 'wb') as f:
	pickle.dump(urls, f)

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


