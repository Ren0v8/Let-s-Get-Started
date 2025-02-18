# establish a menu
menu = ["Coffee", "Tea", "Hot Chocolate", "Mugs"]

# fill in the stock list
stock = {"Coffee": 15,
         "Tea": 20,
         "Hot Chocolate": 10,
         "Mugs": 16
         }

# add in the pricing for the stock
price = {"Coffee": 42.50,
         "Tea": 33.20,
         "Hot Chocolate": 30.0,
         "Mugs": 160
         }

# set stock to 0
total_stock = 0

# calculate total stock value for items in stock
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print(total_stock)
