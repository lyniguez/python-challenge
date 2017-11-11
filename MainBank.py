import os
import csv

budgetCSV = os.path.join('PyBank','raw_data','budget_data_1.csv')

totalmonths = 0
totalrev= 0
maxincreaserev = []
maxincreasedate = []
maxdecreaserev = []
maxdecreasedate = []
prevrev = 0
totalchange = 0

    
with open(budgetCSV, "r") as budget:
    csvreader = csv.DictReader(budget)
    count = 1
    for row in csvreader:
        totalmonths += 1
        totalrev = totalrev + int(row["Revenue"])
        changerev = int(row["Revenue"])- prevrev
        totalchange = totalchange + changerev
        maxincreaserev = int(row["Revenue"])
        maxdecreaserev = int(row["Revenue"])
        
        if prevrev != 0:
            if changerev > maxincreaserev:
                maxincreasedate = row["Date"]
                maxincreaserev = int(row["Revenue"])
            elif changerev < maxdecreaserev:
                maxdecreasedate = row["Date"]
                maxdecreaserev = int(row["Revenue"])
        else:
            prevrev = int(row["Revenue"])
        
        prevrev = int(row["Revenue"])
        count +=1
        averagechange = totalchange / count
    




print("Financial Analysis")
print("------------------------")
print("Total Months: "+ str(totalmonths))
print("Total Revenue: "+ str(totalrev))

print("Greatest Increase in Revenue: "+ str(maxincreasedate)+ " "+str(maxincreaserev))
print("Greatest Decrease in Revenue: "+ str(maxdecreasedate)+ " "+str(maxdecreaserev))
print("Average Revenue Change "+ str(changerev))


