#!/usr/bin/env python
# coding: utf-8




import csv 
import numpy as np





# making a list from the csv file
vote_csv = "Resources/election_data.csv"

vote_id = []
county = []
candidates = []

with open(vote_csv, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:        
        vote_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])





print(candidates[1]) # test





with open("ElectionResults.txt", "w") as file:
    file.write("Election Results")

file = open("ElectionResults.txt", "a")
file.write("\n---------------------\n")





total = len(vote_id) #getting amount of votes
print(total)
file.write(f"Total Votes: {total}")
file.write("\n---------------------\n")




# list of candidates
def unique(list1):
    unique = set(list1)
    return list(unique)   





cand = unique(candidates) #list of candidates





# finding counts of candidates
def count(lst1, name):
    num = 0
    for i in range(len(lst1)):
        if lst1[i]==name:
            num = num + 1
    print (f"{name} has {num} votes")
    return num
                





# finding the number of votes
a = count(candidates, cand[0])
b = count(candidates, cand[1])
c = count(candidates, cand[2])





print(a) #test





# Function to find percent of votes
def percent(lst1, total, lst2):
    lst3 = []
    for i in range(len(lst1)):
        per = round(lst1[i]/total*100,3)
        lst3.append(per)
        print (f"{lst2[i]} has {per}% of the vote")
    return lst3
        
    
    





vote_counts = [a,b,c]
perc_vote = percent(vote_counts, total, cand)





print(perc_vote) #test





# finding  winner
def winner(lst1,lst2):
    max_per = max(lst1)
    ind = lst1.index(max_per)
    win = lst2[ind]
    print(f"{win} is the winner with {max_per}% votes.")
    return win
        




win = winner(perc_vote, cand)





for i in range(0,3):
    print(f"{cand[i]}: {perc_vote[i]}% ({vote_counts[i]})\n")
    file.write(f"{cand[i]}: {perc_vote[i]}% ({vote_counts[i]})\n")





file.write("\n---------------------\n")
file.write(f"Winner: {win}")
file.write("\n---------------------\n")
file.close()

