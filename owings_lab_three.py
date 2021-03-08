"""Owings Lab Three"""
import pandas as pd
from PIL import Image
import requests
import matplotlib.pyplot as plt

state_dict = pd.read_csv("statecapflowerpop.csv").to_dict()
keys = ["State", "Population"]
state_dict_top = {x: state_dict[x] for x in keys}
keys2 = ["State", "Capital", "Population", "Flower"]
state_dict_one = {x: state_dict[x] for x in keys2}
keys3 = ["State", "Capital", "Population"]
state_dict_2 = {x: state_dict[x] for x in keys3}

# List States Function
def list_states_function():
    """List States Function"""
    data_g = pd.DataFrame(state_dict_one, columns=["State", "Capital",
                                                   "Population", "Flower"])
    data_sorted = data_g.sort_values(by=["State"])
    print(data_sorted)
# End List States Function
# List States Function
def list_states_flowerimage_function():
    """List States With Flower Image Function"""
    state_dict_two = pd.read_csv("statecapflowerpop.csv").set_index(
        "State").to_dict(orient="index")
    real_state = False
    while not real_state:
        name_astate = input("Name a U.S. state: ").title()
        if name_astate in state_dict_two.keys():
            data_h = pd.DataFrame(state_dict_one, columns=["State", "Capital",
                                                           "Population"])
            print(data_h.loc[data_h["State"] == name_astate])
            url_pic = state_dict_two[name_astate]["URL"]
            response = requests.get(url_pic, stream=True)
            img = Image.open(response.raw)
            img.show()
            real_state = True
        else:
            print("Your entry is not recognised as a U.S. state, please "
                  "verify spelling and try again.")
# End List States Function
# List States Function
def states_bargraph_function():
    """Bar Graph States Top Five Populations Function"""
    data_f = pd.DataFrame(state_dict_top, columns=["State", "Population"])
    df1 = data_f.nlargest(5, "Population")
    print(df1)
    new_colors = ["blue", "green"]
    plt.bar(df1["State"], df1["Population"], color=new_colors)
    plt.title("Top Five Populated States In U.S.", fontsize=14)
    plt.xlabel("State", fontsize=14)
    plt.ylabel("Population", fontsize=14)
    plt.show()
# End List States Function
# List States Function
def update_states_pop_function():
    """Change States Population Function"""
    state_dict_three = pd.read_csv("statecapflowerpop.csv", sep=",").set_index(
        "State").to_dict(orient="index")
    real_state = False
    real_number = False
    name_astate = ""
    new_pop = ""
    while not real_state:
        name_astate = input("Name a U.S. state: ").title()
        if name_astate in state_dict_three.keys():
            real_state = True
        else:
            print("Your entry is not recognised as a U.S. state, please "
                  "verify spelling and try again.")
    while not real_number:
        new_pop_str = input("Enter the updated population: ")
        if new_pop_str.isdigit():
            new_pop =int(new_pop_str)
            real_number = True
        else:
            print("Your entry is not recognised as a valid integer, "
                  "please try again")
    for _, value in sorted(state_dict_top.items()):
        for k, val in value.items():
            if val == name_astate:
                state_dict["Population"][k] = new_pop
                # make it permanent.
                #data_update = pd.DataFrame(state_dict,
                #                      columns=["State", "Capital",
                #                               "Population", "Flower", "URL"])
                #data_update.to_csv('statecapflowerpop.csv')
# End List States Function
# Menu Function
def menu_function():
    """Menu Function"""
    menu = True
    while menu:
        print("""
        Please Make A Selction From The Menu Below.
        1. Display all U.S. States in Alphabetical order along with the 
        Capital, State Population, and Flower
        2. Search for a specific state and display the appropriate Capital 
        name, State Population, and an image of the associated State Flower.
        3. Provide a Bar graph of the top 5 populated States showing their 
        overall population.
        4. Update the overall state population for a specific state.
        5. Exit the program
        """)
        menu = input("What would you like to do? ")
        if menu == "1":
            list_states_function()
        elif menu == "2":
            list_states_flowerimage_function()
        elif menu == "3":
            states_bargraph_function()
        elif menu == "4":
            update_states_pop_function()
        elif menu == "5":
            print("\nGoodbye")
            menu = None
        else:
            print("\nNot Valid Choice Try again")
# End Menu Function
print(" Welcome to the Python SDEV300 Lab 3 Application.")
menu_function()
