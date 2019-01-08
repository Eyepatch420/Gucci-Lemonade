
###
# Authors = [“l33tH@x0rGh0ul”,”l33tH@x0rcritikal”, “l33tH@x0rn0Mz” ] 
# 
# Description:  This script is on Ghouls azure server. Please send your Full Legal Name and 
#                      and Social Security Number to confirm download.
# Notes: THIS SCRIPT IS ON THE SERVER AND CURRENTLY RUNS WITHOUT ERROR!!!!
#             Correctly captures user input and prints the function that needs to be built as output to 
#             screen.
# TIP: FYI if you dont know what something means GOOGLE. If you dont know how to print to
#         screen or create a class in python, GOOGLE it takes about 2 minutes to find an answer. 
#         Don’t be a mouth breather. Also to help with the understanding of the examples given
#         please mentally read and understand any “equal signs” or “=” as blank IS ASSIGNED
#         the value of. 
#         ex.
#             x = 10          # This would read x IS ASSIGNED the value of 10
#

"""

### GUCCI LEMONADE
Note to User
  > Copy and paste the text from this doc into notepad or the ide of your chose and save the file
  	As a  filename.py
  > To run type python3 filename.py if in a bash terminal. If using windows you may or may not
 	Need to download python or use an ide.
  > This is an open source file and you are free to modify a copied file as you please.
  > You may distribute this content so long as you cite leave the authors portion up top intact.
  	IF YOU FAIL TO COMPLY YOU ARE A HUGE FUCKING DUESH, YOU WILL GET
  	*INFECTED*():RANSOMWARE>>YOU
  > If using this template for class only remove the authors section upon turning in the assignment.
   
Thank you and enjoy *_* L33tH@x0rGh0ul

Overall Project Flow

  1) DAYS:
   a> define the three possible number of days options as one variable
   b> Use a function to randomize between those choices
	- Hint: Use fucking google and stop being a spoon fed brat. I'll give you
  	this one. Type python3 random number function in your google search bar.
  	Your'll be amazed at your own ability. Literally if you dont know how to
  	do a ... DONT PANIC just copy EXACTLY what i typed and guess what paste it
  	in , yup, you guessed it. Google
.
2) RECIPE
   > l33tH@x0rcritikal
   > Possible class implementation

Ingredients = [ice, 
   class recipe:
       def popularity()
       def make_recipe()

3) PURCHASING
  > This can also be constructed of the array of items used in recipe. Optimimally we create a 
     Class representing something similar to the following for purchasing 
     Ex: class ____   = [ current_quant, order_quant, prices]
     
  
4) INVENTORY
   > Inventory is constructed from the recipe since the same variables for the items are used. 
      The recipe direcly influences INVENTORY. RECIPE tells us what items are needed for one
      batch.  It also will tell use what values we need to subtract from inventory. 
   > ex. 
     INVENTORY = PURCHASE   # Note this is the first inventory 
     INVENTORY = INVENTORY + PURCHASE
5)

   




"""
# Import Modules

import time
import random


### Game Duration Program

days = [7, 14, 30]
game_days = 0

def duration_intro():
    print("\n\nSo you've decided to open up a lemonade stand to help FREE the big HOMIE lil j0k3r.")

def days_prompt():
    print('\n\nYou will raise funds with your lemonade stand for', game_days, 'days.')

def days_init():
    global game_days
    game_days = days[selection-1]

def days_selection():
    days_init()
    days_prompt()

def opt_4():
    global game_days
    game_days = random.choice(days)
    days_prompt()


def duration_prompt():
    print("\n\nPlease use 1, 2, 3, 4 to select from the folowing options," , '\n\n1)' , days[0], '\n2)', days[1], '\n3)', days[2], '\n4) Random duration')
    buyer_input()

def duration_select():
    global selection
    selection = b_input
    if selection == 1:
        days_selection()
    elif selection == 2:
        days_selection()
    elif selection == 3:
        days_selection()
    elif selection == 4:
        opt_4()
    else:
        bad_input()
        duration_select()

def duration_main():
     duration_intro()
     duration_prompt()
     duration_select()
 


def duration_init():
    while game_days >=0:
        game_main()



      

### Game Intro Program
def intro_pt2():
  print("Customer: Yo! I need that GUCCI LEMONADE man!!!\n\n")
  time.sleep(1)
  print("I heard ya'll got that, \nDo you got that homie\n\n")
  time.sleep(1)

  print("Do we got that GUCCI LEMONADE?\n\n")
  time.sleep(1)
  print("1) yes \n2) no\n\n")
  time.sleep(1)

  got_that = int(input("Select 1 or 2\n\n:  "))
  time.sleep(1)

  if got_that == 1:
    print("recipe() goes here\n\n")
  elif got_that != 1 or 2:
    print("error_chk() goes here")

# Global Recipe Variables

## Miscellaneous Functions

# New Lines
def n():
    print("\n\n")

def n1():
    print('\n')

# Time Mangement
def t():
    time.sleep(0.5)

def ts():
    time.sleep(1)

def tf():
    time.sleep(0.25)

# Combos

def nt():
    n()
    tf()

def nt2():
    n1()
    tf()

# Bad Input 
def bad_choice():
    print("\n\nPlease select a valid option")
                 
def bad_input():
    bad_choice()
    buyer_input()



#Method Version ???

def bad_selection():
    def bad_choice():
        print("Please select a valid option")
                 
    def bad_input():
        bad_choice()
        buyer_input()
    return bad_choice, bad_input

bad_choice, bad_input = bad_selection()


## INVENTORY

# Inventory Variables


items = ['cups' , 'lemons', 'sugar', 'ice']
inventory = [0, 0, 0, 0, 0.0] # inventory[4] is money
money = inventory[4]


pitchers_made = 0
recipe_used = [0, 0, 0, 0]


# Purchasing Variables

purchase = 0 
cup_prices = [ 0.75, 1.5, 6.0]
cup_quants = [25, 50, 200]
lemons_prices = [2.5, 5.0, 7.5]
lemons_qaunts = [50, 100, 150]
sugar_prices = [1.5, 2.5, 3.5]
sugar_quants = [15, 25, 35]
ice_prices = [1.5, 3.5, 4.5]
ice_quants = [100, 300, 500]


## Class Practice





def purchase_select():
     print('\n\nPlease use 1, 2, or 3 to select a purchase option')


class Item:

    item_loss = 1.50

    def __init__(items, item, prices, quantities, inventory):
        items.item = item
        items.prices = prices
        items.quantities = quantities
        items.inventory = inventory



    # METHODS


    def purchase_prompt(items):
        return '{} {}'.format("\n\nYou have selected to purchase", items.item)
    
    def melt(items):
        items.inventory = int(items.inventory*0)
"""
    def loss(items):
        items.inventory = int(items.inventory * items.)
"""
        #items.inventory[0:3]
        #items.inventory = random.choice(inventory)/0.5
    
        
cups = Item('cups', cup_prices, cup_quants, 0)
lemons = Item('lemons', lemons_prices, lemons_qaunts, 0)
sugar = Item('sugar', sugar_prices, sugar_quants, 0)
ice = Item('ice', ice_prices, ice_quants, 0)
money = Item('money', None, None, 0)

ice.inventory = 20

print(ice.inventory)
ice.melt()
print(ice.inventory)


"""
print(money.prices)  
print(ice.purchase_prompt())
"""
# Inventory Functions

def buyer_input():
    global b_input
    b_input = int(input(": "))



# Inventory Interface Functions
def Inventory_init(): 
   global choice, selection
   print('\nIt’s time to buy inventory…')
   t()
   print('\n\nPlease use 1, 2, 3, or 4 to select one of the following options:\n1)', items[0], '\n2)', items[1], '\n3)', items[2], '\n4)', items[3])
   buyer_input()

   selection = b_input
   choice = items[selection-1]

def purchase_select():
     print('\n\nPlease use 1, 2, or 3 to select a purchase option')

def inventory_interface():
   if items[0] == choice:
       t()
       print('\n\nYou have selected to purchase' ,choice)
       t()
       print('\n\nPlease use 1, 2, or 3 to select a purchase option')
       t()
       print('\n\n1)', cup_quants[0], choice, 'for', cup_prices[0], '\n2)', cup_quants[1], choice, 'for', cup_prices[1], '\n3)', cup_quants[2], choice, 'for', cup_prices[2])
       t()
       buyer_input()
       purchasing()
       buy_more()
   elif items[1] == choice:
       t()
       print('You have selected to purchase',choice,'\nPlease use 1, 2, or 3 to select a purchase option')
       t()
       print('\n\n1)', lemons_qaunts[0], choice, 'for', lemons_prices[0], '\n2)', lemons_qaunts[1], choice, 'for', lemons_prices[1], '\n3)', lemons_qaunts[2], choice, 'for', lemons_prices[2])
       t()
       buyer_input()
       purchasing()
       buy_more()
   elif items[2] == choice:
       t()
       print('You have selected to purchase',choice,'\nPlease use 1, 2, or 3 to select a purchase option')
       t()
       print('\n\n1)', sugar_quants[0], 'lbs', choice, 'for', sugar_quants[0], '\n2)', sugar_quants[1], 'lbs', choice, 'for', sugar_prices[1], '\n3)', sugar_quants[2], 'lbs', choice, 'for', sugar_prices[2])
       buyer_input()
       purchasing()
       buy_more()
   elif items[3] == choice:
       t()
       print('You have selected to purchase',choice,'\nPlease use 1, 2, or 3 to select a purchase option')
       t()
       print('\n\n1)', ice_quants[0], choice, 'cubes for', ice_prices[0], '\n2)', ice_quants[1], choice, 'cubes for', ice_prices[1], '\n3)', ice_quants[2], choice, 'cubes for', ice_prices[2])
       t()
       buyer_input()
       purchasing()
       buy_more()       
   else:
       print('Please select a valid input')
       Inventory_init()

# Purchasing State Change Functions
def purchasing():
    global inventory
    global money
    item_choice = b_input
    if items[0] == choice:
         inventory[selection-1] += cup_quants[item_choice-1]
         inventory[4] -= cup_prices[item_choice-1]
    elif items[1] == choice:
        inventory[selection-1] += lemons_qaunts[item_choice-1]
        inventory[4] -= lemons_prices[item_choice-1]
    elif items[2] == choice:
        inventory[selection-1] += sugar_quants[item_choice-1]
        inventory[4] -= sugar_prices[item_choice-1]
    elif items[3] == choice:
        inventory[selection-1] += ice_quants[item_choice-1]
        inventory[4] -= ice_prices[item_choice-1]
    else:
        print("Please select a valid option")
        purchasing()
    money = inventory[4]


def buy_more():
    t()
    print("\n\nYou now have", inventory[selection-1], choice, 'and', '$', money, 'left to spend')
    print("\n\nPlease use 1, 2 or 3 to select from the following options:\n1) Purchase more:", choice, "\n2) Select another item for purchase", "\n3) Main game menu")
    buyer_input()
    if b_input == 1:
         inventory_interface()
    elif b_input == 2:
        inventory_main()
    elif b_input == 3:
        print("Game Starto")
    else:
        print("Please select a valid option")
        buy_more()

# MAIN INVENTORY function
def inventory_main():
    Inventory_init()
    inventory_interface()



### Weather Program
# Global Weather Variables
def Weather():
    weather_condition = " "
    weather_sales = 0.0
    weather = ["Ice Ice Baby", "Raining cats and dogs", "Its just a little nipply outside", "Perfect", "Oh my lord, somebody call the fire department."]
    weather_effect = [0.5, 0.2, 0.1, 1.3, 1.7]
    
    def weather_output():
      print("Today's weather is", weather_condition, "\nThe effect on sales will be: ", weather_sales)
    
    
    def weather_v2():
        global weather_sales
        weather_sales = random.choice(weather_effect)
        weather_output()
    
    def weather_v1():
       global weather_condition
       global weather_sales
       Random_temp = random.randint(20, 120)
       if (Random_temp >= 20) and (Random_temp < 40):
          weather_condition = weather[0]
          weather_sales = weather_effect[0]
          weather_output()
    
    
       elif (Random_temp > 40) and (Random_temp < 53):
          weather_condition = weather[1]
          weather_sales = weather_effect[1]
          weather_output()
    
       elif (Random_temp > 53) and (Random_temp < 68):
          weather_condition = weather[2]
          weather_sales = weather_effect[2]
          weather_output()
          
       elif (Random_temp >= 68) and (Random_temp < 86):
          weather_condition = weather[3]
          weather_sales = weather_effect[3]
          weather_output()
    
       else:
          weather_condition = weather[4]
          weather_sales = weather_effect[4]
          weather_output()
    return weather, weather_condition, weather_effect, weather_output, weather_sales, weather_v1, weather_v2

weather, weather_condition, weather_effect, weather_output, weather_sales, weather_v1, weather_v2 = Weather()

# WEATHER MAIN

def weather_main():
    weather_v1()
    weather_output()

### MAIN PROGRAM

def main():
    #game_intro()
    duration_main()
    weather_main()
    inventory_main()


### PROGRAM START

main()