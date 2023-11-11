#!usr/bin/env/ python3
# Created By: Marli Peters
# Date: Nov, 11, 2023
# This program asks users for their salary and time with a company then
# if they have been with the company for 5 or more years it will calculate
# a 5% bonus based on their salary and displays the user their bonus.


def main():
    # ask user for information to get bonus and set variables
    salary_str = str(input("Please enter your yearly salary: "))
    company_time_str = str(input("Please enter your time with the company in years: "))

    # calculating and displaying salary
    try:
        salary_int = int(salary_str)
        company_time_int = int(company_time_str)
        # if user company time is under 5 years
        if company_time_int < 5:
            print("You do not qualify for a bonus.")
        # if user company time is 5+ years
        elif company_time_int >= 5:
            bonus = salary_int * 0.05
            print("Your bonus is {}$!".format(bonus))
    # catch input errors
    except:
        print("Please enter valid numbers.")

    # thank user for playing
    finally:
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
