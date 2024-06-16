import csv

data = csv.DictReader(open("Resources/budget_data.csv"))
my_report = open("analysis/budget_report.txt","w") 

months = 0 
total = 0
total_ch = 0
pre_rev = 0
ginc = 0
gdec = 0 

for row in data:
    months+=1

    Rev = int(row["Profit/Losses"])
    total += Rev 

    ch = Rev - pre_rev

    if pre_rev == 0:
        ch = 0

    total_ch += ch

    pre_rev = Rev
    
    if ch > ginc:
        ginc = ch
        gimon = row["Date"]


    if ch < gdec:
        gdec = ch
        gdmon = row["Date"]
    

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {gimon} (${ginc:,})
Greatest Decrease in Profits: {gdmon} (${gdec:,})
'''

print(output)
my_report.write(output)