import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Define the functions 

def count(months):
    total = 0.0
    for month in months:
        total += 1
    return total

def sum(profits):
    sum_profit = 0.0
    for profit in profits:
        sum_profit += profit
    return  sum_profit

def difference(profit, prev_profit):
    change = profit - prev_profit
    return change

def max(changes):
    max_change = 0.0
    for change in changes:
        if change > max_change:
            max_change = change
        else:
            max_change = max_change
    return max_change 

def min(changes):
    min_change = 0.0
    for change in changes:
        if change < min_change:
            min_change = change
        else:
            min_change = min_change
    return min_change 

def financial_analyzer(months, profits):

    Total_profits = int(sum(profits))
    Total_change = 0.0
    prev_profit = 0.0
    changes = []
    for profit in profits:
        row_change = difference(profit, prev_profit)
        changes.append(row_change)
        prev_profit = profit

    changes = changes[1:]
    Total_month = int(count(months))
    Total_change = sum(changes)
    Average_change = round(Total_change / (count(profits) - 1), 2)
    Max_change = max(changes)
    Min_change = min(changes)


    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {str(Total_month)}")
    print(f"Total: ${str(Total_profits)}")
    print(f"Average Change: ${str(Average_change)}")

    idx = 1
    for change in changes:
        if change == Max_change:
            print(f"Greatest Increase in Profits: {months[idx]} (${Max_change})")
        elif change == Min_change:
            print(f"Greatest Decrease in Profits: {months[idx]} (${Min_change})")
        idx += 1


with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    profits = []
    months = []
    for row in csvreader:
        month_str = str(row[0])
        profit = float(row[1])
        months.append(month_str)
        profits.append(profit)

    financial_analyzer(months, profits)



    
