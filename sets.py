import gc
# Assignment No 03

# Part 3: Sets and Frozen Sets.

# other parts included in lists_dict_tuples.py and controlflow.py

# topic included in part 3:

    # 1. Sets (included methods)
    # 2. Frozenset (included methods)
    # 3. GC: Garbage Collection

# 1 - Sets (included methods):


# sets in python:

#A set in Python is an unordered collection of unique elements. It is enclosed in curly brackets { } and automatically removes duplicate values.

# A set is :
#- unordered
#- unchangeable
#- unindexed
#- mutable
 

# two way write sets
num_sets: set = {45, 19, 11, 11, 13,}
num_sets2: set = set([45, 19, 11, 11, 13,])
print("type(num_sets)   = ", type(num_sets))
print("type(num_sets2)  = ", type(num_sets2))
print("num_sets == my_set2 = ", num_sets == num_sets2)


my_set = {"hello", 20, 25, "world"}
print(my_set)
# 1 -remove an item
my_set.remove("hello")
print(my_set)

#2-  add an item
my_set.add(45)
print(my_set)


# 3- discard()
# discard() only removes a single element.
my_set2: set = {1,2,3,4,5,6,7,8,9}

my_set2.discard(5)
print(my_set2.discard({1,2,3})) # discard doesn't find it because {1,2,3} is also a set and its just change  noting  return None.
print(my_set2)

# 4- Use difference_update() method to remove multiple element at once.
my_set2.difference_update({1,2,3}) # remove {1, 2,3} from my_set2
print(my_set2) 

# 5- use update() method to add multiple elements at once
my_set2.update({11,12,13}) # add {11, 12, 13} to my_set2
print(my_set2)

# 6- Union of two sets using union()
fruits1 = {"mango", "strawberry", "orange"}
fruits2 = {"apple", "banana", "mango"}

union_fruits = fruits1.union(fruits2)

print(union_fruits)

# using | operator instead of union more readable and concise

or_fruits = fruits1 | fruits2
print(or_fruits)

#  discard() and remove() and pop() methods:

#difference:

# -7 remove() → Removes a Specific Element, Raises an Error if Not Found

#union_fruits.remove("peach") # error


# -8  discard() → Removes a Specific Element, No Error if Not Found
union_fruits.discard("banana") 

print(union_fruits)



# -9  pop() → Removes and Returns a Random Element
union_fruits.pop()

print(union_fruits)

# -10 clear() → Removes all elements from the set
copy_or_fruits =   or_fruits.copy()

copy_or_fruits.clear()

print(copy_or_fruits) # output set()


# -11 copy(): Returns a copy of the set.

copy_fruits1 = fruits1.copy()

print(copy_fruits1) # output {'mango', 'strawberry', 'orange'}

# -12 difference(): method returns a new set containing only the elements that are in the first set but NOT in the second set(s).

diff_fruits = fruits1.difference(fruits2)

print(diff_fruits)



# -13  intersection(): method returns a new set containing only the same elements in two different sets

intersection_fruits = fruits1.intersection(fruits2)

print(intersection_fruits)


# -14  symmetric_difference(): method returns a new set containing all elements that are in either the first set or the second set but not in both.

sym_diff_fruits = fruits1.symmetric_difference(fruits2)
# like we have a "mango" in both so except "mango" it will return all 

print(sym_diff_fruits) #output {'apple', 'orange', 'banana', 'strawberry'}


# -15 symmetric_difference_update() method modifies the original set by keeping only the elements that are unique in both sets (removing common elements).
 
fruits1.symmetric_difference_update(fruits2)

print(fruits1) # output {'orange', 'banana', 'apple', 'strawberry'}

# -16 issubset() method checks whether one set is completely contained within another set. It returns:

# like fruit1 inside fruit2
print(fruits1.issubset(fruits2)) # output False if one missing it will be false

# -17 issuperset() method checks whether one set contains all elements of another set. It returns:
# like fruit2 inside fruit1
print(fruits1.issuperset(fruits2)) 











# The Inner Working of SET (Advance Topic)

# In Python, sets are implemented as hash tables with unique keys. When we add an element to a set, Python automatically checks if the element is already present in the set. If it is, Python does not add it again. This makes sets very efficient for checking membership.


# i also learn about the difference between id and has 

# id() → :

#Purpose   |  Memory address of an object.
#Changes?  |  Stays the same while object exists.
#Works for |  All objects.
#Used in   |  Object identity checks.

# hash() → :

#Purpose   |  Hash value based on content.
#Changes?  |  Stays the same for immutable objects.
#Works for |  	Only immutable (hashable) objects.
#Used in   |  frozenset, dictionaries (for fast lookups(Checking if an item exists is much faster.)).

# Frozenset (included methods) :

# A frozenset is an immutable version of a set. It is a built-in Python class. Unlike sets, frozensets are hashable and cannot be changed. frozensets are useful when you need to create a set with unchangeable elements.

# A frozenset is :
# Immutable
# unordered
# hashable
#Unique elements
 
random_set :frozenset = frozenset(["blue", "green", 4,5,6])

#  all frozenset methods almost same as sets methods so i already add sets methods details and use case.


# GC: Garbage Collection:

gc.collect()
print(gc.get_count())










