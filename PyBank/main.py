#create path to file
#%%
import os
import csv

data_path = os.path.join('Resources', 'budget_data.csv')

#open data
with open(data_path) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=',')

    for row in budgetdata:
        print(row)

