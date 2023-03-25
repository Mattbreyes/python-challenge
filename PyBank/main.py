#pybank script
import os
import csv

file_path = "Resources/budget_data.csv"

with open(file_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # number of months included in dataset is equal to number of rows
    months = 0

    # net total amount of pofit/losses over the entire period
    profit_losses = []

    totalrows = []

    for row in csvreader:
        # number of months
        months += 1
        # net total 
        profit_losses.append(int(row[1]))
        # store all rows in list
        totalrows.append(row)
    
    # print(months)
    
    net_total = sum(profit_losses)
    # print(net_total)

    #changes in profit/losses and the average
    profit_loss_diff = []

    for i in range(len(profit_losses) - 1):
        difference = (profit_losses[i + 1] - profit_losses[i])
        profit_loss_diff.append(difference)

    avg_change = round(sum(profit_loss_diff)/(len(profit_loss_diff)),2)
    
    # print(avg_change)
    

    # greatest increase in profits
    great_increase = max(profit_loss_diff)
    
    # find index for month of greatest increase
    greatest_increase_index = profit_loss_diff.index(great_increase)
    greatest_increase_month = totalrows[greatest_increase_index + 1][0]
    # print(greatest_increase_month)
    

    # greatest decrease
    great_decrease = min(profit_loss_diff)
    # print(great_decrease)

    # find index for month of greatest decrease
    greatest_increase_index = profit_loss_diff.index(great_decrease)
    greatest_decrease_month = totalrows[greatest_increase_index + 1][0]
    # print(greatest_decrease_month)


print('Total Months: ' + str(months))
print('Total : $' + str(net_total))
print('Average Change: $' + str(avg_change))
print('Greatest Increase in Profits: ' + greatest_increase_month + " $" + str(great_increase))
print('Greatest Increase in Profits: ' + greatest_decrease_month + " $" + str(great_decrease))

output_path = "../output/new.csv"

# Open the file using "write" mode. Specify the variable to hold the contents

output_path = "Analysis/Financial_Analysis.txt"
with open(output_path, 'w') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(["Financial Analysis"])

    # Write the second row
    csvwriter.writerow(['----------------------------'])

    # input values
    csvwriter.writerow(['Total Months: ' + str(months)])
    csvwriter.writerow(['Total : $' + str(net_total)])
    csvwriter.writerow(['Average Change: $' + str(avg_change)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + greatest_increase_month + " $" + str(great_increase)])
    csvwriter.writerow(['Greatest Increase in Profits: ' + greatest_decrease_month + " $" + str(great_decrease)])
   