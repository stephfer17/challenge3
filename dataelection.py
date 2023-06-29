import csv
import os
#joining the data to the csv files 
# for the os.path.join ("..","Resources,"election_data.csv) it was just an issue on my computuer
election_data = os.path.join("election_data.csv")
# opening the csv file
with open (election_data) as csvfile:
    election_reader = csv.reader (csvfile,delimiter= ",")
    header = next (election_reader)
#place to hold the info cretate a dictonary 
    votes = []
    candidatename={'Charles Casper Stockham':0,"Diana DeGette":0,"Raymon Anthony Doane":0}
# the loop to read through everything
    for rows in election_reader :
# place for votes 
        votes.append (rows[0])
# maybe a if statement for votes and numbers ask about this AskBSC helped 
       # if candidatename[rows[2]]:
        candidatename[rows[2]]+=1
#else:
            #candidatename[rows[2]] = 1
#For the percentages
percentagechar = round(candidatename["Charles Casper Stockham"]/len(votes)*100,2)
percentagedia = round(candidatename ["Diana DeGette"]/len(votes)*100,2)
percentageray = round(candidatename["Raymon Anthony Doane"]/len(votes)*100,2)
winner = max(zip(candidatename.values(),candidatename.keys()))

# print out winners 
print("Election results ")
print (f"total votes are {len(votes)}")
print (".............................")
print (f'Charles Casper,{(percentagechar)}% {candidatename["Charles Casper Stockham"]}')
print (f"Diana DeGette, {percentagedia}% {candidatename['Diana DeGette']}")
print (f'Raymon Anthony Doane,{percentageray}% {candidatename["Raymon Anthony Doane"]}')
print (f"winner is with {winner} ")
#Ask BSC helped me to fill in the path 
electionresult = (f"Election results " , f"total votes are {len(votes)}",".............................")
printcan = (f'Charles Casper,{(percentagechar)}% {candidatename["Charles Casper Stockham"]}' , f"Diana DeGette, {percentagedia}% {candidatename['Diana DeGette']}" ,f'Raymon Anthony Doane,{percentageray}% {candidatename["Raymon Anthony Doane"]}')
winnerelect= (f'winner is with {winner} ')
summary =(electionresult,printcan,winnerelect)
textelection = os.path.join ("Pypoll_output.txt")
with open (textelection,"w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(summary)