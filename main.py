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