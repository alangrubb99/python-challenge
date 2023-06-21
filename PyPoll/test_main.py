# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
# Lists for Candidates and Votes
votecount = 0
winning = 0
Candidates_List=[]
Candidates_Votes={}

# Method 2: Improved Reading using CSV module
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath) as csvfile:

# Define variables
    

    # CSV reader specifies delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    print("Election Results")
    print("----------------------------")
        
    # Read each row of data after the header
    for row in csvreader:
       
    # init variables for tracking voters and candidates
        votecount = votecount + 1
        Candidate = row[2]
        if Candidate not in Candidates_List:
            Candidates_List.append(Candidate)
            Candidates_Votes[Candidate]=0
            
        Candidates_Votes[Candidate] = Candidates_Votes[Candidate] + 1

    print("Total Votes: " + str(votecount))
    print("-----------------------------------")

    for Candidate in Candidates_Votes:
        Count_Votes = Candidates_Votes.get(Candidate)
        Percentage = round(Count_Votes / votecount * 100,3)

        if Count_Votes > winning:
            winning = Count_Votes
            winning_candidate = Candidate

        print(Candidate+ " " + str(Percentage) + "%  " + str(Count_Votes)) 

    print("-----------------------------------")
    print("Winner: " +str(winning_candidate)) 
    print("-----------------------------------")

    
    


    