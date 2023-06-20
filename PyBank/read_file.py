# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath) as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    totalmonths = 0
    income = 0
    deltaincome = 0
    lastincome = 0
    greatestincrease = 0
    greatestdecrease = 0
    deltatotal = 0


    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
    
        totalmonths =totalmonths +1
        if lastincome != 0:
             deltaincome = int(row[1]) - lastincome
             deltatotal = deltatotal + deltaincome

             if deltaincome < greatestdecrease:
                  greatestdecrease = deltaincome

             if deltaincome > greatestincrease:
                  greatestincrease = deltaincome

        lastincome = int(row[1])
        income = int(row[1]) + income
        print("deltaincome " + str(deltaincome))
        print("lastincome: " + str(lastincome))
        for col in row:
                print("%10s"%col,end=" "),
        print('\n')

    deltatotal = int(deltatotal / 85)

    print("Total Months: " + str(totalmonths))
    print("Total: " + str(income))
    print("Change in Profits: " + str(deltatotal))
    print("Greatest Increase in Profits: " + str(greatestincrease))
    print("Greatest Decrease in Profits: " + str(greatestdecrease))   

