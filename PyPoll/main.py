# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath) as csvfile:

# Define variables
    Voter_ID = []   
    County = []
    Candidate1 = "Charles Casper Stockham"
    Candidate2 = "Diana DeGette"
    Candidate3 = "Raymon Anthony Doane"
    Candidate1_Count = 0
    Candidate2_Count = 0
    Candidate3_Count = 0
    votecount = 0
    Next_Candidate = "Alaan Lamar Grubb"
    candidate_total = 0

    # CSV reader specifies delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
       
    # init variables for tracking voters and candidates
        votecount = votecount + 1
        Candidate = row[2]

        if Candidate == Candidate1:
             Candidate1_Count = Candidate1_Count + 1

        elif Candidate == Candidate2:
            Candidate2_Count = Candidate2_Count + 1

        elif Candidate == Candidate3:  
             Candidate3_Count = Candidate3_Count + 1
    
        # determine the winner by comparing voter counts

        if Candidate1_Count > Candidate2_Count and Candidate1_Count > Candidate3_Count:
            winner = Candidate1

        elif Candidate2_Count > Candidate1_Count and Candidate2_Count > Candidate3_Count:
            winner = Candidate2

        else:  
            winner = Candidate3

    # get % from candidate counts   
    percentage1 = round((Candidate1_Count / votecount)*100,3)
    percentage2 = round((Candidate2_Count / votecount)*100,3)
    percentage3 = round((Candidate3_Count / votecount)*100,3)

    # output to terminal
  
    print("Election Results")
    print("-----------------")
    print("Total Votes: " + str(votecount))
    print("-----------------------")
    print(Candidate1 + " " + str(percentage1) + "%  " + str(Candidate1_Count))
    print(Candidate2 + " " + str(percentage2) + "%  " + str(Candidate2_Count))
    print(Candidate3 + " " + str(percentage3) + "%  " + str(Candidate3_Count))
    print("-------------------------")
    print("Winner: " +str(winner)) 
    print("-------------------------")

    # output to text file
    with open('PyPoll.txt', 'w') as f:
        f.write('\n')  
        f.write("Election Results") 
        f.write('\n')    
        f.write("-----------------")
        f.write('\n')
        f.write("Total Votes: " + str(votecount))
        f.write('\n')
        f.write("-----------------------")
        f.write('\n')
        f.write(Candidate1 + " " + str(percentage1) + "%  " + str(Candidate1_Count))
        f.write('\n')
        f.write(Candidate2 + " " + str(percentage2) + "%  " + str(Candidate2_Count))
        f.write('\n')
        f.write(Candidate3 + " " + str(percentage3) + "%  " + str(Candidate3_Count))
        f.write('\n')
        f.write("-------------------------")
        f.write('\n')
        f.write("Winner: " +str(winner)) 
        f.write('\n')
        f.write("-------------------------")
        f.write('\n')