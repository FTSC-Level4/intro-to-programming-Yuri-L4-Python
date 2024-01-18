#create a guest list for a dinner
Guests = ["Jennie", "Jisoo", "Rose", "Lisa"]

#create a loop that prints an invitation to every person in the guests list
for person in Guests:
    print(f"{person}, you are invited to a dinner at my place.")

#Jennie cant come to dinner
print(f"\nIt seems like {Guests[0]} can't make it to dinner.")

#Replace Jennie with Denise Julia 
Guests[0] = "Denise Julia"

#n for extra space
print("\n")

#Make another loop that prints out the newly updated List with Denise Julia
for person in Guests:
    print(f"{person}, you are invited to a dinner at my place.")