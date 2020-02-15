##
#
#

families = ["1. Aist", "2. Bellamy", "3. Pettit", "4. Wood"]
balances = [0,0,0,0]

# Gets index of families, asks user which family they choose (prompts come from other functions -- either choose you or choose other fam)
def get_family(choices,prompt):
    print("\nFamilies: \n")
    for choice in choices:
        print(choice)
    which_fam = int(input(prompt))
    return which_fam

# Displays the hour balance for the single family they choose
def display_personal_balance(choices,hours):
    personal_fam = get_family(families,"\tWhich family are you? Type 1, 2, 3, or 4. ")
    if personal_fam == 1:
        print("\nYour balance is: \n","\t", families[0], ":", balances[0], "hours")
    elif personal_fam == 2:
        print("\nYour balance is: \n","\t", families[1], ":", balances[1], "hours")
    elif personal_fam == 3:
        print("\nYour balance is: \n","\t", families[2], ":", balances[2], "hours")
    elif personal_fam == 4:
        print("\nYour balance is: \n","\t", families[3], ":", balances[3], "hours")
    else:
        print(personal_fam, "Something went wrong!")

# Displays the hour balance for the every family, in text and in a bar chart
def display_group_balance(choices,hours):
    print("\nThe group balances are:\n",families[0], ":", balances[0], "hours\n", families[1], ":", balances[1], "hours\n", families[2], ":", balances[2], "hours\n", families[3], ":", balances[3], "hours")
    #import numpy as np
    #import matplotlib.pyplot as plt
    #y_pos = np.arange(len(bars))
    ## Create bars
    #plt.bar(y_pos, balances)
    ## Create names on the x-axis
    #plt.xticks(y_pos, families)
    ## Show graphic
    #plt.show()


# Asks whether the user wants to see everyone’s balance or just their own and calls the appropriate function
def display_balance(choices,hours):
    balance_choice = int(input("Would you like to see just your balance, or the whole group's balances? \nPlease type 1 for you, and 2 for the whole group: "))
    if balance_choice == 1:
        display_personal_balance(families,balances)
    elif balance_choice == 2:
        display_group_balance(families,balances)
    else:
        print("Whoops! That didn't work.")
        

#asks the user which function they would like to run (or quit) and then calls itself to run again.
def user_loop(choices,hours):
    action = int(input("\nWhat would you like to do?\n" +
                       "\t1. Check balances\n" +
                       "\t2. Record childcare hours\n" +
                       "\t3. Save and quit\n\t"))
    if action == 1:
        display_balance(families,balances)
    elif action == 2:
        #families =
        record_hours(families,balances)
        record_their_hours(families,balances)
    elif action == 3:
        exit()
        
    user_loop(choices,hours) #run this method again!


#updated balances - asks which family is receiving the hours and updates that family’s balance
def record_hours(choices,hours):
    #asks which family gave the hours
    personal_fam = get_family(families,"\tWhich family are you? Type 1, 2, 3, or 4. ")
    if personal_fam == 1:
        balances[0] += total_hours(families,balances)
    elif personal_fam == 2:
        balances[1] += total_hours(families,balances)
    elif personal_fam == 3:
        balances[2] += total_hours(families,balances)
    elif personal_fam == 4:
        balances[3] += total_hours(families,balances)
    else:
        print(personal_fam, "Something went wrong!")
    

def total_hours(choices,hours):
    babysitting_hours = float(input("\tHow many hours did you watch the kids? If you watched more than one family's kids, multiply these hours by 1.5: "))
    return babysitting_hours


# Asks which families you provided care for, and calculates their new balances
def record_their_hours(choices,hours):
    receiving_fam = get_family(families,"\tWhich family's kids did you watch? Type 1, 2, 3, or 4. If more than one family, enter one of them now. ")
    give_hours = float(input("How many hours did you watch the kids? "))
    if receiving_fam == 1:
        balances[0] -= give_hours
        multiple_fams = int(input("Did you watch another's family's kids during this same time? Please type 1 for yes and 2 for no. "))
        if multiple_fams == 1:
            record_their_hours(choices,hours)
    elif receiving_fam == 2:
        balances[1] -= give_hours
        multiple_fams = int(input("Did you watch another's family's kids during this same time? Please type 1 for yes and 2 for no. "))
        if multiple_fams == 1:
            record_their_hours(choices,hours)
    elif receiving_fam == 3:
        balances[2] -= give_hours
        multiple_fams = int(input("Did you watch another's family's kids during this same time? Please type 1 for yes and 2 for no. "))
        if multiple_fams == 1:
            record_their_hours(choices,hours)
    elif receiving_fam == 4:
        balances[3] -= give_hours
        multiple_fams = int(input("Did you watch another's family's kids during this same time? Please type 1 for yes and 2 for no. "))
        if multiple_fams == 1:
            record_their_hours(choices,hours)
    else:
        record_their_hours(choices,hours)
    
    
if __name__ == "__main__":
    #display_personal_balance(families,balances)
    #get_family(families, "Which family are you? Type 1, 2, 3, or 4. ")
    #display_group_balance(families,balances)
    #display_balance(families,balances)
    user_loop(families,balances)