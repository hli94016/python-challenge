import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('.', 'Resources', 'election_data.csv')


# Define the functions 

def count(voter_ids):
    total = 0.0
    for voter_id in voter_ids:
        total += 1
    return total

with open(election_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    voter_ids = []
    candidates = []
    candidatePollDict = {}
    vote_percentage = []
    for row in csvreader:
        voter_id = str(row[0])
        candidate = str(row[2])
        voter_ids.append(voter_ids)
        candidates.append(candidate)
    Total_vote = int(count(voter_ids))     

    for candidate in candidates:
        if candidate not in candidatePollDict:
            candidatePollDict[candidate] = {'vote': 1, 'percentage': float(1/Total_vote)}
        else:
            vote = candidatePollDict[candidate]['vote']
            candidatePollDict[candidate] = {'vote': vote + 1, 'percentage': float((vote + 1) / Total_vote)}
 
    # print(candidatePollDict)
    print('Election Results\n--------------------------')
    print(f"Total Votes: {Total_vote}\n--------------------")
    maxVote = 0
    winner = ''
    for candidate in candidatePollDict.keys():
        content = candidatePollDict[candidate]
        print(f"{candidate}: {round(content['percentage'] * 100, 3)}% ({content['vote']})")
        if content['vote'] > maxVote:
            maxVote = content['vote']
            winner = candidate
    print('------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

   
    


