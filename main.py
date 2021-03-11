import sneakers as s
import error as log


urls = ["https://www.footlocker.ie/en/product/nike-air-vapormax-evo-menshoes/314206438104.html","https://m.jdsports.ie/product/white-nike-dunk-high-retro/16070128_jdsportsie/","https://www.footlocker.ie/en/product/~/316160325904.html","https://www.footlocker.ie/en/product/~/316700300904.html","https://www.brownthomas.com/brown-thomas-navigation-catalog/air-max-90-trainers/1000327103.html"]

for url in urls:
	sneaker = s.get(url)
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




	print("\n\n")