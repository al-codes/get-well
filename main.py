
import suggestions

summarylist = []


# Initial greeting - START
print("Welcome to Get Well, your guide to easy, natural home remedies. What issue are you dealing with today?\n")


# Asks user if they would like to view more issues and provides exit out of program
def select_again():

    another_selection = input("Do you have any additional issues?\n> ")
    another_selection = another_selection.lower()

    if another_selection.startswith("y"):
        return greeting()

    # Asks user if they want a summary upon exit
    if another_selection.startswith("n"):
        wantsummary = input("\nLooks like we're all done here! Before exiting, would you like to see a summary of the suggestions provided to you during this session?\n> ")
        print("\n")
        wantsummary = wantsummary.lower()
        if wantsummary.startswith("y"):
            return suggestion_summary()
        
        else:
            print("Take care and we hope you get well soon! If your problem persists for more than 24 hours, please contact your primary physician. Bye!")

    elif another_selection != another_selection.startswith("y") or another_selection.startswith("n"):
        print("I did not understand that. Please type yes or no.\n")
        return select_again()

# User selects nausea
def nausea_selection():
    print("\nI'm sorry to hear you're experiencing nausea.")

    food_intake = input("\nHave you eaten anything today?\n> ")
    food_intake = food_intake.lower()

    if food_intake.startswith("y"):
        print("\n")
        print(suggestions.nausea_foody)
        summarylist.append(suggestions.nausea_foody)
        print("\n")
        return select_again()

    if food_intake.startswith("n"):
        print("\n")
        print(suggestions.nausea_foodn)
        summarylist.append(suggestions.nausea_foodn)
        print("\n")
        return select_again()
    
    elif food_intake != food_intake.startswith("y") or food_intake.startswith("n"):
        print("Please type yes or no.")
        return nausea_selection()

# User selects gas/bloating
def gasbl_selection():
        print("\n")
        print("I'm sorry to hear you are experiencing gas/bloating.\n")
        print(suggestions.gasbloat)
        summarylist.append(suggestions.gasbloat)
        print("\n")
        return select_again()

# User selects bowel issues
def bowel_selection():
        print("\nI'm sorry to hear you're experiencing bowel issues.")
        bowel_type = input("Are you currently experiencing diarrhea or constipation?\n> ")
        print("\n")
        bowel_type = bowel_type.lower()
        if bowel_type.startswith("d"):
            print(suggestions.diarrhea)
            summarylist.append(suggestions.diarrhea)
            print("\n")
            return select_again()

        if bowel_type.startswith("c"):
            print(suggestions.constipation)
            summarylist.append(suggestions.constipation)
            print("\n")
            return select_again() 

        elif bowel_type != bowel_type.startswith("d") or bowel_type.startswith("c"):
            print("Please type your issue. (diarrhea or constipation)")
            return bowel_selection()

# Shows user summary of issues
def suggestion_summary():
    for summary in enumerate(summarylist, 1):
        print(summary)
        print("\n")

    save_file = input("Would you to save this to a file?\n> ")

    if save_file.startswith("y"):
        with open("myhealth.txt", 'w') as output:
            output.write(str(summarylist))
            
            print("\nYour file has been saved. Take care and we hope you get well soon. If your problem persists for more than 24 hours, please contact your primary physician. Bye!")
    
    else:
        print("\nTake care and we hope you get well soon. If your problem persists for more than 24 hours, please contact your primary physician. Bye!")

# Shows user list of options 
def greeting():
    print("\nPlease type the corresponding letter to your issue:\n")
    print("A) Nausea")
    print("B) Gas/Bloating")
    print("C) Bowel Issues\n")


    while True:
        selection = input("> ")
        selection = selection.upper()

        nausea = "A"
        gas_bloating = "B"
        bowel_issues = "C"


        if selection == nausea:
            return nausea_selection()
        
        if selection == gas_bloating:
            return gasbl_selection()
        
        if selection == bowel_issues:
            return bowel_selection()

        elif selection != nausea or gas_bloating or bowel_issues:
            print("Please type A, B or C.")
            return greeting()

greeting()



