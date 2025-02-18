menu = ["Coffee", "Tea", "Hot Chocolate", "Mugs"]

stock = {"Coffee": 15,
         "Tea": 20,
         "Hot Chocolate": 10,
         "Mugs": 16
         }

price = {"Coffee": 42.50,
         "Tea": 33.20,
         "Hot Chocolate": 30.0,
         "Mugs": 160
         }

total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print(total_stock)
