#!/usr/bin/env python
# coding: utf-8




import csv
import numpy as np





# creating file with new data
with open("FinancialAnalysis.txt", "w") as file:
    file.write("Financial Analysis")

file = open("FinancialAnalysis.txt", "a")
file.write("\n---------------------\n")





# opening csv
budget_csv = "Resources/budget_data.csv"





# create 2d array from csv file
def read(filename, skip_header=True):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        if skip_header:
            next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data





budget_array = read(budget_csv)





# making a 1d array with profits/losses and turning from string to array
budget_values = []
for i in range(len(budget_array)):
    budget_values.append(int(budget_array[i][1]))
#budget_array = np.array(budget_values)
print(budget_values)
    





#count how many items are in array
months = len(budget_array)
print(months)
file.write(f"Total Months: {months}\n")





# finding the total profit
net = np.sum(budget_values)
print(net)
file.write(f"Total: ${net}\n")





# finding the yearly change
def changes(data):
    diff = []   
    for i in range(1, len(data)):
        differences = data[i] - data[i - 1]
        diff.append(differences)
    
    return diff





change = changes(budget_values) # list of monthly changes
ave_change = round(np.mean(change), 2) #average of that list
print(ave_change)
file.write(f"Average Change: ${ave_change}\n")





# finding min and max changes
max_increase = np.max(change)
max_index = change.index(max_increase)
max_decrease = np.min(change)
min_index = change.index(max_decrease)





# finding the date of max/min change dates

max_date = budget_array[max_index+1][0]
print(max_increase)
print(max_date)
min_date = budget_array[min_index+1][0]
print(max_decrease)
print(min_date)





file.write(f"Greatest Increase in Profits: {max_date} (${max_increase})\n")
file.write(f"Greatest Decrease in Profits: {min_date} (${max_decrease})")
file.close()







