
#create list of sandwich orders
sandwich_orders = ["Tuna Sandwich", "Egg Sandwich", "Chocolate Sandwich", "Bacon Sandwich"]

#create empty list of finished sandwiches
finished_sandwiches = []

#loops through the list
while sandwich_orders:
    #.pop removes the specific item from a collection
    sandwich = sandwich_orders.pop()
    print(f"I am making your {sandwich}.")
    #.append adds the sandwich to the empty list of finished sandwiches
    finished_sandwiches.append(sandwich)
    
print("\n")

#for every sandwich in the list finished_sandwiches
for sandwich in finished_sandwiches:
    #Print this
    print(f"I made your {sandwich}.")