import time
# Assignment No 03

# Part 1 : ControlFlow and Decision Making in python

# other parts included in lists_dict_tuples.py and sets.py.

# topic included in part 1:

    # 1. if- elif-else statement
    # 2. for loop
    # 3. while loop
    # 4. break statement
    # 5. continue statement
    # 6. pass statement
    # 7. range function
    # 9. nested loops


# what is Control flow ?

# Control flow is the order in which statements or instructions and functions are executed. 
  
 




# 1 - if-elif-else statement:
# understand by example:

# A mood detector which will give you the amazing message based on your mood 
mood_detector =input("How are you Feeling Today 😊 ? (happy, sad, excited, tired) ")

if mood_detector == "happy":
    print("Yay! Your smile just made the world a better place! Keep shining! ✨")

elif mood_detector == "sad":
    print("Aww, sending you a virtual hug! 🤗 Remember, even rainy days bring rainbows! 🌈")

elif mood_detector == "excited":
    print("Whoa! Your energy is contagious! Go conquer the world! 🚀🔥")

elif mood_detector == "tired":
    print("Time to recharge! Grab a cozy blanket and power up like a pro! ⚡😴")

else:
    print("I don't know how you feel, but remember—you're amazing, unstoppable, and capable of incredible things! Keep going! 🌟💖")





# 2 - for loop:
#Understand by example:

# a simple dount maker with if-else , for loop and time 
# take user input yes and no
donut_maker = input("Enter donut if you like? (yes, no )")
#if user input yes the for loop start
if donut_maker == "yes":
    for i in range(3): 
        # loop through to make 3
        print("Making donut number:", i+1)
         # using time.sleep for 1 sec delay  for each step.
        time.sleep(1)
        print("✅ Fry it to golden perfection 🔥")

        time.sleep(1)
        print("✅ Glaze it with sweet icing 🍯")
       
        time.sleep(1)
        print("✅ Sprinkle it with toppings 🌈")
        
        time.sleep(1)
        print("donut is ready! Enjoy! 🎉🍩")

# if user input no the for loop not start       
else:
    print("No problem, you can make your own donuts at home! ")





# 3 - while loop:
# understand by example:

# initially cookies_jar has zero 0 cookies 
# imagine integers as cookies
cookies_jar: int = 0
# to fill cookies_jar with cookies we set while loop running until cookies_jar will be filles with 20 cookies
while cookies_jar <= 20:
    # print current number of cookies in jar
    print(f"you have {cookies_jar} 🍪 Cookies in your jar ")
    # each time loop runs and 5 cookies add in jar.
    cookies_jar += 5 
    # adding 1 second delay for each step of while loop.
    time.sleep(1)





# 4,5 - break & continue statement:
# understand by example:

#Break Example:
#break: Exits the loop immediately.
for i in range(20):
    if i == 9:
        break
    print(i)


#Continue Example:
#continue: Skips the rest of the code in the current iteration and moves to the next iteration.
for i in range(10):
    if i == 5:
        continue
    print(i)


#nested loops:
#understand by example:

# List of days in a week
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for week in range(1,5): # 4 weeks
    print(f'Days of the week {week}') # Prints the current week number

    # Loop through each day in the list
    for day in week_days:
        time.sleep(1) # delay for print each day
        print(day) # Prints each day of the week













