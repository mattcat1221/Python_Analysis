import csv
from tkinter.tix import ROW


#data = csv.DictReader(open(Project /Users/cmatthews/Desktop/Data-Analyst/Projects/Pybank/Pybank.xcodeproj)) # type: ignore

months = 0 
total = 0
total_ch = 0
pre_rev = 0

for data in ROW:
    months+=1

    Rev = (["Profit/Losses"])
    int=total = Rev 

    ch = Rev - pre_rev

    if pre_rev == 0:
        ch = 0

    total_ch += ch

    pre_rev = Rev

    

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

print(output)
