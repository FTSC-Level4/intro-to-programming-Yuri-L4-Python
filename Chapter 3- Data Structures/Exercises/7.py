#create list of places I want to visit
Places = ["South Korea", "Japan", "Switzerland", "France", "Italy"]

#print List
print("Original: ")
print(Places,"\n")

#print the list using "sorted()" to make it alphabetical
print("Alphabetical: ")
print(sorted(Places),"\n")

#print the original list to show that no changes are made with the List
print("Original: ")
print(Places, "\n")

#print the list using "sorted()" and "reverse = true" to make it reversed alphabetical
print("Reverse Alphabetical: ")
print(sorted(Places, reverse = True), "\n")

#print the original list to show that no changes are made with the list
print("Original: ")
print(Places, "\n")

#print the list using the function .reverse() to reverse the original list
print("Reversed: ")
Places.reverse()
print(Places, "\n")

#print again with .reverse to bring it back to original order
print("Original: ")
Places.reverse()
print(Places, "\n")

#use sort to replace the original list into alphabetical order
print("Alphabetical: ")
Places.sort()
print(Places, "\n")

#use sort to replace the original list into reverse alphabetical order
print("Reverse Alphabetical: ")
Places.sort(reverse = True)
print(Places)
