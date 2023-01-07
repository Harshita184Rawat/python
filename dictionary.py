# A dictionary is used to store a bunch of key value pairs
# Name: xyz
# Email: xyz23@gmail.com
# Phone: 1029...
Details = {
    "name": "Jhon Smith",
    "age": 30,
    "is_verified": True
    
}
# to access each item from dictionary
print(Details["name"])
# get method
print(Details.get("age"))
# print(Details.get("birthdate")) : 
# this returns None which represents absense of a value
print(Details.get("birthdate", "April 18 2002")) # passing default value
# updating a key
Details["name"]="Jack"
print(Details["name"])
# adding new key value pair to dictionary
Details["Date_of_birth"] = "Jan 1 1989"
