'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
def sleep_in(weekday, vacation):
    if weekday == False:
        sleep_q = True
    elif vacation == True:
        sleep_q = True
    else:
        sleep_q = False
    return sleep_q

if __name__ == "__main__":
    print(sleep_in(False, True))


'''
Given three ints, a b c, return True if b is greater than a, and c is greater than b.
However, with the exception that if "bOk" is True, b does not need to be greater than a.


in_order(1, 2, 4, False) → True
in_order(1, 2, 1, False) → False
in_order(1, 1, 2, True) → True
'''
def in_order(a, b, c, b0k):
    if b > a:
        if c > b:
            is_it = True
        else:
            is_it = False
    elif b0k == True:
        if c > b:
            is_it = True
        else:
            is_it = False
    else:
        is_it = False
    return is_it
        
if __name__ == "__main__":
    print(in_order(1, 1, 2, True))


'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
'''
def extra_end(str):
    return str[-2:] + str[-2:] + str[-2:]

if __name__ == "__main__":
    print(extra_end("Hi"))




'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''
def make_chocolate(small, big, goal):
    big_kilos = int(big)*5
    if int(goal) - big_kilos <= small:
        return int(goal) - big_kilos
    else:
        return -1
    
if __name__ == "__main__":
    print(make_chocolate(4, 1, 7))


'''
HINT FOR LIST PROBLEMS: Use a[0], a[1], ... to access elements in a list, len(a) is the length.

Given a list of ints, return True if 6 appears as either the first or last element in the list.
The list will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''
def first_last6(nums):
    full_list = a[0], a[1],


'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''
def rotate_left3(nums):
    pass


'''
Return the number of even ints in the given list.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''
def count_evens(nums):
    pass


'''
Given a list length 1 or more of ints, return the difference between the largest and smallest values in the list.
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
'''
def big_diff(nums):
    pass


# Call functions here
sleep_in(False, False)