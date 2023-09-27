# BABY NAMES DATA ASSIGNMENT START CODE

import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close()
    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    for i in range(len(baby_data)):
        baby_name = baby_data[i].get("name")
        baby_rank = baby_data[i].get("rank")
        baby_gender = baby_data[i].get("gender")
        print(f"{baby_name} (Rank: {baby_rank}, Gender: {baby_gender})")


def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER")
    gender_selection = input("Enter a gender (Boy/Girl): ")
    for i in range(len(baby_data)):
        baby_name = baby_data[i].get("name")
        baby_rank = baby_data[i].get("rank")
        baby_gender = baby_data[i].get("gender")
        if baby_gender == gender_selection:
            print(f"{baby_name} (Rank: {baby_rank}, Gender: {baby_gender})")

def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")
    rank_selection_minimum = input("Enter a minimum rank: ")
    rank_selection_maximum = input("Enter a maximum rank: ")
    baby_count = 0
    for i in range(len(baby_data)):
        baby_name = baby_data[i].get("name")
        baby_rank = baby_data[i].get("rank")
        baby_gender = baby_data[i].get("gender")
        if baby_rank >= int(rank_selection_minimum) and baby_rank <= int(rank_selection_maximum):
            print(f"{baby_name} (Rank: {baby_rank}, Gender: {baby_gender})")
            baby_count += 1
    print(f"Number of names found: {baby_count}")

def searchStartLetter(baby_data):
    # Insert User Item into a Position
    print("\nSEARCH BY START LETTER")
    letter_selection = input("Enter a starting letter: ")
    baby_count = 0
    for i in range(len(baby_data)):
        baby_name = baby_data[i].get("name")
        baby_rank = baby_data[i].get("rank")
        baby_gender = baby_data[i].get("gender")
        if baby_name[0] == letter_selection:
            print(f"{baby_name} (Rank: {baby_rank}, Gender: {baby_gender})")
            baby_count += 1
    print(f"Number of names found: {baby_count}")

def searchNameLength(baby_data):
    # Remove item from position
    print("\nSEARCH BY NAME LENGTH")
    name_length_selection = input("Enter a name length: ")
    baby_count = 0
    for i in range(len(baby_data)):
        baby_name = baby_data[i].get("name")
        baby_rank = baby_data[i].get("rank")
        baby_gender = baby_data[i].get("gender")
        if len(baby_name) == int(name_length_selection):
            print(f"{baby_name} (Rank: {baby_rank}, Gender: {baby_gender})")
            baby_count += 1
    print(f"Number of names found: {baby_count}")

# Invoke main to begin program
main()


