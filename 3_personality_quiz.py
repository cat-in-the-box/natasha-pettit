#QuizName
print("Which style of yoga is right for you, you precious flower? \n")

#questions!
while True:
    question_1 = input("1. How do you feel about acquaintances touching you?: \n \t a) bring it on; I prefer deep-tissue friendships! \n \t b) that could be okay, I guess, in particular circumstances \n \t c) oh god, no, get away from me! \n Type 'a,' 'b,' or 'c': ")
    if question_1.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_2 = input("\n 2. Sweating feels: \n \t a) no time to think about sweating! Too much fun to be had! \n \t b) ew, gross \n \t c) SO GOOD OH GOD IT MAKES ME FEEL ALIVE \n Type 'a,' 'b,' or 'c': ")
    if question_2.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break
    
while True:
    question_3 = input("\n 3. How do you feel about authority? \n \t a) EAT THE RICH \n \t b) I choose my gurus with great care \n \t c) hey, you look like you know stuff - just tell me what to do \n Type 'a,' 'b,' or 'c': ")
    if question_3.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_4 = input("\n 4. Time for handstands! \n \t a) SWEEET but first look at my one-arm balance on my friend's leg! \n \t b) hmm -- maybe tomorrow; my body is telling me to slow down in this moment \n \t c) sounds hard -- I will attempt this thing until I perish. \n Type 'a,' 'b,' or 'c': ")
    if question_4.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_5 = input("\n 5. My perfect Saturday involves: \n \t a) playing with 35 of my closest friends in a park in the sun \n \t b) a warm blanket, a long book, and quiet music playing from at least one room away \n \t c) 6am 10k, 9am meet 2 friends at the climbing crag, 7pm swim a mile in open water, 10pm sauna and cocktails \n Type 'a,' 'b,' or 'c': ")
    if question_5.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break
    
while True:
    question_6 = input("\n 6. My drug of choice is: \n \t a) MDMA \n \t b) weed \n \t c) runner's high \n Type 'a,' 'b,' or 'c': ")
    if question_6.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_7 = input("\n 7. How do you learn best? \n \t a) extremely careful scaffolding (watching an example, then trying on my own in small parts until I can do it)  \n \t b) ugh don't make me learn things \n \t c) in a room full of lean mean people who already know how to do it -- I thrive on peer pressure! \n Type 'a,' 'b,' or 'c': ")
    if question_7.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_8 = input("\n 8. My favorite snack is: \n \t a) pistachios, kale chips, and rainbow carrots in daylight; nachos after dark \n \t b) that thing my mom used to make for me when I was sick as a kid \n \t c) bone broth and gritty superfood smoothies \n Type 'a,' 'b,' or 'c': ")
    if question_8.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_9 = input("\n 9. How do you push through when things are hard? \n \t a) with the support of my wonderful community \n \t b) I don't feel the need to push through -- if it's meant to be, it will be easeful \n \t c) I AM A ROBOT WHO FEELS NO PAIN -- I just do it, you limp linguini of a human \n Type 'a,' 'b,' or 'c': ")
    if question_9.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break

while True:
    question_10 = input("\n 10. How much do you like to pay for a 1 hour class? \n \t a) maybe instead of 'paying' for a 'class,' we can just 'jam' instead and then we don't have to deal with any capitalist bullshit or help our teachers make enough to survive! \n \t b) I'd rather work out a trade -- I can provide bodywork or feather earrings or sound healing! \n \t c) exactly $20, with 5% increases each year \n Type 'a,' 'b,' or 'c': ")
    if question_10.lower() not in ('a', 'b', 'c'):
        print("\n ~*~*~ TRY AGAIN! Please type 'a', 'b', or 'c' ~*~*~")
    else:
        break


category_1 = 0
category_2 = 0
category_3 = 0

#question 1 
if question_1 == "a":
    category_1 = category_1 + 1
    
elif question_1 == "b":
    category_2 = category_2 + 1
    
elif question_1 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 2
if question_2 == "a":
    category_1 = category_1 + 1
    
elif question_2 == "b":
    category_2 = category_2 + 1
    
elif question_2 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 3
if question_3 == "a":
    category_1 = category_1 + 1
    
elif question_3 == "b":
    category_2 = category_2 + 1
    
elif question_3 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 4
if question_4 == "a":
    category_1 = category_1 + 1
    
elif question_4 == "b":
    category_2 = category_2 + 1
    
elif question_4 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 5
if question_5 == "a":
    category_1 = category_1 + 1
    
elif question_5 == "b":
    category_2 = category_2 + 1
    
elif question_5 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 6
if question_6 == "a":
    category_1 = category_1 + 1
    
elif question_6 == "b":
    category_2 = category_2 + 1
    
elif question_6 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 7
if question_7 == "a":
    category_1 = category_1 + 1
    
elif question_7 == "b":
    category_2 = category_2 + 1
    
elif question_7 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
        

#question 8
if question_8 == "a":
    category_1 = category_1 + 1
    
elif question_8 == "b":
    category_2 = category_2 + 1
    
elif question_8 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 9
if question_9 == "a":
    category_1 = category_1 + 1
    
elif question_9 == "b":
    category_2 = category_2 + 1
    
elif question_9 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#question 10
if question_10 == "a":
    category_1 = category_1 + 1
    
elif question_10 == "b":
    category_2 = category_2 + 1
    
elif question_10 == "c":
    category_3 = category_3 + 1
    
else:
    print("Please type a, b, or c")
    

#calculations
cat_1_percent = (category_1 / 8)*100
cat_2_percent = (category_2 / 8)*100
cat_3_percent = (category_3 / 8)*100

#category descriptions
cat_1_description = "AcroYoga! You're a creative free spirit who wants nothing more than to lounge about in a pile of your best friends' bodies, making up new ways to balance on each other. Fly high, my little songbird! Try not to get an STD!"
cat_2_description = "Yin yoga! You long for those quiet, deep, inching-deeper stretches that require absolutely zero active effort. Working out is for the unenlightened, yall. Stretching gets the lymphatic system moving too, so go ahead and just lie there for a while and call it exercise."
cat_3_description = "Hot yoga! Which is actually called Bikram -- get it right or you're in BIG TROUBLE. Important things to note: leave your creativity and problem-solving at the door. This is a practice for those who want to follow a precise recipe for success. NO THINKING ALLOWED! But yes, you will have sick abs, you'll sweat out all your toxins, and you'll be promoted to demi-god."


#answers
if category_1 > category_2 and category_1 > category_3:
    print("\n ~*~*~ RESULTS ~*~*~ \n Congratulations! You are perfect for", cat_1_description, "You are", cat_1_percent, "% AcroYoga,", cat_2_percent, "% Yin yoga, and", cat_3_percent, "% Hot yoga.")

elif category_2 > category_3 and category_2 > category_1:
    print("\n ~*~*~ RESULTS ~*~*~ \n Congratulations! You are perfect for", cat_2_description, "You are", cat_2_percent, "% Yin yoga,", cat_1_percent, "% AcroYoga, and", cat_3_percent, "% Hot yoga.")

elif category_3 > category_2 and category_3 > category_1:
    print("\n ~*~*~ RESULTS ~*~*~ \n Congratulations! You are perfect for", cat_3_description, "You are", cat_3_percent, "% Hot yoga,", cat_2_percent, "% Yin yoga, and", cat_1_percent, "% AcroYoga.")
    
else:
    print("\n ~*~*~ RESULTS ~*~*~ \n: Congratulations! Wow, you're difficult to define! You are", cat_1_percent, "% AcroYoga,", cat_2_percent, "% Yin yoga, and", cat_3_percent, "% Hot yoga. Which of these describes you best? \n", cat_1_description, "\n", cat_2_description, "\n", cat_3_description)


