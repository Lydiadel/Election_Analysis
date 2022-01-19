# PyPoll Election Analysis Challenge
# 18/ 01/ 2022
# Author: Lydia Delgado Uriarte

import csv
import os
dir (csv)

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
# Create a file to save with a direct or indirect path to the file
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

#Initialize a vote counter
total_votes = 0

# Candidates Options and Candidates Votes
candidate_options = []
candidates_votes = {}

# 1: Create a county list and county votes dictionary
county= []
county_votes= {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
county_voter = 0

# Open the elections results and read the file
with open(file_to_load, 'r') as election_data:

    #Read the file with the reader function
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        # Add votes 
        total_votes += 1 

        # Get the candidate name from each row
        candidate_name = row[2]

        # 3: Extract the county from each row
        county_name = row[1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count with a key
            candidates_votes[candidate_name] = 0
        
        # 4a: If statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county:
            # 4b: Add the existing county to the list of counties.
            county.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        county_votes[county_name] += 1
        candidates_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    
    #Print final vote in terminal
    election_results = (
        "\nElection Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        "-------------------------\n\n")
    txt_file.write(election_results)
    print(election_results)

    print ("County Votes:\n")
    
    # 6a: For loop to get the county from the county dictionary:
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = (float(votes)/float(total_votes) * 100)
        # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({votes:,})\n")
        print (county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > county_voter) :
            #Set largest county and county voter
            county_voter = votes
            largest_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout = (
        "\n------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        "------------------------\n")
    
    print(largest_turnout)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout)

    # Iterate through the candidate list
    for candidate_name in candidates_votes:
        #Retrive votes from a candidate
        votes = candidates_votes[candidate_name] 
        #Calculate the percentage of votes
        vote_percentage = (float(votes)/ float(total_votes) * 100)
        candidate_results = (f"{candidate_name} received {vote_percentage:.1f}% ({votes:,})\n")
        print (candidate_results)
        txt_file.write(candidate_results)
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Determine if votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # Set winning count, winning percentage and winning candidate
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winning candidate (to terminal)
    winning_candidate_summary= (
        f"------------------------\n"
        f"Winner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        "------------------------")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
