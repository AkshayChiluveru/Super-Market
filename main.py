from datetime import datetime

name = input("Enter Your Name: ")


# List of Items to be displayed in the super market: 
lists = '''
mangoes     Rs 50/each
Chocolates  Rs 20/each
Rice        Rs 15/kg
Colgate     Rs 10/each
Oil         Rs 10/liter
paneer      Rs 10/kg
maggi       Rs 10/kg
Complan     Rs 10/kg
Chips       Rs 10/each
cool Drinks Rs 10/liter
'''


price = 0 
price_list = []
total_price = 0
final_price = 0
item_list = []
quantity_list = []
price_list = []
 

# rates for each items: 
items = {
    "mangoes"      :50,
    "Chocolates"   :20,
    "Rice"         :15,
    "Colgate"      :40,
    "Oil"          :200,
    "paneer"       :75,
    "maggi"        :20,
    "Complan"      :100,
    "Chips"        :10,
    "cool Drinks"  :20
}

option = int(input("Press 1 for list of items: "))
if option == 1:
    print(lists)
for i in range(len(items)):
    input1 = int(input("if you want to buy press 1 or press 2 for exit: "))
    if input1 == 2:
        break
    if input1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            price = quantity*(items[item])
            price_list.append((item,quantity,items,price))
            total_price += price
            item_list.append(item)
            quantity_list.append(quantity)
            price_list.append(price)
            gst = (total_price*5) / 100
            final_amount = gst + total_price
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered wrong number")
    
    
