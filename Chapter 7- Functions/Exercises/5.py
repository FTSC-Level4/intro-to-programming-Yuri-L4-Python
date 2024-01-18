
#Create new function that takes two argument, a (city) and a default value (Australia)
def describe_city(city, country = "Australia"):
    print(f"{city} is located in {country}.")

#Print out "Athens" as the value of city
describe_city("Canberra")

#Replace the values of the argument, city and country
describe_city("Beijing", "China")
describe_city("Manila", "Philippines")