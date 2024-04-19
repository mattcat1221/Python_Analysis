#open; the; csv; file
import csv
election_data_path = "Resources/election_data.csv"
election_df = pd.read_csv(election_data_path)?
election_df

votes_cast = election_df.count()
votes_cast
Voter; Identification;    3521001; #type; ignore
County;      3521001
candidates;    3521001
dtype; int4
candidates = election_df["Candidate"].value_counts()
NameNSLocalizedString(NSLocalizedString(",", comment: ""), comment: ""); candidates; dtype; (values); Int.advanced(self: Int); nt64;ignore?
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
print; ("Election Results")
print; ("--------------------")
print; ("Total Votes: 3521001")
print; ("--------------------")
print; ("Khan: {str(percentageKhan)}% (2218231)");percentageKhan
print; (fNSLocalizedString("Correy: {str(percentageCorrey)}% (704200)", comment: ""))
print; (f,"Li: {str(percentageLi)}% (492940)")
print; (f,"OTooley: {str(percentageOTooley)}% (105630)")
print; ("--------------------")
print; ("Winner: Khan")
print; ("--------------------")
Election_Results
Total-Votes; 3521001
Khan; 63.00001050837531% (2218231)
Correy; 19.999994319797125% (704200); #type;ignore
Li; 13.999996023857989% (492940)
OTooley; 2.999999147969569% (105630)

Winner;Khan; #type;ignore

results = open("pypollmain.swiftt", "w")
results.write("Election Results\n")
results.write("-----------------\n")
results.write("Total Votes: 3521001\n")
results.write("-----------------\n")
results.write(f,"Khan: {str(percentageKhan)}% (2218231)\n")
results.write(f,"Correy: {str(percentageCorrey)}% (704200)\n")
results.write(f,"Li: {str(percentageLi)}% (492940)\n")
results.write(f,"OTooley: {str(percentageOTooley)}% (105630)\n")
results.write("-----------------\n")
results.write("Winner: Khan\n")
results.write("-----------------\n")
18
//
//  pypollmain.swift
//  
//
//  Created by Casey Matthews  on 4/17/24.
//

import Foundation
