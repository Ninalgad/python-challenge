import csv
import os

file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

ballot = dict()
total = 0

with open(file_path, encoding='UTF-8') as f:
    csvreader = csv.reader(f, delimiter=",")
    header = next(csvreader)  # stores the header row

    for (voter_id, county, candidate) in csvreader:
        total += 1

        if candidate in ballot:
            ballot[candidate] += 1
        else:
            ballot[candidate] = 1

# sort candidate names in alphabetical order for output
sorted_candidate = sorted(ballot.keys())
candidate_result_str = ""
for c in sorted_candidate:
    percent = 100 * (ballot[c] / total)
    percent = round(percent, 2)
    candidate_result_str += f"{c} {percent}% ({ballot[c]})\n"

# gets candidate with most votes
winner = max(ballot, key=ballot.get)

# output string
output = f"""Election Results
-------------------------
Total Votes: {total}
-------------------------
{candidate_result_str}-------------------------
Winner: {winner}
-------------------------"""
print(output)

# save to file
output_file = os.path.join('PyPoll', 'analysis', 'output.txt')
with open(output_file, "w") as f:
    f.write(output)
