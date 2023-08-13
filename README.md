# Assignment 5: Mailroom
The goal of this assignment is to create two lists to manage donations and print thank you notes:
 - Donor list: a list of everyone who's donated to the organization
 - Donation list: details on each individual donation

# Capture donations
First, the program asks for the name of the donor and checks to see if they are already in the donor list.  If not, they are added.

![Try to find donor name in donor list](https://github.com/AFolmer/Assignment5/assets/132308533/b05b9511-aee8-4a26-bb08-a0888ce4ffc4)

Then the domain is captured as a two decimal float using try/except to ensure that the user enters a number greater than 0 and round to round to two decimal places.

![Capture donation as a two decimal float](https://github.com/AFolmer/Assignment5/assets/132308533/16ab0196-9816-4ea1-abfe-a802fda06717)

Finally, a thank you is printed using an f'' string to format the donation with a currency symbol and a , for thousands.

![Thank you message](https://github.com/AFolmer/Assignment5/assets/132308533/3fab421a-4ff3-46b0-8c47-40b7a9299f65)

# Report donations
This program generates two reports: a basic table of all donations and their donors using tabulate and a summary report with the total amount given, number of gifts, and average for each donor.
First, the list is sorted by donor name using donor_list[0] as the key.  Then, a for loop is used with list comprehension to create a sub-list of donations for each donor.  The sub-list is added using sum for total donations, len for number of donations, and average is total/len.  These three metrics and the donor name are saved as a row in list summary_report and printed using tabulate.

![Code to create summary report](https://github.com/AFolmer/Assignment5/assets/132308533/403e50e1-9555-4d03-90dd-c269a063135a)

![Sample summary report](https://github.com/AFolmer/Assignment5/assets/132308533/e4d4900d-d2a5-4865-b869-13cc76dde17c)

