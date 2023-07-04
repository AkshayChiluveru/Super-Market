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
Cool Drinks Rs 10/liter
'''


price = 0 
pricelist = []
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
    "Cool Drinks"  :20
}

option = int(input("Press 1 for list of items: "))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if you want to buy press 1 or press 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
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
    

    inp = input("click yes to bill the items else no: ")
    if inp == 'yes':
        pass
    if final_amount != 0:
        for i in range(len(pricelist)):
            print(i,item_list[i],quantity_list[i],price_list[i])
