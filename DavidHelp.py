

# The GucciLemon Game
# Cisp#Team_Arrays_Start_@_Onerog1 with Professor Gary Patton
# Team Members Phillip, Victor, David, Skye
# Due 12/10/18
#
###

# Imports
import random
import time

# Inventory Variables

items = ['cups' , 'lemons', 'sugar', 'ice']
inventory = [0, 0, 0, 0]

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
"""
class purchase_items:
    item_prices[0.0, 0.0, 0.0]
    item_quant [0, 0, 0]
    


"""

def Inventory(): 
   global choice
   print('\nIt’s time to buy inventory…')
   time.sleep(1)
   print('\n\nPlease use 1, 2, 3, or 4 to select one of the following options:\n1)', items[0], '\n2)', items[1], '\n3)', items[2], '\n4)', items[3])
   selection = int(input(':  '))
   choice = items[selection-1]
   if items[0] == choice:
       print('purchasing')
   elif items[1] == choice:
       print('purchasing')
   elif items[2] == choice:
       print('purchasing')
   elif items[3] == choice:
       print('purchasing')
   else:
       print('Please select a valid input')
       Inventory()





def purchasing_display():
    global purchase
    time.sleep(1)
    i = 0
    print(choice,'Is available in the following options\n',)
    while i <= 2:
      print(choice,'Is available in the following options\n1)', cup_quants[i], 'for', cup_prices[i],'\n')
      i += 1
      

#    print('You have selected', item[selection-1], 'for purchasing.', item[selection-1], 'is available for purchase in the following quantities\n')
 #   print('1)', )




Inventory()
