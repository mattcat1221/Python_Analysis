#open the csv file
import csv
from functools import total_ordering
from turtle import pd
from typing import Counter 
election_data_path = "Resources/election_data.csv"
election_df = pd.read_csv(election_data_path)
election_df

votes_cast = election_df.count()
votes_cast
Voter Identification;    3521001 # type: ignore
Counter;      3521001
candidates;    3521001 # type: ignore
dtype: int
candidates = election_df['Candidate'].value_counts()
candidates
Name: candidates, dtype: int64 # type: ignore
percentageKhan = (2218231 / 3521001) * 100
percentageKhan
63.00001050837531
percentageCorrey = (704200 / 3521001) * 100
percentageCorrey
19.999994319797125
percentageLi = (492940 / 3521001) * 100
percentageLi
13.999996023857989
percentageOTooley = (105630 / 3521001) * 100
percentageOTooley
2.999999147969569
print('Election Results')
print('--------------------')
print('Total Votes: 3521001')
print('--------------------')
print(f'Khan: {str(percentageKhan)}% (2218231)')
print(f'Correy: {str(percentageCorrey)}% (704200)')
print(f'Li: {str(percentageLi)}% (492940)')
print(f'OTooley: {str(percentageOTooley)}% (105630)')
print('--------------------')
print('Winner: Khan')
print('--------------------')
Election_Results # type: ignore
total_ordering-Votes; 3521001 # type: ignore
Khan: 63.00001050837531% (2218231) # type: ignore
Correy: 19.999994319797125% (704200) # type: ignore
Li: 13.999996023857989% (492940) # type: ignore
OTooley: 2.999999147969569% (105630) # type: ignore

Winner: Khan # type: ignore

results = open('analysis/results.txt', 'w')
results.write('Election Results\n')
results.write('-----------------\n')
results.write('Total Votes: 3521001\n')
results.write('-----------------\n')
results.write(f'Khan: {str(percentageKhan)}% (2218231)\n')
results.write(f'Correy: {str(percentageCorrey)}% (704200)\n')
results.write(f'Li: {str(percentageLi)}% (492940)\n')
results.write(f'OTooley: {str(percentageOTooley)}% (105630)\n')
results.write('-----------------\n')
results.write('Winner: Khan\n')
results.write('-----------------\n')
18
