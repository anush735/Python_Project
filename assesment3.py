import random
# random_string function to display random response 
def random_string():  
    ran_Answers = ['Hmmm', 'Oh', 'Yes', 'May be', 'Haha', 'I see', 'Tell me more']     # list of random answers
    ran_Response = random.choice(ran_Answers)                                          # choices random answer from the list
    print(ran_Response)                                                                # displays random value from the list

# operator function to display random operator name from the list
def operator():
    # list of random operator name 
    oprt_Name = ["Jhon", "Jane", "Rose", "George"]
    print(f"My name is {random.choice(oprt_Name)} and it will be my pleasure to help you.")

# Message shown to user 
print("\nWelcome to Pop Chat")
print("One of our operators will be pleased to help you today.\n")

# conditions to validate email
inp_Email = input("Please enter your Poppleton email address: ")   
j = 0
if len(inp_Email) >= 12:                    # checks whether length if given email is greater than and equal to 12 or not
    if inp_Email[0].isalpha():              # checks whether the first value in given email is alphabet or not
        if "@pop.ac.uk" in inp_Email:       # checks whether @pop.ac.uk is in given email or not
            if ("@" in inp_Email) and (inp_Email.count("@") == 1) and (inp_Email[-10] == "@"):       #checks count and position of @ in given email
                for i in inp_Email:         # checks if given email has space or not
                    if i == " ":
                        j = 1
                if j == 1:
                    print("Invalid Email! Try Again")
                else:
                    # using string methods to give required output
                    username = inp_Email.split("@")[0]
                    print(f"Hi, {username.capitalize()}! Thank you, and Welcome to PopChat!")
                    
                    # operator function called
                    operator()                           

                    # random 10% network error
                    value = random.randint(1,100)         # sets random value from 1 to 100
                    if value in range(1, 11):             # gives error if value is in the range of 1 to 11  
                        print("*** Network Error ***")
                        print(f"\nThanks, {username.capitalize()}, for using PopChat. See you again soon!")
                    else:
                        # input for chat system
                        user_Input = str()     # global variable 
                        while(("exit" not in user_Input) and ("bye" not in user_Input)):    # while loop to loop global variable
                            user_Input = input("---> ").lower()

                            # check if given input has mentioned string or not
                            if "library" in user_Input:
                                print("The library is closed today.")
                            elif "wifi" in user_Input:
                                print("WiFi is excellent across the campus")
                            elif "deadline" in user_Input:
                                print("Your deadline has been extended by two working days.")
                            elif "exams" and "exam" in user_Input:
                                print("Exams are coming!!")
                            elif "lab" in user_Input:
                                print("Labs are open till 5pm")
                            elif "where" in user_Input:
                                print("Sorry I am not sure about that")
                            elif ("exit" not in user_Input) and ("bye" not in user_Input):
                                random_string()       # random_string function called
                            else:
                                print(f"\nThanks, {username.capitalize()}, for using PopChat. See you again soon!")
            else:
                print("Invalid Email! Try Again")
        else:
            print("Invalid Email! Try Again")
    else:
        print("Invalid Email! Try Again")
else:
    print("Invalid Email! Try Again")


