import csv
import os
dir (csv)

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Initialize a vote counter
total_votes = 0

# Candidates Options and Candidates Votes
candidate_options = []
# 1. Declare an empty dictionary
candidates_votes = {}

# Open the elections results and read the file
with open(file_to_load, 'r') as election_data:

    #Read the file with the reader function
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    print (headers)

    #Print each row in the CSV file
    for row in file_reader:
        # Add votes 
        total_votes += 1 

        # Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count with a key
            candidates_votes[candidate_name] = 0
        
        candidates_votes[candidate_name] += 1



# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 1. Iterate through the candidate list
for candidate_name in candidates_votes:
    #Retrive votes from a candidate
    votes = candidates_votes[candidate_name] 
    
    #Calculate the percentage of votes
    vote_percentage = (float(votes)/ float(total_votes) * 100)
    print (f"{candidate_name} : received {vote_percentage:.1f}% of the total votes\n")

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Determine if votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # Set winning count, winning percentage and winning candidate
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

print ("--------------------------------------")
print (f"Winner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}%")
print ("--------------------------------------")

#To do: perform analysis
with open(file_to_load) as election_data:
    #Print the file object
    print(election_data)

# Create a file to save with a direct or indirect path to the file
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file
    txt_file.write(
        "Counties in the Election\n"
        "-------------------------\n"
        "Araphoe\nDenver\nJefferson")


#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Close the file