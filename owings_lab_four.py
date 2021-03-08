"""Owings Lab Four"""
import re
import sys
import numpy as np
import pandas as pd


# Proceed Function
def proceed_function():
    """Function will be used to offer an exit to user."""
    print("Do you want to play the Matrix Game?")
    end = input("Enter Y for Yes or N for No:")
    if end in ('n', 'N', 'NO', 'No', 'nO'):
        sys.exit("*"*20+"Thanks for playing Python Numpy"+"*"*20)
# End Proceed Function


# Phone Number Function
def phone_number_function():
    """Phone Number Function"""
    valid_number = False
    while not valid_number:
        phone = input("Enter your phone number XXX-XXX-XXXX: ")
        format_phone = re.match(r"^\d{3}-\d{3}-\d{4}$", phone)
        if format_phone:
            print("Your phone number is: "+format_phone.group())
            valid_number = True
        else:
            print("Your phone number is not in correct format. "
                  "Please renter: ")
# End Phone Number Function


# ZipCode Function
def zipcode_function():
    """ZipCode Function"""
    valid_number = False
    while not valid_number:
        zip_code = input("Enter your zip code+4 (XXXXX-XXXX): ")
        format_zip = re.match("^\\d{5}-\\d{4}$", zip_code)
        if format_zip:
            print("Your zip code is: "+format_zip.group())
            valid_number = True
        else:
            print("Your zip code is not in correct format. Please renter: ")
# End ZipCode Function


# Matrix One Function
def matrix_one_function():
    """Matrix One Function"""
    matrix_one = []
    valid_number = False
    print("Enter your first 3x3 matrix:")
    while not valid_number:
        try:
            for i in range(3):
                row = list(map(int, input().split()))
                matrix_one.append(row)
            valid_number = True
        except ValueError:
            valid_number = False
            matrix_one = []
            print("Matrix can only contain integers, please try again...")
    print("Your first 3x3 matrix is: ")
    for i in matrix_one:
        for j in i:
            print(j, end=" ")
        print()
    matrix_one = np.array(matrix_one)
    return matrix_one
# End Matrix One Function


# Matrix Two Function
def matrix_two_function():
    """Matrix Two Function"""
    valid_number = False
    print("Enter your second 3x3 matrix:")
    matrix_two = []
    while not valid_number:
        try:
            for i in range(3):
                row = list(map(int, input().split()))
                matrix_two.append(row)
            valid_number = True
        except ValueError:
            valid_number = False
            matrix_two = []
            print("Matrix can only contain integers, please try again...")
    print("Your second 3x3 matrix is: ")
    for i in matrix_two:
        for j in i:
            print(j, end=" ")
        print()
    matrix_two = np.array(matrix_two)
    return matrix_two
# End Matrix Two Function


# Set global matrix variables to be used in other functions
def one():
    """"set global for matrix one"""
    global set_matrix_one
    set_matrix_one = matrix_one_function()


def two():
    """"set global for matrix two"""
    global set_matrix_two
    set_matrix_two = matrix_two_function()
# End Set global variables functions


# Show Results Function
def show_results(solve):
    """Function to display results from math functions"""
    for i in solve:
        for j in i:
            print(j, end=" ")
        print()
    print("The Transpose is:")
    transpose = solve.transpose()
    for i in transpose:
        for j in i:
            print(j, end=" ")
        print()
    data = pd.DataFrame(data=solve)
    row_mean = data.mean(axis=1)
    column_mean = data.mean(axis=0)
    print("The mean of each row is:")
    print(row_mean.to_string(index=False))
    print("The mean of each column is:")
    print(column_mean.to_string(index=False))
# End Show Results Function


# Add Function
def add_function():
    """Add Function"""
    solve = np.add(set_matrix_one, set_matrix_two)
    show_results(solve)
# End Add Function


# Subtract Function
def subtract_function():
    """Subtract Function"""
    solve = np.subtract(set_matrix_one, set_matrix_two)
    show_results(solve)
# End Subtract Function


# Multiply Function
def multiply_function():
    """Multiply Function"""
    solve = np.matmul(set_matrix_one, set_matrix_two)
    show_results(solve)
# End Multiply Function


# Element by Element Multiply Function
def ebe_multiply_function():
    """Element by Element Multiply Function"""
    solve = np.multiply(set_matrix_one, set_matrix_two)
    show_results(solve)
# End Element by Element Multiply Function


# Menu Function
def menu_function():
    """Menu Function"""
    while not proceed_function():
        phone_number_function()
        zipcode_function()
        one()
        two()
        print("""
            Please Make A Selection From The Menu Below.
            a. Addition
            b. Subtraction
            c. Matrix Multiplication
            d. Element by element multiplication
            """)
        menu = input("What would you like to do? ")
        if menu == "a":
            add_function()
        elif menu == "b":
            subtract_function()
        elif menu == "c":
            multiply_function()
        elif menu == "d":
            ebe_multiply_function()
        else:
            print("\nNot Valid Choice Try again")
# End Menu Function


print("*"*20+" Welcome to the Python Matrix Application "+"*"*20)
menu_function()
