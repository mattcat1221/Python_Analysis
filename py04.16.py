import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")



    budget_data.csvreader = csv.call (csvfile budgegt_data, delimiter=",") # type: ignore
    budget_data = next()
    print(f"Header: {csv_header}") # type: ignore

    # find net amount of profit and loss

    P = []
    months = [] 
    
    int; 


          #read through each row of data after header in}

    for rows in #csvreader = "in:("budget_data:"budget_data 3"")
        P.append(int(rows[1]))
        months.append(rows[0])


    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

    revenue_average = sum(revenue_change) / len(revenue_change)

    total_months = len(months)

    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)

    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(P)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))#ignore