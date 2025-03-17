# Assignment No 03

# Part 2: List, Tuples, and Dictionary

# other parts included in controlflow.py and sets.py

# topic included in part 2:

    # 1. Lists (included methods)
    # 2. Tuples (included methods)
    # 3. Dictionary (included methods)

# 1 - Lists (included methods):

# lists in python:
#A list is an ordered, mutable (changeable) collection of items in Python, enclosed in square brackets [ ], and can store multiple data types (numbers, strings, other lists, etc.

#list
user_info = ["Khadija", 20, 5.1, True ]


#Accessing List Elements ny using indexing
print(user_info[0]) #Khadija
print(user_info[-1]) #True

#Modifying Lists:

user_info[3] = False
print(user_info)

#List Slicing:
print(user_info[0:3])


#methods in lists:

#append() - Add an element to the end of the list.

days = ["Mon", "Tue", "Wed", "Thu", ]

days.append("Fri") # Adds a single element 'Fri' to the end
print(days)

#extend() - Add multiple element to the end of the list

days.extend(["Sat", "Sun"]) # Adds multiple elements 'Sat' and 'Sun' to the end
print(days)

# remove() - The remove() method in Python removes the first occurrence of a specified element from a list

integ_nums = [1, 2, 3, 4, 5, 2]

integ_nums.remove(2) # Removes the first occurrence of 2 from the list
print(integ_nums)

# pop() - The pop() method removes the item at the specified index from a list and If no index is provided, it removes and returns the last item in the list.

charc = ["a", "b", "c", "d", "e", "f"]

charc.pop(2) # Removes the third element 'c' from the list
print(charc)

charc.pop() # Removes the last element 'f' from the list
print(charc)

# sorting in list :
# 1. Default Sorting (Ascending Order)

numbers = [5, 3, 8, 2, 1, 6, 7, 4]

numbers.sort() # sorts the list in ascending order
print(numbers) 

# 2. Descending Sorting
numbers.sort(reverse=True)

print(numbers)

#3. Sorting by String Length (key=len)

fav_foods = ["Biryani", "fries", "maggie", "shashlak", ]

fav_foods.sort(key=len)

print(fav_foods)

# 4. Sorting by Last Character (key=lambda word: word[-1])

fav_foods.sort(key=lambda word: word[-1])
print(fav_foods)

#5. Reverse Sorting
nums = [2, 3, 5, 8, 7, 10, 12]
nums.reverse()

print(nums)



# 2 - Tuples (included methods)
# A tuple is an ordered, immutable (unchangeable) sequence of elements. Tuples are useful for fixed data collections


#Tuple
user_info2:tuple = ("Ayesha", 18, 5.1, True)

# Accessing elements in a tuple:
print(user_info[2]) #5.1

# Tuple slicing

print(user_info2[0:2]) # ('Ayesha', 18)

# Tuple length
print("Length of user_info2:", len(user_info2))

# Concatenation of tuples

user_info3 = user_info2 + ("Female",)
print(user_info3)


# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2]) # (3, 4)

# Unpacking tuples

descNum = ( 3, 2, 1)

a, b, c = descNum

print(a, b, c) # 3 2 1

# Using tuples as keys in dictionaries (because they are immutable)

# my_dict = {descNum: "this is a tuple key1",user_info: "this is a user info1",
# user_info2: "this is a user info2"}
# print("Dictionary with tuple keys:", my_dict)


# 3 - Dictionary (included methods)

# A dictionary is a collection of key-value pairs.

# Dictionary
fav_country: list =["Saudi Arabia", "South Korea", "Dubai", "Pakistan"]

myinfo :dict = {
    "name": "Khadija",
    "age": 20,
    "gender": "Female",
    "fav_country": fav_country
}

print(myinfo)


# Accessing dictionary values'

print(myinfo["name"]) # Khadija
print(myinfo["fav_country"]) # ['Saudi Arabia', 'South Korea', 'Dubai', 'Pakistan']


# Modifying dictionary values

myinfo["age"] = 19
print(myinfo)

# Adding a new key-value pair

myinfo["city"] = "karachi"
print(myinfo)

# Removing a key-value pair
del myinfo["city"]

print(myinfo)




# Dictionary methods

#keys()	Returns a list of all keys in the dictionary.	

print(myinfo.keys()) # dict_keys(['name', 'age', 'gender', 'fav_country'])

#values()	Returns a list of all values in the dictionary.	

print(myinfo.values()) # dict_values(['Khadija', 19, 'Female', ['Saudi Arabia', 'South Korea', 'Dubai', 'Pakistan']])

#items()	Returns a list of key-value pairs as tuples.

print(myinfo.items()) # dict_items([('name', 'Khadija'), ('age', 19), ('gender', 'Female'), ('fav_country', ['Saudi Arabia', 'South Korea', 'Dubai', 'Pakistan'])])


#update()	Adds or updates multiple key-value pairs from another dictionary

other_info = {"occupation": "Frontend Developer", "education": "Bachelor of Computer Science"}

myinfo.update(other_info)

print(myinfo)


#clear()	Removes all items from the dictionary.

myinfo.clear()

print(myinfo) # {}


#Iterating Over a Dictionary
product: dict = {
   "name": "Samsung",
   "model": "s4Ultra",
   "price": 50000,
   "quantity": 1,
}

for key in product:
    print(key)

for key, value in product.items():
    print(key," : ", value)







