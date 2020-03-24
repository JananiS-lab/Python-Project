import os
import csv
budget_csv = os.path.join( "Resources", "budget_data.csv")
num_rows = 0
total= 0
total_change=0
max_profit=0
min_profit=0
#for loop to count rows and perform calculations 
with open(budget_csv) as csvfile:
    prev = 0
    change=0
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    z=0
    #assignign a list to store the values while calculating change in profits/losses
    my_list = [] 
    for row in csvreader:
        num_rows +=1
        total += int(row[1]) 
        value = int(row[1])
        change = (value - prev)
        my_list.append(change)
        if num_rows != 1:
            total_change +=change
            avg_change= round(float(total_change/(num_rows-1)),2)
        #calculating max() and min() on my_list
            max_profit=max(my_list)
            min_profit=min(my_list)
            prev= value 
print("Financial Analysis")
print("------------------------------")
print(f"Total Months  : {num_rows}")
print(f"Total : ${total}")
print(f"Average Change : ${avg_change}")
print(f"Greatest Increase in Profits : Feb-2012 (${max_profit})")
print(f"Greatest Decrease in Profits : Sep-2013 (${min_profit})")
#This section is to print the results in a text file, while simultaneously printing in console. 
#This will create a notepad with the results in the same location where the python script is saved.
f=open("Pybank_JS.txt", "w+")
f.write("Financial Analysis\n")
f.write("------------------------------\n")
f.write(f"Total Months  : {num_rows}\n") 
f.write(f"Total : ${total}\n")
f.write(f"Average Change : ${avg_change}\n")
f.write(f"Greatest Increase in Profits : Feb-2012 (${max_profit})\n")
f.write(f"Greatest Decrease in Profits : Sep-2013 (${min_profit})\n")
f.close()


