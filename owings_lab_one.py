"""Owings - Week 1 - Lab 1"""
import sys
# list of all abbreviated US states for comparison in state user input.
us_states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
             "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
             "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
             "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
             "VT", "VA", "WA", "WV", "WI", "WY")
def proceed_function():
    """Function will be used to offer an exit to user."""
    end = input('Would you like to continue? yes = y OR no = n.')
    if end in ('n', 'N', 'NO', 'No', 'nO'):
        sys.exit('Thank You for using the voter registration application.')
# Script runs inside while loop to be able to restart if info is wrong at end.
restart: str = 'n'
while str(restart) == 'n':
    # Welcome message.
    print('*****************************************************************')
    print('        Welcome to the Voter Registration Application')
    print('*****************************************************************')
    # End statement will allow the user the option to exit after every entry.
    proceed_function()
    firstname = input('Enter your first name: ')
    while not firstname.isalpha():
        firstname = input('That was not a compatible name type, '
                          'please try again.')
    proceed_function()
    lastname = input('Enter your last name: ')
    while not lastname.isalpha():
        lastname = input('That was not a compatible name type, '
                         'please try again.')
    proceed_function()
    AGE = input("Please enter your age : ")
    # while statement to check user has entered a reasonable age (1 - 120).
    # Oldest person in the U.S. is Hester Ford born 15 Aug 1905 < 120
    while not AGE.isdigit() or int(AGE) not in range(1, 120):
        AGE = input("Please try to enter your age again: ")
    # If statement will exit if user is under 18.
    if int(AGE) < 18:
        sys.exit('You are under the legal age to vote, thank you')
    proceed_function()
    country = input('Are you a U.S. citizen (Yes or No) ')
    # If statement will exit if user not US citizen.
    if country in ('n', 'N', 'NO', 'No', 'nO'):
        sys.exit('You must be a U.S. citizen to vote.')
    proceed_function()
    state = input('Enter your state of residence as a two character '
                  'abbreviation '
                  'all caps: ')
    # while user entered state not in us_states list this question will loop.
    while state not in us_states:
        state = input('Not a valid state abbreviation, did you enter the two '
                      'characters in all caps, try again: ')
    proceed_function()
    zipcode = input('Enter your five or nine digit zip code: ')
    # while loop ensures zip code entered is a five digit long number.
    while len(zipcode) != 5 and len(zipcode) != 9 or not zipcode.isdigit():
        zipcode = input('That was not five or nine digits ')
    proceed_function()
    # Thanks and read back info for review.
    print('Thank You for Using the Voter Registration Application. The details'
          ' you entered are below.')
    print('*****************************************************************')
    print('*     Name: ', firstname, lastname)
    print('*     Age: ', AGE)
    print('*     You ARE a U.S. citizen.')
    print('*     Your state of residency is: ', state)
    print('*     Your zipcode is: ', zipcode)
    print('*****************************************************************')
    # End by entering y or restart while loop by entering n.
    restart = input('If this info is correct type "y" and enter, otherwise '
                    'to restart type "n" end enter.')
