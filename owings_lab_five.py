"""Owings Lab Five"""
import pandas as pd
import matplotlib.pyplot as plt

pop_change = pd.read_csv("PopChange.csv")
housing = pd.read_csv("Housing.csv")
merged = pd.concat([pop_change, housing])


# Statistics Function
def statistics_function(column, x_title):
    """Statistics Function"""
    precision = 2
    count = merged[column].count()
    mean = merged[column].mean()
    stan_dev = merged[column].std()
    minimum = merged[column].min()
    maximum = merged[column].max()
    plt.hist(merged[column], bins=50, color="#008fd5", edgecolor="black")
    plt.title(column)
    plt.xlabel(x_title)
    plt.ylabel("Quantity")
    plt.grid()
    print("Count = " + "{:.{}f}".format(count, precision))
    print("Mean = " + "{:.{}f}".format(mean, precision))
    print("Standard Deviation = " + "{:.{}f}".format(stan_dev, precision))
    print("Min = " + "{:.{}f}".format(minimum, precision))
    print("Max = " + "{:.{}f}".format(maximum, precision) + "\n")
    plt.show()
# End Statistics Function


# Housing Menu Function
def housing_menu_function():
    """Housing Menu Function"""
    housing_menu = True
    while housing_menu:
        print("""Select the Column you want to analyze:
a. Age
b. Bedrooms
c. Built Year
d. Rooms
e. Utility
f. Exit Column
        """)
        housing_menu = input("")
        if housing_menu == "a":
            print("\nYou Selected Age")
            statistics_function("AGE", "Ages")
        elif housing_menu == "b":
            print("\nYou Selected Bedrooms")
            statistics_function("BEDRMS", "Bedrooms")
        elif housing_menu == "c":
            print("\nYou Selected Built Year")
            statistics_function("BUILT", "Year")
        elif housing_menu == "d":
            print("\nYou Selected Rooms")
            statistics_function("ROOMS", "Rooms")
        elif housing_menu == "e":
            print("\nYou Selected Utility")
            statistics_function("UTILITY", "Utility cost")
        elif housing_menu == "f":
            print("\nYou selected to exit the column menu")
            housing_menu = False
        else:
            print("\nNot Valid Choice Try again")
# End Housing Menu Function


# Pop Change Menu Function
def pop_change_menu_function():
    """Pop Change Menu Function"""
    pop_menu = True
    while pop_menu:
        print("""Select the Column you want to analyze:
a. Pop Apr 1
b. Pop Jul 1
c. Change Pop
d. Exit Column
        """)
        pop_menu = input("")
        if pop_menu == "a":
            print("\nYou Selected Pop Apr 1.")
            statistics_function("Pop Apr 1", "Total Population")
        elif pop_menu == "b":
            print("\nYou Selected Pop Jul 1.")
            statistics_function("Pop Jul 1", "Total Population")
        elif pop_menu == "c":
            print("\nYou Selected Change Pop.")
            statistics_function("Change Pop", "Total Population")
        elif pop_menu == "d":
            print("\nYou selected to exit the column menu")
            pop_menu = False
        else:
            print("\nNot Valid Choice Try again")
# End Pop Change Menu Function


# Main Menu Function
def menu_function():
    """Main Menu Function"""
    menu = True
    while menu:
        print("""
Select the file you want to analyze:
1. Population Data
2. Housing Data
3. Exit the Program
        """)
        menu = input("")
        if menu == "1":
            print("You have entered Population Data.")
            pop_change_menu_function()
        elif menu == "2":
            print("\nYou have entered Housing Data.")
            housing_menu_function()
        elif menu == "3":
            print("")
            menu = False
        else:
            print("\nNot Valid Choice Try again")
# End Main Menu Function


print("*"*17, "Welcome to the Python Data Analysis App", "*"*17)
menu_function()
print("*"*17, "Thanks for using the Data Analysis App", "*"*17)
