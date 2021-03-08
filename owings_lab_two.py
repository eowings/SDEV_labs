"""Owings Project Two"""
import secrets
import random
import string
import sys
from datetime import date
import numpy as np
# Begin Password Function
def password_function():
    """Password Function"""
    length = input ("How long would you like your password?"
                    " (type a number between 8 and 100): ")
    while not length.isdigit() or int(length) not in range(8, 101):
        length = input("Please enter a valid integer between 8 and 100: ")
    total = int(length)
    lc_amount = input("Enter the minimum lower case characters you would "
                      "like your password to have: ")
    while not lc_amount.isdigit() or int(lc_amount) not in range(0, 101) or \
            int(lc_amount)>total:
        lc_amount = input("Please enter a valid integer between 0 and 100 "
                          "and also ensure you have not exceeded your chosen "
                          "password length: ")
    uc_amount = input("Enter the minimum upper case characters you would "
                      "like your password to have: ")
    while not uc_amount.isdigit() or int(uc_amount) not in range(0, 101) or \
            int(lc_amount) + int(uc_amount)>total:
        uc_amount = input("Please enter a valid integer between 0 and 100 "
                          "and also ensure you have not exceeded your chosen "
                          "password length: ")
    lc_uc_amount = int(lc_amount) + int(uc_amount)
    num_amount = input("Enter the minimum numbers you would "
                       "like your password to have: ")
    while not num_amount.isdigit() or int(num_amount) not in range(0, 101)or \
            int(lc_uc_amount) + int(num_amount)>total:
        num_amount = input("Please enter a valid integer between 0 and 100 "
                           "and also ensure you have not exceeded your chosen "
                           "password length: ")
    lc_uc_num_amount = int(lc_uc_amount) + int(num_amount)
    special_amount = input("Enter the minimum special characters you would "
                           "like your password to have: ")
    while not special_amount.isdigit() or int(special_amount) \
            not in range(0, 101) or int(lc_uc_num_amount) + \
            int(special_amount)>total:
        special_amount = input("Please enter a valid integer between 0 and "
                               "100 and also ensure you have not exceeded "
                               "your chosen password length: ")
    lc_uc_num_spc_amount = int(lc_uc_num_amount) + int(special_amount)
    lc_amount = int(lc_amount)-1
    uc_amount = int(uc_amount)-1
    num_amount = int(num_amount)-1
    special_amount = int(special_amount)-1
    subtract_total = total - lc_uc_num_spc_amount
    all_list = ([secrets.choice(string.punctuation),
                 secrets.choice(string.digits),
                 secrets.choice(string.ascii_lowercase),
                 secrets.choice(string.ascii_uppercase)] +
                [secrets.choice(string.ascii_lowercase) for dummy_i in
                 range(lc_amount)]
                +
                [secrets.choice(string.ascii_uppercase) for dummy_i in
                 range(uc_amount)]
                +
                [secrets.choice(string.punctuation) for dummy_i in
                 range(num_amount)]
                +
                [secrets.choice(string.digits) for dummy_i in
                 range(special_amount)]
                +
                [secrets.choice(string.ascii_lowercase
                                + string.ascii_uppercase
                                + string.punctuation
                                + string.digits) for dummy_i in
                range(subtract_total)]
                )
    random.shuffle(all_list)
    password = "You Chose A Password That Is " + length + \
               " Characters Long\nyour password is: " + \
               ''.join(all_list)
    print("***************************************************************"
          "*************************")
    print(password)
    print("***************************************************************"
          "*************************")
# End Password Function.
#Begin Percentage Function
def percentage_function():
    """Percentage Function"""
    numerator = input("Enter your positive integer numerator ")
    while not numerator.isdigit() or int(numerator) not in range(1, 101):
        numerator = input("Please try to enter your integer again: ")
    denominator = input("Enter your positive integer "
                                  "denominator: ")
    while not denominator.isdigit() or int(denominator) \
            not in range(1, sys.maxsize):
        denominator = input("Please try to enter your "
                                      "integer again: ")
    decimal = input("Enter your positive integer float "
                              "precision: ")
    while not decimal.isdigit() or int(decimal) \
            not in range(1, sys.maxsize):
        decimal = input("Please try to enter your integer again: ")
    string_denominator = str(denominator)
    solution = int(numerator)/int(denominator)*100
    format_solution = (f'{solution:.{decimal}f}')
    print ("******************************************************************"
           "**********************")
    print(numerator + " / " + string_denominator + " yields: " +
          format_solution + " percent.")
    print ("******************************************************************"
           "**********************")
#End Percentage Function
# Begin Days Fucntion
def days_function():
    """Days Function"""
    d_0 = date.today()
    d_1 = date(2025, 7, 4)
    delta = d_1 - d_0
    days_string = str(delta.days)
    print ("******************************************************************"
           "**********************")
    print("There are " + days_string + " until July 4, 2025.")
    print ("******************************************************************"
           "**********************")
# End Days Function
# Begin Cosine Function
def cosine_function():
    """Cosine Function"""
    a_to_c_length = input("Enter a positive integer for line "
                                    "a <-> c length: ")
    while not a_to_c_length.isdigit() or int(a_to_c_length) \
            not in range(1, sys.maxsize):
        a_to_c_length = input("Please try to enter your "
                                                "integer again: ")
    b_to_c_length = input("Enter a positive integer for line "
                                    "b <-> c length: ")
    while not b_to_c_length.isdigit() or int(b_to_c_length) \
            not in range(1, sys.maxsize):
        b_to_c_length = input("Please try to enter your "
                                        "integer again: ")
    angle_of_line_a_and_b = input("Enter a positive integer for line"
                                            "b <-> c length: ")
    while not angle_of_line_a_and_b.isdigit() or int(angle_of_line_a_and_b) \
            not in range(1, sys.maxsize):
        angle_of_line_a_and_b = input("Please try to enter your "
                                                "integer again: ")
    a_to_c_length = int(a_to_c_length)
    b_to_c_length = int(b_to_c_length)
    angle_of_line_a_and_b = int(angle_of_line_a_and_b)
    rad_angle_of_line_a_and_b = np.deg2rad(angle_of_line_a_and_b)
    sq_plus_sq = a_to_c_length**2 + b_to_c_length**2
    two_x_a_x_b = 2 * a_to_c_length*b_to_c_length
    c_cosine = np.cos(rad_angle_of_line_a_and_b)
    solve = np.sqrt(sq_plus_sq - two_x_a_x_b * c_cosine)
    format_solve = "{:.2f}".format(solve)
    print ("******************************************************************"
           "**********************")
    print(format_solve + " is the length of c.")
    print ("******************************************************************"
           "**********************")
# End Cosine Fucntion
# Begin Volume Function
def volume_function():
    """Volume Function"""
    radius = input("Enter a positive integer for the radius of the "
                             "cylinder: ")
    while not radius.isdigit() or int(radius) not in range(1, sys.maxsize):
        radius = input("Please try to enter your "
                                        "integer again: ")
    height = input("Enter a positive integer for the height of the "
                             "cylinder: ")
    while not height.isdigit() or int(height) not in range(1, sys.maxsize):
        height = input("Please try to enter your "
                                        "integer again: ")
    radius = int(radius)
    height = int(height)
    volume = np.pi*pow(radius,2)*height
    fomat_volume = "{:.5f}".format(volume)
    print ("******************************************************************"
           "**********************")
    print(fomat_volume + " is the volume of the Right Circular Cylinder")
    print ("******************************************************************"
           "**********************")
# End Volume Function
# Menu Function
def menu_function():
    """Menu Function"""
    menu=True
    while menu:
        print("""
        Please Make A Selction From The Menu Below.
        a. Generate Secure Password
        b. Calculate and Format a Percentage
        c. How many days from today until July 4, 2025?
        d. Use the Law of Cosines to calculate the leg of a triangle.
        e. Calculate the volume of a Right Circular Cylinder
        f. Exit program
        """)
        menu=input("What would you like to do? ")
        if menu=="a":
            password_function()
        elif menu=="b":
            percentage_function()
        elif menu=="c":
            days_function()
        elif menu=="d":
            cosine_function()
        elif menu=="e":
            volume_function()
        elif menu=="f":
            print("\nGoodbye")
            menu = None
        else:
            print("\nNot Valid Choice Try again")
# End Menu Function
print(" Welcome to the Python SDEV300 Lab 2 Application.")
menu_function()
