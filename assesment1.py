# Message shown to user
print("Stop! Who would cross the Bridge of Death")
print("Must answer these questions three, 'ere the other side he see.\n")

# prompts user to input name 
input_Name = input("What is your name? ")

# checks if 'Arthur' is in given input or not
if("Arthur" in input_Name or "arthur" in input_Name):
    print("My liege! You may pass!")

else:
    # prompts user to input quest if 'Arthur' is not in given input
    input_Quest = input("What is your quest? ")

    # checks if 'Grail' is in given input or not  
    if("Grail" in input_Quest or "grail" in input_Quest):

        # prompts user to input color if 'Grail' is not in given input
        input_Color = input("What is your favourite colour? ")

        # checks whether 0 index value of input_Name is equal to 0 index value of input_color
        if(input_Name.lower()[0] == input_Color.lower()[0]):
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")