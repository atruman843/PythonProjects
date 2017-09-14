##################################################
# atruman843 updated 9/14/17
# This code is a password protected address book; allows you to input contacts; allows you to look up contacts
##################################################

with open('Contacts', 'a') as targ_write: # this opens a txt file named 'Contacts' and defines it as targ_write
    print('This program is password protected.')
    print()
    print('Please enter the password to continue.')
    print()
    pass_list = [] # creates a list to store password attempts
    while len(pass_list) < 5: # the while loop will continue until the number of password attempts reaches 5
        password = input('password: ')
        if password == 'GoPanthers!': # the password is GoPanthers; if guessed correctly, the program starts
            while True:
                user_input = input('Would you like to add a contact: ') # asking the user if they want to add a contact
                if user_input.lower() == 'yes': # if the user wants to add a contact they are prompted to do so
                    print('What is their name?')
                    name = input()
                    print('What is their phone number?')
                    phone = input()
                    print('What is their email address?')
                    email = input()
                    contact = ('''{} 
                    Phone: {}
                    Email: {}
                
                    '''.format(name, phone, email))
                    # this takes all of the input from lines 13-18 and formats it so that name, number, and email
                    # are printed in that order
                    targ_write.write(contact.upper()) # the variable 'contact' is written to the txt file
                elif user_input.lower() == 'no': # if the user does not want to add a contact, the loop ends
                    break
                else:
                    print('''Please type 'yes' or 'no'.''')
                    # if the user responds with an invalid command, it prints the only two valid commands
            targ_write.close() # closes and saves the contact list for future use of the program

            contact_list = [] # creates a list for contacts to be added to

            with open('Contacts', 'r') as targ_read: # opens the txt file
                for line in targ_read: # reads each line in the txt file
                    line = line.strip() # strips each line of white space
                    contact_list.append(line) # adds the stripped line to the list defined in line 31

            while True:
                user_lookup = input('Would you like to look up a contact: ')
                # this piece allows users to look up contacts in their address book
                if user_lookup.lower() == 'yes': # if they want to look up a contact, they are prompted to do so
                    name = input('Type the first letters of the person you would like to look up: ')
                    for item in contact_list: # looks at each contact in list from line 31
                        if item.startswith(name.upper()):
                            # if the name starts with letters they typed above, the contact will be printed
                            a = (contact_list[contact_list.index(item.upper()):contact_list.index(item.upper()) + 3])
                            # defines a variable where current line and next two lines are printed
                            print(*a, sep='\n') # prints the variable above and separates it by one line
                elif user_lookup.lower() == 'no': # if the user does not want to look up someone, the loop ends
                    break
                else:
                    print("Please type 'yes' or 'no'.") # if input is invalid, prompted to type a valid response
            break

        else:
            pass_list.append(password) # adds password attempt to password list
            print('You have', 5 - len(pass_list), 'attempts remaining before the program locks.')
            # tells how many attempts are left until the program locks
print('Have a nice day.')