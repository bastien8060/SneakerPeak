# SneakerPeak
Scrapes Sneaker selling websites.

## Support

Only should work on Linux. This was never tested under Windows.

Only scrapes the data off the website for now. Supported websites:  
- https://www.jdsports.ie/
- https://www.footlocker.ie/

Website to be supported soon:
- www.brownthomas.com/ 

This collects from the website:

| Data  | Notes |
| ------------- | ------------- |
| The source (Website name) | |
| The item's price (In Euro)  | |
| The shoes' available size | (Does so inconsistently between UK and EU sizes for now. To be fixed.) |
| Wether or not it is in stock  | |
| Wether or not it is labeled as a limited pair/edition. | |
| The pair's color | |

## Demo

Sample output for this list of urls: 
- "https://www.footlocker.ie/en/product/nike-air-vapormax-evo-menshoes/314206438104.html
- https://m.jdsports.ie/product/white-nike-dunk-high-retro/16070128_jdsportsie/
- https://www.footlocker.ie/en/product/~/316160325904.html
- https://www.footlocker.ie/en/product/~/316700300904.html
- https://www.brownthomas.com/brown-thomas-navigation-catalog/air-max-90-trainers/1000327103.html"]

Output:

Warning: page response was empty. Trying second method.<br>
product name is `Nike Air Vapormax Evo - Men Shoes`<br>
source is `footlocker`<br>
price is `€224.99`<br>
colors: `Black`<br>
sizes are:<br>
	- Size 40<br>
	- Size 41<br>
	- Size 42<br>
	- Size 42.5<br>
	- Size 43<br>
	- Size 44<br>
	- Size 45<br>
	- Size 46<br>
Those sneakers are in stock!<br>


---


product name is `Nike Dunk High Retro`<br>
source is `jdsports`<br>
price is `€110.00`<br>
colors: `White`<br>
sizes are:<br>
	- Size 8<br>
	- Size 13<br>
Those sneakers are Limited!<br>
Those sneakers are in stock!<br>


---


product name is `Nike Tuned 1 Essential - Baby Shoes`<br>
source is `footlocker`<br>
price is `€79.99`<br>
colors: `Black`<br>
sizes are:<br>
	- Size 21<br>
	- Size 22<br>
	- Size 23,5<br>
	- Size 25<br>
	- Size 26<br>
	- Size 27<br>
Those sneakers are in stock!<br>


---


url is `https://www.footlocker.ie/en/product/~/316700300904.html`<br>
source is `footlocker`<br>
The page doesn't exist anymore!<br>
Out of stock<br>


---


`brownthomas` is not yet implemented!
