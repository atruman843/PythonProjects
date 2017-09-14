##################################################
# atruman843 9/14/17
# this program tells you what to do when it is raining

while True: # beginning of while loop
    s = input('Is it raining? : ') # asks the user to input whether or not it is raining
    if s.lower() == 'yes': # if the user says yes, it continues the loop
        a = input('Do you have an umbrella? : ') # asks the user to state whether or not they have an umbrella
        if a.lower() == 'yes': # if the user responds 'yes', code tells user to go outside
            print('Go outside')
            break
        elif a.lower() == 'no': # if the user says 'no', prompts them to wait inside
            print('Wait a while')
            b = input('Is it still raining? : ') # asks for input on the weather
            if b.lower() == 'yes':
                print('Give up.')
                break
            else:
                print('Go outside')
                break
    elif s.lower() == 'no':
        print('Go outside')
        break
    else:
        print('Please Try again')
print('RAIN RAIN GO AWAY')
