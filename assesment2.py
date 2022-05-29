# message shown to user
print("\nSwallow Speed Analysis: Version 1.0\n")

# declaring variables 
list_Reading = []                                                # list type variable
input_Reading = input("Enter the Next Reading: ").lower()    # variable to take input from the user

# condition to check if input is given or not
if input_Reading == "":
    print("No readings entered. Nothing to do.")
else:
    # while loop to ask input from user
    while input_Reading != "":
        # condition to take right input from user
        if (input_Reading[0] == "u") and (input_Reading[1:].replace('.', '', 1).isdigit()):    # check if 0 index value is u and other are digits or not
            print("Reading saved")
            list_Reading.append(float(input_Reading[1:])*1.61)             # appends given value as float type ignoring 0 index value to the list and converts MPH to KPH 
            input_Reading = input("Enter the Next Reading: ").lower()
        elif (input_Reading[0] == "e") and (input_Reading[1:].replace('.', '', 1).isdigit()):  # check if 0 index value is e and other are digits or not
            print("Reading saved")
            list_Reading.append(float(input_Reading[1:]))                  # appends given value as float type ignoring 0 index value to the list
            input_Reading = input("Enter the Next Reading: ").lower()
        else:
            break  # stop loop

    # condition to check if list is appended or not
    if (len(list_Reading)!= 0):           
        print("\nReading summary\n")
        print(len(list_Reading), "Reading Analysed\n")     # prints number of input taken
        print(f"Max Speed: {max(list_Reading)/1.61:.1f} MPH,  {max(list_Reading):.1f} KPH")     # prints maximum MPH and KPH readings 
        print(f"Min Speed: {min(list_Reading)/1.61:.1f} MPH,  {min(list_Reading):.1f} KPH")     # prints minimum MPH and KPH readings
        
        # calculates average
        total_Reading = 0 
        for i in range(0,len(list_Reading)):
            total_Reading = total_Reading + list_Reading[i]
        average_Reading = total_Reading/len(list_Reading)
        print (f"Avg Speed: {average_Reading/1.61:.1f} MPH, {average_Reading:.1f} KPH.")        # prints average MPH and KHP readings
    else:
        print("Invalid Input! Try Again")
