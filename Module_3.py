import csv

profit_loss_diff = []

for i in range(len(profit_loss) - 1):
    difference = (profit_loss[i + 1] - profit_loss[i])
    profit_loss_diff.append(difference)

for row in csvreader:
    row[0],row[1]
    date.append(row[0])
    profit_loss.append(int(row[1]))

def sumcolumn(profit_loss):
    total = 0
    for i in profit_loss:
        total += i
    return total

def average(profit_loss_diff):
    length = len(profit_loss)
    total = sumcolumn(profit_loss)
    return round(total/length, 2)
    


print("Greatest Increase in Profits: $" + str(max(profit_loss_diff)))
print("Greatest Decrease in Profits: $" + str(min(profit_loss_diff)))
