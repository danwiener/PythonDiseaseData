#Henrik Wiener / 2/20/2022


# Open and read health data file one line at a time
# Columns are 
#   disease,increase,location,number,population,year

file = open("health-no-head.csv", "r")

def format_disease_data(file):
    """This function processes every line of given file to separate data including 
    states, diseases, number of occurences of those diseases, and years. It also
    prompts user for input and defines conditions which allow user to input 
    any combination of three fields of input to access desired data, which will
    be printed as formatted below. The program also lets users enter first three
    letters of any state rather than the whole state name, if they so desire.""" 

    # Define categories to print header for tables
    categories = ["State", "Disease", "Number", "Year"]
    # Initiate lists to organize and store data from each line of file
    states = []
    # List of first three characters of all states in data
    states3 = []
    diseases = []
    numbers = []
    years = []
    # Loop through lines of file
    # Append lines of file to lists above
    for aline in file:
        line = aline.split(",")
        states.append(line[2])
        # Append first three characters of each state to list states3
        states3.append(line[2][:3])
        diseases.append(line[0])
        numbers.append(int(line[3]))
        years.append(line[5].strip('\n'))
    #calculate total prior to formatting numbers with commas because python 
    #will not be able to calculate once commas are added.
    Total = sum(numbers)
    # Format Total to include print a comma in the number where necessary.
    commaTotal = "{:,}".format(Total)
    # Create a copy of list numbers which is formatted properly with commas,
    # for printing purposes.
    numbers2 = numbers[:]
    for i in range(len(numbers2)):
        numbers2[i] = "{:,}".format(numbers2[i])
    # The following block of code would print the entire data table formatted as specified,
    # however, it is extremely slow to do this because there are so many data entries. 
    # Remove triple-quotation marks to activate block of code.
    """print("All Data:")
    print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
    print()
    for i in range(len(states)-1):
        if (int(years[i]) < int(years[i+1])) or (diseases[i] < diseases[i+1]):
            print("{0:<25}{1:<15}{2:>0}{3:>15}\n".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
        else:
            print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
    print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[-1], diseases[-1], str(numbers2[-1]).rjust(10), years[-1]))
    print("{0:<25}{1:<15}{2:>0}".format("", "Total", str(commaTotal).rjust(10)))
    print()
    print()"""

    # Close file - we no longer need to read the file.
    file.close()

    # Briefly explain the program to the user with these
    # printed lines.
    print("This program provides information about diseases\n\
in the United States from years 1928 through 2011.\n\
\n\
Enter a state, disease, and/or year as prompted to view information.\n\
Press 'Enter' to continue. Type 'End' to end the program.)\n\
\n\
Diseases included in the data are:\n\
Measles, Polio, Smallpox, Pertussis, Hepatitis A, Rubella, and Mumps.")
    print()

    #define conditions for searching for specific data.
    k = 0
    # Initiate list which will be used to store numbers of occurences of diseases for any given search query.
    numbers3 = []
    while k == 0:
        # Prompt user for search inputs, end program if they type 'end'
        END = 'END'

        state = input("Enter U.S. state: ")
        if state.upper() == END:
            quit()

        disease = input("Enter disease: ")
        if disease.upper() == END:
            quit()

        year = input("Enter year: ")
        if year.upper() == END:
            quit()
        print()

        # If user enters a state, disease, AND a year
        # if state: user entered something when prompted to enter a state
        # if not state: user left state field blank in search query
        # if disease: user entered something for disease input
        # if not disease: user left disease field blank in search query
        # if year: user entered something for year input
        # if not year: user left year field blank in search query
        if state and disease and year:
            # If one of three inputs not found in the database
            # print error message and start while loop over.
            # This also accounts for/allows user to enter first three characters
            # of a state to search for a state rather than enter the whole state.
            if (state.upper() not in states and state.upper() not in states3) or disease.upper() not in diseases or year not in years:
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            else:
                # Print header
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate through each list initiated at beggining of function
                # containing states, first three characters of 
                # states, diseases, numbers, and years
                # All lists have same number of indexes so index of each list will 
                # properly line up for printing while loop is iterating
                for i in range(len(states)):
                    # If 
                    #(e.g. list of states, list of first three characters of
                    # states, list of diseases, or list of years), 
                    # print relevant list info formatted as specified
                    if (state.upper() == states[i] or state.upper() == states3[i]) and disease.upper() in diseases[i] and year in years[i]:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        # Add numbers of any returned data to list three to return Total of any given query
                        numbers3.append(int(numbers[i]))
            # Total is equal to sum of all numbers added to list numbers3. 
            # Formula for total will remain the same for 
            # all combos of user input in the following blocks of code.
            Total = sum(numbers3)
            # Format total to include a comma if necessary for proper number formatting.
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            # Clear list numbers3 out once printed, so it can be resused to calculate Total for other input combinations
            numbers3.clear()

        # If user enters a state OR first three letters of a state, and a year, but NOT a disease
        if state and not disease and year:
            # If one of two inputs not in database, print error
            # This also accounts for user input of just first three characters of a state
            if (state.upper() not in states and state.upper() not in states3) or year not in years:
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            else:
                # Print header
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate through lists
                for i in range(len(states)):
                    # If both user inputs in database, print data linked to inputs,
                    # formatted as specified
                    # Accounts for user entering just first three characters of a state
                    if (state.upper() == states[i] or state.upper() == states3[i]) and year in years[i]:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        numbers3.append(int(numbers[i]))
            # Same formula/method for (printing) total as used above
            Total = sum(numbers3)
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            numbers3.clear()


        # If user enters a state OR first three letters of a state, and disease, but NOT a year
        if state and disease and not year:
            # If one of two inputs not in database, print error
            # This also accounts for user input of just first three characters of a state
            if (state.upper() not in states and state.upper() not in states3) or disease.upper() not in diseases:
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            else:
                # Print header
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate through lists
                for i in range(len(states)):
                    # If both user inputs in database, print data linked inputs,
                    # formatted as specified
                    # Accounts for user entering just first three characters of a state
                    if (state.upper() == states[i] or state.upper() == states3[i]) and disease.upper() in diseases[i]:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        numbers3.append(int(numbers[i]))
            # Same formula/method for (printing) total as used above
            Total = sum(numbers3)
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            numbers3.clear()

        # If user enters a state OR first three letters of a state, but NOT a disease and NOT a year
        if state and not disease and not year:
            # If state input not in database, print error
            # Accounts for user input of just first three characters of a state
            if (state.upper() not in states and state.upper() not in states3):
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields\n\
does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            # Print header
            else:
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate throgh lists
                for i in range(len(states)):
                    #If user input for state is in database, print data linked to that state,
                    # Formatted as specified
                    # Accounts for user entering just first three characters of a state
                    if (state.upper() == states[i] or state.upper() == states3[i]):
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        numbers3.append(int(numbers[i]))
            # Same formula/method for (printing) total as used above
            Total = sum(numbers3)
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            numbers3.clear()

        # If user does NOT enter a state, but enters a disease and a year
        if not state and disease and year:
            # If neither of two inputs in database, print error
            if disease.upper() not in diseases or year not in years:
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            else:
                # Print header
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate through lists
                for i in range(len(states)):
                    # If both user inputs exist in database, print data linked to those inputs,
                    # formatted as specified
                    # Accounts for user entering just first three characters of a state
                    if disease.upper() in diseases[i] and year in years[i]:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        numbers3.append(int(numbers[i]))
            # Same formula/method for (printing) total as used above
            Total = sum(numbers3)
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            numbers3.clear()

        # If user does NOT enter a state, but does enter a disease, and NOT a year
        if not state and disease and not year:
            # If input for disease field not in database, print error
            if disease.upper() not in diseases:
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            else:
                # Print header
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate through lists
                for i in range(len(states)):
                    # If input for disease in database, print data linked to input,
                    # formatted as specified
                    # Accounts for user entering just first three characters of a state
                    if disease.upper() in diseases[i]:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        numbers3.append(int(numbers[i]))
            # Same formula/method for (printing) total as used above
            Total = sum(numbers3)
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            numbers3.clear()

        # If user does NOT enter a state or a disease, but enters a year
        if not state and not disease and year:
            # If input for year field not in database, print error
            if year not in years:
                print("Error: Please input valid information.\n\
The information you have requested in one or more fields does not exist in the data.")
                print()
                #start back at beginning of loop to prompt user for new input
                continue
            else:
                # Print header
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                # Iterate through lists
                for i in range(len(states)):
                    # If input for year in database, print data linked to input,
                    # formatted as specified
                    # Accounts for user entering just first three characters of a state
                    if year in years[i]:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                        numbers3.append(int(numbers[i]))
            # Same formula/method for (printing) total as used above
            Total = sum(numbers3)
            commaTotal = "{:,}".format(Total)
            print("{0:<25}{1:<15}{2:>0}\n".format("", "Total", str(commaTotal).rjust(10)))
            numbers3.clear()

        # If user does not enter any information
        if not state and not disease and not year:
            #ask user whether they would like to see entire database
            output = input("Error: You did not input any information.\n\
Would you like to view all disease data?\n\
It might take a minute to process. Please enter Yes or No: ")
            YES = 'YES'
            NO = 'NO'
            # if they do, print following lines, including header, and every index of lists containing
            #states, diseases, numbers of occurrence, and years
            if output.upper() == YES:
                print("All Data:")
                print("{0:<25}{1:<15}{2:>10}{3:>15}".format("State", "Disease", "Number", "Year"))
                print()
                for i in range(len(states)-1):
                    if (int(years[i]) < int(years[i+1])) or (diseases[i] < diseases[i+1]):
                        print("{0:<25}{1:<15}{2:>0}{3:>15}\n".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                    else:
                        print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[i], diseases[i], str(numbers2[i]).rjust(10), years[i]))
                print("{0:<25}{1:<15}{2:>0}{3:>15}".format(states[-1], diseases[-1], str(numbers2[-1]).rjust(10), years[-1]))
                print("{0:<25}{1:<15}{2:>0}".format("", "Total", str(commaTotal).rjust(10)))
                print()
                print()
            # if not, print a goodbye message
            if output.upper() == NO:
                print("We assume you would like to exit the program. Have a beautiful day!")
                quit()

# call function
format_disease_data(file)


