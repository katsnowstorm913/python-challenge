#create path to file
import os
import csv
import sys

data_path = os.path.join('Resources', 'budget_data.csv')

#variables
months = 0
total_profits = 0
big_prof = ["month", "0"]
big_loss = ['Month', "0"]
first = True
mon_start = 0
mon_end = 0
prof_changes = []
change_months = []

#open data
with open(data_path) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=',')
    #skip header
    csv_head = next(csvfile)
     
     #count months
    for row in budgetdata:
        months += 1
        #total profits/losses
        total_profits += float(row[1])
       
        #find change in profits. skip first month
        if first == True:
            mon_start = float(row[1])
            first = False
        else:
            mon_end = float(row[1])
            prof_changes.append(mon_end - mon_start)
            change_months.append(row[0])
            mon_start = mon_end
    
    #calculate average change in profits
    avrg_change = sum(prof_changes) / len(prof_changes)

    #find greatest profit and loss
    for x in range(len(prof_changes)):
        if prof_changes[x] > int(big_prof[1]):
             big_prof[0] = change_months[x]
             big_prof[1] = prof_changes[x]
        if prof_changes[x] < int(big_loss[1]):
            big_loss[0] = change_months[x]
            big_loss[1] = prof_changes[x]

#output results to text file and print to terminal
outpath = os.path.join('analysis','financial_analysis.txt')
with open(outpath, 'w') as outF:
    outF.write("Financial Analysis\n")
    print("Financial Analysis")
    outF.write("-------------\n")
    print("-------------")
    outF.write(f"Total Months: {months}\n")
    print(f"Total Months: {months}")
    outF.write(f"Total: ${total_profits}\n")
    print(f"Total: ${total_profits}")
    outF.write(f"Average Change: ${avrg_change}\n")
    print(f"Average Change: ${avrg_change}")
    outF.write(f"Greatest Increase in Profits: {big_prof[0]} (${big_prof[1]})\n")
    print(f"Greatest Increase in Profits: {big_prof[0]} (${big_prof[1]})")
    outF.write(f"Greatest Decrease in Profits: {big_loss[0]} (${big_loss[1]})\n")
    print(f"Greatest Decrease in Profits: {big_loss[0]} (${big_loss[1]})")

