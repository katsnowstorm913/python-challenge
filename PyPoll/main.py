#%%
#create path to file
import os
import csv
import sys

data_path = os.path.join('Resources', 'election_data.csv')

#variables
total_votes = 0
candidate_info = {}
candidate = ""
winner = ["", "0"]

#open file
with open(data_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_head = next(csvfile)

    #loop through data
    for row in election_data:
        #count total votes
        total_votes += 1

        #keep track of candidates and their votes
        candidate = row[2]
        if candidate in candidate_info:
            candidate_info[candidate] += 1
        else:
            candidate_info.update({candidate:1})
       
#open file to print results
outpath = os.path.join('analysis','election_results.txt')
with open(outpath, 'w') as outF:
    #print title and total votes
    outF.write("Election Results\n-------------------\n")
    print("Election Results\n-------------------")
    outF.write(f"Total Votes: {total_votes}\n-------------------\n")
    print(f"Total Votes: {total_votes}\n-------------------")
    #calculate percent won for each candidate
    for person in candidate_info:
        percent = candidate_info[person] / total_votes * 100
        #print each candidates results
        outF.write(f"{person}: {percent}% ({candidate_info[person]})\n")
        print(f"{person}: {percent}% ({candidate_info[person]})")
        #find winner
        if candidate_info[person] > int(winner[1]):
            winner[0] = person
            winner[1] = candidate_info[person]
    #print winner
    outF.write(f"-------------------\nWinner: {winner[0]}\n-------------------")
    print(f"-------------------\nWinner: {winner[0]}\n-------------------")
