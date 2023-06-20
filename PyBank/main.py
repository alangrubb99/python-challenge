# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

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
    decrease_date = "Jan-01"
    increase_date = "Jan-01"

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
    
        totalmonths =totalmonths +1
        if lastincome != 0:
             deltaincome = int(row[1]) - lastincome
             deltatotal = deltatotal + deltaincome

             if deltaincome < greatestdecrease:
                  greatestdecrease = deltaincome
                  decrease_date = row[0]

             if deltaincome > greatestincrease:
                  greatestincrease = deltaincome
                  increase_date = row[0]

        lastincome = int(row[1])
        income = int(row[1]) + income
    #   print("deltaincome " + str(deltaincome))
    #   print("lastincome: " + str(lastincome))

    deltatotal = round(deltatotal / 85,2)

    print("Financial Analysis ")
    print("--------------------------------------")
    print("Total Months: " + str(totalmonths))
    print("Total: " + str(income))
    print("Average Change: " + str(deltatotal))
    print("Greatest Increase in Profits: " +str(increase_date)+ " "+str(greatestincrease))
    print("Greatest Decrease in Profits: " +str(decrease_date)+" "+str(greatestdecrease))   

    #for col in row:
    #           print("%10s"%col,end=" "),
    #  print('\n')

    # output to text file
    with open('PyBank.txt', 'w') as f:

        f.write("Financial Analysis ")
        f.write('\n')
        f.write("--------------------------------------")
        f.write('\n')
        f.write("Total Months: " + str(totalmonths))
        f.write('\n')
        f.write("Total: " + str(income))
        f.write('\n')
        f.write("Average Change: " + str(deltatotal))
        f.write('\n')
        f.write("Greatest Increase in Profits: " +str(increase_date)+ " "+str(greatestincrease))
        f.write('\n')
        f.write("Greatest Decrease in Profits: " +str(decrease_date)+" "+str(greatestdecrease))   



