# Import modules
import os 
import csv

# Variables
total_months = 0
net_total = 0
monthly_change = []
month_count = []
max_increase = 0
max_month_increase = 0
max_decrease = 0
max_month_decrease = 0

# Create path and open
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    row = next(csvreader)
    
    previous_row = int(row[1])
    total_months += 1  
    net_total += int(row[1])
    max_increase = int(row[1])
    max_month_increase = row[0]


    for row in csvreader:

        # The total number of months included in the dataset
        total_months += 1 

        # The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        profit_change = int(row[1]) - previous_row
        monthly_change.append(profit_change)
        previous_row = int(row[1])
        month_count.append(row[0])


        # The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > max_increase:
            max_increase = int(row[1])
            max_month_increase = row[0]

        # The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < max_increase:
            max_decrease = int(row[1])
            max_month_decrease = row[0]

        average_change = sum(monthly_change) / len(monthly_change)
        highest = max(monthly_change)
        lowest = min(monthly_change)

# Print analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {max_month_increase}, (${highest})")
print(f"Greatest Decrease in Profits:, {max_month_decrease}, (${lowest})")

# Create path for new file
output_file = os.path.join('analysis.txt')

# Export to text file with results
with open(output_file, 'w',) as txtfile:
   txtfile.write(f"Financial Analysis\n")
   txtfile.write(f"----------------------------\n")
   txtfile.write(f"Total Months: {total_months}\n")
   txtfile.write(f"Total: ${net_total}\n")
   txtfile.write(f"Average Change: ${average_change:.2f}\n")
   txtfile.write(f"Greatest Increase in Profits:, {max_month_increase}, (${highest})\n")
   txtfile.write(f"Greatest Decrease in Profits:, {max_month_decrease}, (${lowest})\n")
