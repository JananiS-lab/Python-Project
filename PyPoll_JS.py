import os
import csv
num_rows= 0
Khan_wins=0
Li_wins=0
Correy_wins=0
Tooley_wins=0
Khan_count =0
Li_count=0
Correy_count=0
Tooley_count=0
winner=0
poll_csv=os.path.join("Resources", "election_data.csv")
# forloop to count the total number of voters
with open(poll_csv) as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for  row in csvreader: 
        num_rows +=1
    #this section uses if statement to count the number of votes received my each candidate.
        if row[2] == 'Khan' : 
            Khan_count += 1
        elif row[2] == 'Li' :
            Li_count += 1
        elif row[2] == 'Correy' :
            Correy_count += 1
        else:
            Tooley_count += 1
    #this section is to calculate the percentage of wins for each candidate.
        Khan_wins= round((Khan_count/num_rows) * 100, 2)
        Li_wins=round((Li_count/num_rows)*100, 2)
        Correy_wins=round((Correy_count/num_rows)*100, 2)
        Tooley_wins=round((Tooley_count/num_rows)*100, 2)
        winner=max(Khan_wins, Li_wins, Correy_wins, Tooley_wins)
    #this section uses if statement to print the name of hte candidate who has the highest percentag of votes
        if winner == Khan_wins:
            winner_name= "Khan"
        elif winner == Li_wins:
            winner_name = "Li"
        elif winner == Correy_wins:
            winner_name ="Correy"
        else:
            winner_name = "O'Tooley"
print(f"Election Results")
print("-------------------------------")
print(f"Total votes : {num_rows}")
print("-------------------------------")
print(f"Khan : {Khan_wins}% ({Khan_count})")
print(f"Correy : {Correy_wins}% ({Correy_count})")
print(f"Li : {Li_wins}% ({Li_count})")
print(f"O'Tooley : {Tooley_wins}% ({Tooley_count})")
print("-------------------------------")
print(f"Winner : {winner_name}")  
print("-------------------------------")
#This section is to print the results in a text file, while simultaneously printing in console.
#This will create a notepad with the results in the same location where the python script is saved.
f=open("Pybank_JS.txt", "w+")
f=open("PyPoll_JS.txt", "w+")
f.write("Election Results\n")
f.write("------------------------------\n")
f.write(f"Total votes  : {num_rows}\n") 
f.write("------------------------------\n")
f.write(f"Khan : {Khan_wins}% ({Khan_count})\n")
f.write(f"Correy : {Correy_wins}% ({Correy_count})\n")
f.write(f"Li : {Li_wins}% ({Li_count})\n")
f.write(f"O'Tooley : {Tooley_wins}% ({Tooley_count})\n")
f.write("------------------------------\n")
f.write(f"Winner : {winner_name}\n") 
f.write("------------------------------\n")
f.close()




