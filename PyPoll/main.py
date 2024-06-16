
import csv

# Load the data

file_load = "Resources/election_data.csv"  
my_report = open("analysis/election_report.txt","w")  
# Initialize variables
total_votes = 0
candidate_votes = {}
candidate_options = []

winning_candidate = ""
winning_count = 0

# Read the election data file
with open(file_load) as ed:
    reader = csv.reader(ed)

    # Skip the header
    header = next(reader)

    # Process each row in the CSV file
    for row in reader:
        # Increment total vote count
        total_votes += 1

        # Get candidate name from the row
        candidate_name = row[2]

        # If the candidate is not in the list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Increment the candidate's vote count
        candidate_votes[candidate_name] += 1
        
        

    output = f'''
Election Results
-------------------------

Total Votes: {total_votes:,}

-------------------------\n\n'''

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Create a summary for each candidate
        output += f"{candidate} : {vote_percent:.3f}% ({votes:,})\n"

    # Create a summary for the winning candidate
    output += (
        f"\n----------------------\n\n"
        f"Winner : {winning_candidate}\n\n"
        f"-----------------------\n"
    )
    print(output)
    my_report.write(output)
