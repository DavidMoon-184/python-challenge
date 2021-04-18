# Import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
total = 0 
khan = 0
correy = 0
li = 0
otooley = 0

# Open file
with open(csvpath,newline="", encoding="utf-8") as elections:

    csvreader = csv.reader(elections,delimiter=",") 
    csvheader = next(csvreader)     

    for row in csvreader: 

        # The total number of votes cast
        total += 1

        # Statement that counts each vote per candidate
        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1

    # The winner of the election based on popular vote.
    winner = max(khan,correy,li,otooley)

    if winner == khan:
        winner_name = "Khan"
    elif winner == correy:
        winner_name = "Correy"
    elif winner == li:
        winner_name = "Li"
    elif winner == otooley:
        winner_name = "O'Tooley"


    # The percentage of votes each candidate won.
    khan_percent = (khan / total) 
    correy_percent = (correy / total) 
    li_percent = (li / total) 
    otooley_percent = (otooley / total) 


# Print analysis
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
print(f"Khan: {khan_percent:.3%} ({khan})")
print(f"Correy: {correy_percent:.3%} ({correy})")
print(f"Li: {li_percent:.3%} ({li})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley})")
print("-------------------------")
print("Winner: " + winner_name)
print("-------------------------")

# Export to text file with results
output_file = os.path.join('election_results.text')
with open(output_file, 'w',) as txtfile:
   txtfile.write(f"Election Results\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Total Votes: {total}\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Khan: {khan_percent:.3%} ({khan})\n")
   txtfile.write(f"Correy: {correy_percent:.3%} ({correy})\n")
   txtfile.write(f"Li: {li_percent:.3%} ({li})")
   txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley})")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Winner: {winner_name}\n")
   txtfile.write(f"----------------------------\n")
