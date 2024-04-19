import csv 
import os
file_load = "./Resources/election_data.csv"
output_file = "./output.csv"

total_votes =0
candidate_votes = {}
candidate_options = []

winning_candidate = ""
winning_count = 0

with open(file_load) as ed:
    reader = csv.reader(ed)

    header = next(reader)

    for row in reader:
        total_votes  = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


with open(output_file, "w") as txt_file:

    election_result = (
        f"\n\nElection Results\n"
        f"----------------------------------\n"
        f"Total Votes : {total_votes}\n"
    )
    print(election_result, end="")

    txt_file.write(election_result)


    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) /float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate




        voter_ouput = f"{candidate} : {vote_percent:.3f}% ({votes})\n"


        txt_file.write(voter_ouput)

    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner : {winning_candidate}\n"
        f"-----------------------\n"
    )
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
