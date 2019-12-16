## Ask user for 3 numbers, then see whether any two of them add up to the third.


## Tell user what's happening
print("Let's test whether any of your number choices add up to another.")

## Ask for first number
while True:
    num1 = int(input("Type a number between 1 and 10: "))
    if num1 not in (1,2,3,4,5,6,7,8,9,10):
        print("\n ~*~*~ TRY AGAIN! Please type a number between 1 and 10: ~*~*~")
    else:
        break
    

## Ask for second number
while True:
    num2 = int(input("Type another number between 1 and 10: "))
    if num2 not in (1,2,3,4,5,6,7,8,9,10):
        print("\n ~*~*~ TRY AGAIN! Please type a number between 1 and 10: ~*~*~")
    else:
        break
    
    
## Ask for third number    
while True:
    num3 = int(input("Type a third number between 1 and 10: "))
    if num3 not in (1,2,3,4,5,6,7,8,9,10):
        print("\n ~*~*~ TRY AGAIN! Please type a number between 1 and 10: ~*~*~")
    else:
        break
    
    
## Calculate and print answer    
if (num1) + num2 == num3:
    print("True! Two of these numbers add up to another.")
    
elif num2 + num3 == num1:
    print("True! Two of these numbers add up to another")
    
elif num3 + num1 == num2:
    print("True! Two of these numbers add up to another")
    
else:
    print("False! No two of these add up to the other.")