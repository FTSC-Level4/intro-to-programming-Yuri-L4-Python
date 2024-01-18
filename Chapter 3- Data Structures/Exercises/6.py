#create a guest list for a Dinner
Guests = ["Jennie", "Jisoo", "Rose", "Lisa"]

#create a loop that prints an invitation to every person in the guests list
for person in Guests:
    print(f"{person}, you are invited to a dinner at my place.")

#Jennie cant come to dinner
print(f"\nIt seems like {Guests[0]} can't make it to dinner.")

#Replace Jennie with denise Juulia
Guests[0] = "Denise Juiia"

#n for extra space
print("\n")

#create another loop that prints out the newly updated list with Denise Julia
for person in Guests:
    print(f"{person}, you are invited to a dinner at my place.")

#ran out of space for 2 more people
print("\nOh no! We only have space for two people!")

#remove 2 other guests by using the pop function which removes the guest from the list
name = Guests.pop()
print(f"\nI apologize {name}, we ran out of space at the table.")

name = Guests.pop()
print(f"I apologize {name}, we ran out of space at the table.")

#create another loop to print the updated list that contains only 2 guests
for person in Guests:
    print(f"{person}, you are still invited to a dinner at my place.")

#delete the guests in the list to have an empty list and print out to confirm
del(Guests[0])
del(Guests[0])
print(Guests)
