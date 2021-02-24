# Write a function that works out the total discount available
# if the user gives you the item price and sale %. 
# Return the answer in a string.
# 05/01/2021
# joey tierney

def itemDisc(price, percent):
	discount = price * (percent / 100)

	return round(discount, 2)

itemPrice = float(input("Please enter items price: €"))
salePerc = float(input("Please enter the discount percentage: %"))
discount = itemDisc(itemPrice, salePerc)

print("\nYour item discount is €" + str(discount))