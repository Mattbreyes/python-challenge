#pypoll script
import os
import csv

file_path = "Resources/election_data.csv"

with open(file_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    # store header
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # total number of votes cast
    total_votes = 0

    # number of candidates who received votes
    candidates = {}

    for row in csvreader:
        # number of votes
        total_votes += 1
        
        # find unique candidates
        if row[2] not in candidates:
            candidates[row[2]] = 0
        if row[2] in candidates:
            candidates[row[2]] += 1

    # percentage of votes each candidate won
    def percent_votes(candidate):
        if candidate in candidates:
            percent = round(((candidates[candidate]/total_votes)*100),3)
            return percent


# print statements


print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------')

for candidate,votes in candidates.items():
    print(candidate + ': ' + str(percent_votes(candidate)) + '% (' + (str(candidates[candidate])) + ')')

print('-------------------------')

winner = max(candidates, key=candidates.get)

print("Winner: " + winner)

print('-------------------------')

# Open the file using "write" mode. Specify the variable to hold the contents

output_path = "Analysis/Financial_Analysis.txt"
with open(output_path, 'w') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(["Election Results"])

    # Write the second row
    csvwriter.writerow(['----------------------------'])

    # input values
    csvwriter.writerow(['Total Votes: ' + str(total_votes)])
    csvwriter.writerow(['----------------------------'])
    for candidate,votes in candidates.items():
        csvwriter.writerow([(candidate + ': ' + str(percent_votes(candidate)) + '% (' + (str(candidates[candidate])) + ')')])
    csvwriter.writerow(["Winner: " + winner])
    csvwriter.writerow(['----------------------------'])
   