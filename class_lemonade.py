
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
    print('\n\nYou will raise funds with your lemonade stand for', game_days, 'days ')
    nt()
    print('and you will start with', money.inventory, "to purchase supplies before you get started")
    nt() 
    print("Sales may vary between about $75-250")

def days_init():

    global game_days
    start_funds = [20, 30, 40]
    game_days = days[selection-1]
    money.inventory = start_funds[selection-1]

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
    while game_days >=0 :
        game_main()     

### Game Intro Program
def intro_main():
  print("Customer: Yo! We Need to Raise MONEY!!\nThe Big HOmie got locked up Ya feel\n")
  nt2()
  print("I heard ya'll could, Help\n")
  nt2()

  print("Do we Wanna help Big Sm0keZ?\n\n")
  time.sleep(1)
  print("1) yes \n2) no\n\n")
  nt2()

  got_that = int(input("Select 1 or 2\n\n:  "))
  nt2()

  if got_that == 1:
    duration_main()
  elif got_that != 1 or 2:
    while True:
       print("FUCK YOU DAWG....")

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

perfect_recipe = [12, 6, 2, 50]
default_recipe = [12, 4, 1, 25]
player_recipe = [0, 0, 0, 0]

days_sales = random.randint(40, 140)

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

    def loss(items):
        items.inventory = int(items.inventory / item_loss)

    def purchase(items):
        items.inventory = new_inventory = int(items.inventory + items.quantities[item_choice-1])

        #items.inventory[0:3]
        #items.inventory = random.choice(inventory)/0.5
        
cups = Item('cups', cup_prices, cup_quants, 0)
lemons = Item('lemons', lemons_prices, lemons_qaunts, 0)
sugar = Item('sugar', sugar_prices, sugar_quants, 0)
ice = Item('ice', ice_prices, ice_quants, 0)
money = Item('money', days_sales, None, [60, 70, 120])
recipe = Item('Recipe', default_recipe, perfect_recipe, 0) 
items = [cups.item, lemons.item, sugar.item, ice.item, money.item]
inventory =  [cups.inventory, lemons.inventory, sugar.inventory, ice.inventory, money.inventory]
extras = ['', 'squeezed', "cups", "cubes" ]
"""
ice.inventory = 20
ice.apply_loss()
print(ice.inventory)
ice.melt()
print(ice.inventory
print(money.prices)  
print(ice.purchase_prompt())
# Inventory Functions
class Purchasing(Item):
    def __init__(purchase, ):
"""

def buyer_input():
    global b_input
    b_input = int(input(": "))

# Inventory Interface Functions
def Inventory_init(): 
   global choice, selection
   nt()
   print('It’s time to buy inventory…')
   nt()
   print('Please use 1, 2, 3, or 4 to select one of the following options:\n1)', cups.item, '\n2)', lemons.item, '\n3)', sugar.item, '\n4)', ice.item)
   buyer_input()
   selection = b_input
   choice = items[selection-1]
   

def purchase_select():
     print('Please use 1, 2, or 3 to select a option')
     nt()

def selected_purchase():
    nt()
    '{} {}'.format('You have selected' ,choice)
    nt()

def inventory_interface():
   if cups.item == choice:
       selected_purchase()
       purchase_select()
       print('1)',cups.quantities[0], choice, 'for', cups.prices[0], '\n2)', cups.quantities[1], choice, 'for', cups.prices[1], '\n3)', cups.quantities[2], choice, 'for', cups.prices[2])
       nt2()
       buyer_input()
       purchasing()
       buy_more()
   elif lemons.item == choice:
       selected_purchase()
       purchase_select()
       print('1)', lemons.quantities[0], choice, 'for', lemons.prices[0], '\n2)', lemons.quantities[1], choice, 'for', lemons.prices[1], '\n3)', lemons.quantities[2], choice, 'for', lemons.prices[2])
       nt2()
       buyer_input()
       purchasing()
       buy_more()
   elif sugar.item == choice:
       selected_purchase()
       purchase_select()
       print('1)', sugar.quantities[0], 'lbs', choice, 'for', sugar.prices[0], '\n2)', sugar.quantities[1], 'lbs', choice, 'for', sugar.prices[1], '\n3)', sugar.quantities[2], 'lbs', choice, 'for', sugar.prices[2])
       buyer_input()
       purchasing()
       buy_more()
   elif ice.item == choice:
       selected_purchase()
       purchase_select()
       print('1)', ice.quantities[0], choice, 'cubes for', ice.prices[0], '\n2)', ice.quantities[1], choice, 'cubes for', ice.prices[1], '\n3)', ice.quantities[2], choice, 'cubes for', ice.prices[2])
       nt2()
       buyer_input()
       purchasing()
       buy_more()       
   else:
       bad_choice()
       Inventory_init()
       
# Purchasing State Change Functions
def purchasing():
    global inventory
    item_choice = b_input
    if cups.item == choice:
         inventory[selection-1] += cups.quantities[item_choice-1]
         money.inventory -= cups.prices[item_choice-1]
    elif lemons.item == choice:
         inventory[selection-1] += cups.quantities[item_choice-1]
         money.inventory -= lemons.prices[item_choice-1]
    elif items[2] == choice:
         inventory[selection-1] += sugar.quantities[item_choice-1]
         money.inventory -= sugar.prices[item_choice-1]
    elif items[3] == choice:
         inventory[selection-1] += ice.quantities[item_choice-1]
         money.inventory -= ice.prices[item_choice-1]
    else:
        bad_choice()
        purchasing()
    
def buy_more():
    t()
    print("\n\nYou now have", inventory[selection-1], choice, 'and', '$', money.inventory, 'left to spend')
    print("\n\nPlease use 1, 2 or 3 to select from the following options:\n1) Purchase more:", choice, "\n2) Select another item for purchase", "\n3) Make Lemonade!")
    buyer_input()
    if b_input == 1:
         inventory_interface()
    elif b_input == 2:
        inventory_main()
    elif b_input == 3:
        main_recipe()
    else:
        print("Please select a valid option")
        buy_more()

def recipe_method():
    recipe_mod = [1.25, 1.5, 1.75, 2]
    global sales
    sales = days_sales
    if player_recipe[1] == 6 and player_recipe[2] == 2 and player_recipe[3] == 50  :
        sales = recipe_mod[3] * sales
    elif ((player_recipe[1] > 6 and player_recipe[1] <= 8) or (player_recipe[1] < 6 and player_recipe[1] >= 4)) and (player_recipe[2] >=1 or  player_recipe[2] <= 4) and (player_recipe[3] >= 25 and player_choice <= 75):
        sales = recipe_mod[1] * sales
    elif player_recipe == default_recipe:
        sales *= recipe_mod[0]
    else:
        sales = sales / recipe_mod[3]

def main_recipe():
    recipe_opts = ["Would you like to use the default recipe?", "Would you like to make a custom recipe?", "Quick Start"]
    purchase_select()
    for i in range(1, 4):
        print(str(i)+ ")", recipe_opts[i-1] )
        nt2()
    buyer_input()
    recipe_select()
    
def defrecipe_prompt():
    global player_recipe
    print("The default recipe uses the following:" )
    for i in range(1, 4):
        print(items[i] ," : ", default_recipe[i], extras[i] )
    print("Would you like to use this recipe?\n1) Yes\n2) No")
    buyer_input()
    if b_input == 1:
        player_recipe = default_recipe
        game_main()
    elif b_input == 2:
        main_recipe()
    else:
        bad_choice
        defrecipe_prompt()

def pitcher_interface():
    global pitchers_made
    pitcher_prompts = ["Here at the stand we make our lemonade by the pitcher.", "A pitcher makes twelve cups.","How many pitchers of lemonade would you like to make?","Its time to make some lemonade!\nLets hope it turns out GUCCI"]
    for i in range(0, len(pitcher_prompts)):
        print(pitcher_prompts[i])
        nt()
    buyer_input()
    pitchers_made = b_input
    

 
def pitcher_calculations():
    global item_loss
    for i in range(0, len(inventory)-1):
        item_loss[i] = item_loss[i]*pitchers_made
        enough_inventory()

def inventory_loss():
    global inventory
    
    for i in range(0, len(item_loss)-1):
        inventory[i] -= item_loss[i]
        return inventory

def pitchers_main():
    pitcher_interface()
    enough_inventory()
    pitcher_calculations()




def enough_inventory():
    global item
    item_loss = player_recipe
    for i in range(0, len(player_recipe)):
        if (inventory[i]- item_loss[i]) <= 0:
            print("You do not have enough", items[i], "to make", str(pitchers_made), "pitchers of lemonade." )
            print("Please select a different amount of ingredients and/or amount of pitchers made")
            not_enough()
        else:
            print(pitcher_prompts[3])
        
 
def not_enough():
    options = ["Chose another recipe", "Make less pitchers", "Buy more inventory"]
    purchase_select()
    for i in range(0 ,len(options)):
        print(str(i+1)+")", options[i])
    buyer_input()
    selection = b_input
    if selection == 1:
        main_recipe()
    elif selection == 2:
        pitcher_interface()
    elif selection == 3:
        inventory_main()
    else:
        bad_choice()
        not_enough()

def recipe_interface():
    nt2()
    global player_recipe
    for i in range(1, len(player_recipe)):
        print("\nHow many", items[i], "would you like to use in your recipe?")
        buyer_input()
        player_recipe[i] = b_input

def recipe_select():
    selection = b_input
    if selection == 1:
        defrecipe_prompt()        
    elif selection == 2:
        recipe_interface()
    elif selection == 3:
        inventory_main()
    #elif selection == 4:
        #game_start()
    else:
        bad_choice()
        recipe_interface()
   

# MAIN INVENTORY function
def inventory_main():
    Inventory_init()
    inventory_interface()

### Weather Program
# Global Weather Variables
weather_condition = " "
weather_sales = 0.0
weather = ["Ice Ice Baby", "Raining cats and dogs", "Its just a little nipply outside", "Perfect", "Oh my lord, somebody call the fire department."]
weather_effect = [ 1.2, 1.1, 1.3, 1.5, 1.7]

def weather_output():
  '{} {} {} {}'.format("Today's weather is", weather_condition, "\nThe effect on sales will be: ", weather_sales )

def weather_v2():
    global weather_sales
    weather_sales = random.choice(weather_effect)
    weather_output()

def weather_v1():
   global weather_condition, sales, Random_temp
   Random_temp = random.randint(20, 120)
   if (Random_temp >= 20) and (Random_temp < 40):
      weather_condition = weather[0]
      sales /= weather_effect[3]
   elif (Random_temp > 40) and (Random_temp < 53):
      weather_condition = weather[2]
      sales /= weather_effect[1]
   elif (Random_temp > 53) and (Random_temp < 68):
      weather_condition = weather[2]
      sales *= weather_effect[2]
   elif (Random_temp >= 68) and (Random_temp < 86):
      weather_condition = weather[3]
      sales *= weather_effect[3]
   else:
      weather_condition = weather[4]
      sales *= weather_effect[4]

# Game Start

def preday_calcs():
    inventory_loss()

def game_main():
    game_prompts = [ "Reselect Day's Reicipe ", "Purchase inventory", "Simulate Days Sales"]
    print("We bout to start selling lemonade for the day, Are you ready or do you want to select another option?")
    purchase_select()
    for i in range(0, 3):
       print(i + 1,')', game_prompts[i])
    buyer_input()
    day_starto

   
def day_starto():
    selection = b_input
    if selection == 1:
        game_stprompt()
        calculate_sales()       
    elif selection == 2:
       inventory_interface()
    elif selection == 3:
        recipe_interface()
    else:
        bad_choice()
        game_starto()


def game_stprompt():
    day_prompts = ["Whoop whooop, time to get the day started.", " Damn here goes another day." , " TIme to get the party stared." , "Ghoul Life Baby!"]
    purchase_select()
    day_prompt = random.choice(day_prompts)
    prompt = print("Calculating Days Sales now!....")
    i = 0
    for i in range(0, 10):
        print(prompt)
        nt()


 # WEATHER MAIN

def weather_main():
    weather_v1()
    weather_output()

### MAIN PROGRAM

def main():
   
    intro_main()
    inventory_main()
    pitchers_main()
    game_main()


     
### PROGRAM START

main()