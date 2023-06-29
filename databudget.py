import csv
import os
# joining the data to the csv files spoke to BSC there was an issue find the folders 
# In the os.path.join("..","Resources","budget_data.csv")
budget_data = os.path.join("budget_data.csv")
with open (budget_data,"r") as csvfile: 
    budget_reader =csv.reader(csvfile,delimiter =',')
    header = next (budget_reader)
    # Places to hold the data ask BSC helped me 
    dates =[]
    net_income =[]
    greatest_postive= []
    greatest_decrease = []
#For for looping to read through Thanks to Ask BSC for this 
    for rows in budget_reader:
# place to add dates
        dates.append(rows[0])
# place to add net income for profit change
        net_income.append(int(rows[1]))
# place to hold the greatest increase max of net income 
        greatest_postive =  max(net_income) 
# place to hold the greatest decrease min of net income 
        greatest_decrease = min(net_income)
# the output for the codes
 #printing out the answers to look like the image 
print ('Financial Analysis')
print ("................")
print (f"The total amount of months is {len(dates)}")
print (f"The total profit is $ {sum(net_income)}")
print (f"The average change is $ {round(sum(net_income)/len(dates))}")
print (f"The greatest increase  $ {greatest_postive}")
print (f"The greatest decrese is $ {greatest_decrease}")
#AskBSC helped with making a path for the data 
datasum= ('Financial Analysis' ,"................" ,f"The total amount of months is {len(dates)}")
sumincome= (f"The total profit is $ {sum(net_income)}",f"The average change is $ {round(sum(net_income)/len(dates))}")
sumchange =(f"The greatest increase  $ {greatest_postive}", f"The greatest decrese is $ {greatest_decrease}")
sumbank = (sumincome,sumincome,sumchange)
textbank = os.path.join("Pybank_output.txt")
with open(textbank, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(sumbank)