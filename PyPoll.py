import csv
import os
dir (csv)

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

# Open the elections results and read the file
with open(file_to_load, 'r') as election_data:

    #Read the file with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print (headers)


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