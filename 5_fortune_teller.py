import random
##random_number = random.random()
##print(round(random_number * 100, 2))

## Take-Home 2
## Use lists and random generation to make a fortune teller application.
## Bonus: make it only semi-random, where a user has to input their zodiac sign/some other information, which controls which fortunes they can receive.


## Define variables

#You will make your millions via
millions = ["marrying a wealthy old person in ill health", "founding a tech startup", "winning the lottery", "pulling off a fine art con", "writing a best-selling memoir"]
random_millions = random.choice(millions)

#You will meet your soulmate when you are
soul_age = random.randint(1,100)

#For powerful healing, put this crystal on your altar
crystal = ["amethyst", "rose quartz", "citrine", "obsidian", "hematite"]
random_crystal = random.choice(crystal)

#This month, pay extra attention to
attention = ["the weather", "your family relationships", "eating enough protein", "eating enough healthy fats", "your shoulders", "your hips", "your feet", "how your phone makes you feel", "your mother", "the moon", "your best friend's goals and desires", "your life's purpose"]
random_attention = random.choice(attention)

#Next time it rains, be sure to
next_rain = ["have a good ugly cry", "dance naked", "eat two oranges", "take a mud bath", "trim your toenails", "call your mother"]
random_next_rain = random.choice(next_rain)

#For optimal health, drink this every day
drink_this = ["magnesium calm", "lemon water", "cucumber juice", "bone broth", "unicorn blood", "tecate", "mezcal", "psilocybin tea", "green tea", "dr pepper", "nectar from the jacaranda tree"]
random_drink_this = random.choice(drink_this)

#Your lucky number is
lucky_number = random.randint(1,30)

## Start the magic!
print("Welcome to Natasha's Den of Totally True Fortune. Are you ready to see your future? \n")

# Useless info to make them feel like something is happening
user_name = input("What is your name? ")
birth_date = input("What is your sign? ")

print("\n~*~*~ What a beautiful life you will lead,", user_name + "! ~*~*~ \n\nYou will make your millions by " + random_millions +
".\nYou will meet your soulmate when you are", soul_age,
".\nFor powerful healing, put " + random_crystal +
" on your altar. \nThis month, pay extra attention to " + random_attention +
".\nNext time it rains, be sure to " + random_next_rain +
". \nFor optimal health, drink " + random_drink_this +
" every day. \nYour lucky number is", lucky_number, ".")
    
