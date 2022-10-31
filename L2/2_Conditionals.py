
# 1. ==, <=, >=, !=,  and / or / not

# 2. truthy and falsy values

# Let's explore if, else with an example
# 3. if statement

rain_check = input('Is it raining?')

if rain_check == 'Yes':
    print("Stay at home")

# 4. else statement


rain_check = input('Is it raining?')

if rain_check == 'Yes':
    print("Stay at home and study")
else:
    print("Go out and play")

# 5. elif statement


rain_check = input('Is it raining?')
wind_check = input("Is the wind blowing?")

if rain_check == 'Yes':
    print("Stay at home and study")
elif wind_check == 'Yes':
    print("Play basketball")
else:
    print("Play badminton")


# We can illustrate with a number program -> MARKS

name = "Chris"

if name == "Mike" or "Charles" or "Boyle":
    print("True")

# we'll see a better way to do this (which actually works) when we study Lists.