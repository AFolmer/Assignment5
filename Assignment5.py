# Python Basics Assignment 5: Mailroom
# AFolmer
# Created 7/25/2023
# Create and maintain a list of donors and their donations and use this data to generate thank you emails
# and donation summary reports by donor

import pickle
from tabulate import tabulate


def menu_choice(max_value):
    """Validate that user menu choice is an integer within range
    :param max_value: the number of menu choices
    :return int_choice: validated menu choice"""
    while True:
        try:
            int_choice = int(input(f"Enter menu choice 1 - {max_value}: "))
        except ValueError:
            print("Choice must be an integer.")
        else:
            if 1 <= int_choice <= max_value:
                break
            else:
                print(f"Choice must be between 1 - {max_value}")
    return int_choice


def open_mailroom_pickle():
    """Try to open pickle file with donor and donation list.  If file cannot be opened, create lists
    :return donor_list: list of donors
    :return donation list: list of donations and associated donors"""
    try:
        f = open("mailroom_lists.dat", "rb")
        donor_list = pickle.load(f)
        donation_list = pickle.load(f)
        f.close()
    except FileNotFoundError:
        print("Mailroom saved data not found.")
        donor_list = []
        donation_list = []
    return donor_list, donation_list


def save_mailroom_pickle(donor_list, donation_list):
    """Try to save donor and donation lists to a pickle file
    :param donor_list: list of donors
    :param donation_list: list of donations and associated donors"""
    try:
        f = open("mailroom_lists.dat", "wb")
        pickle.dump(donor_list, f)
        pickle.dump(donation_list, f)
        f.close()
        print("Donor and donation lists saved.")
    except:
        print("Error, inventories not saved.")


def print_donor_list(donor_list):
    """Print list of donors
    :param donor_list: list of donors"""
    print("Donor List")
    print(tabulate(donor_list, headers=["Donor Name", "Donor E-mail"]))


def add_donor(donor_name):
    """Add new donor to list
    :param donor_name: name of new donor
    :return donor_row: list of donor information to append to main donor list"""
    name = donor_name
    # Check to validate email field contains a @ and .
    while True:
        email = input("What is the donor's e-mail address? ")
        if '@' and '.' in email:
            donor_row = [name, email]
            break
        else:
            print(f'{email} is not a valid email address')
    return donor_row


def add_donation(donor_name):
    """Validate that donations are greater than zero and saved as a float
    :param donor_name: name of the donor
    :return donation_row: donation donor and amount"""
    while True:
        try:
            # User input saved as a float
            donation_amount = float(input("What is the amount of the donation? "))
            # Check that donation is greater than 0
            if 0 <= donation_amount:
                donation_amount = round(donation_amount, 2)
                break
            else:
                print("Donation amount must be greater than 0.")
        # Notify user if entry cannot be saved as a float
        except ValueError:
            print("Donation amount must be a number.")
    donation_row = [donor_name, donation_amount]
    return donation_row


def generate_thank_you(donation_row):
    """Generate a thank you message for a donation
    :param donation_row: list with donation details name and amount"""
    print(f'Thank you {donation_row[0]} for your generous donation of ${donation_row[1]:,}')


def create_summary_report(donor_list, donation_list):
    """Create summary report by donor with sum of donations, number of donations, and average donation
    :param donor_list: list of donors
    :donation_list: list of donations"""
    summary_report = []
    # Sort donor list alphabetically by donor
    list.sort(donor_list, key=lambda donor_list: donor_list[0])
    for donor in donor_list:
        # List comprehension to pull out a list of donation values for each donor
        donor_donations = [donation[1] for donation in donation_list if donor[0] == donation[0]]
        # Check donations exist for the donor to prevent dividing by zero
        if len(donor_donations) == 0:
            print(f'{donor[0]} has no donations.')
        # Calculate sum and count of donations, then average
        else:
            donor_sum = sum(donor_donations)
            donor_count = len(donor_donations)
            donor_average = donor_sum/donor_count
            # Append donor summary values to summary_report table
            summary_report.append([donor[0], "$", donor_sum, donor_count, "$", donor_average])
            donor_headers = ["Donor", "", "Total Given", "Num Gifts", "", "Average Gift"]
    print(tabulate(summary_report, headers=donor_headers, floatfmt=",.2f"))


# Main code block for mailroom program
print("Welcome to Mailroom!")
# Open pickle file with saved donors and donations or create new lists
donor_list, donation_list = open_mailroom_pickle()
MAX_MENU_CHOICE = 3
while True:
    print("Main Menu: \n1. Send a thank you \n2. Print donor report \n3. Save and exit")
    main_menu_choice = menu_choice(MAX_MENU_CHOICE)
    # Get user input to enter donation and print a thank you
    if main_menu_choice == 1:
        donor_name = input("What is the donor's name?  "
                           "\nType 'list' for list of donors or 'exit' to return to main menu. ")
        # Print list of donors
        if donor_name.lower() == "list":
            print_donor_list(donor_list)
        # Exit to main menu
        elif donor_name.lower() == 'exit':
            print("Donation cancelled.")
        # Check if donor is in donor_list and if yes log donation
        elif any(donor_name in sublist for sublist in donor_list):
            donation_row = add_donation(donor_name)
            # If user confirms donation, add to donation list and generate thank you
            sub_menu_choice = input("Enter 'Y' to confirm donation: ")
            if sub_menu_choice.lower() == 'y':
                donation_list.append(donation_row)
                generate_thank_you(donation_row)
            else:
                print("Donation cancelled.")
        else:
            # If donor is not in donor list, add them
            sub_menu_choice = input(f'{donor_name} not found.  Enter Y to add donor to list: ')
            if sub_menu_choice.lower() == 'y':
                donor_row = add_donor(donor_name)
                donor_list.append(donor_row)
                # Log donation for new donor
                donation_row = add_donation(donor_name)
                sub_menu_choice = input("Enter 'Y' to confirm donation: ")
                # If user confirms donation, add to list and generate thank you
                if sub_menu_choice.lower() == "y":
                    donation_list.append(donation_row)
                    generate_thank_you(donation_row)
            else:
                print("Donation cancelled.")
    elif main_menu_choice == 2:
        print("1. Print list of all donations \n2. Print donation summary report \n3. Main menu")
        report_choice = menu_choice(3)
        # Sort donations by donor and print list of all donations
        if report_choice == 1:
            list.sort(donation_list, key=lambda donation_list: donation_list[0])
            print(tabulate(donation_list, headers=["Donor", "Amount"], floatfmt=",.2f"))
        # Create summary report of donors and their total, count, and average giving
        elif report_choice == 2:
            create_summary_report(donor_list, donation_list)
        else:
            break
    elif main_menu_choice == 3:
        print("Exit")
        save_mailroom_pickle(donor_list, donation_list)
        break
    else:
        print("Congratulations on breaking function to validate menu choices!")