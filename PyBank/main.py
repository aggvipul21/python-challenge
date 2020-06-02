#Importing csv library to read csv file , iterate data and write to CSV file
import csv
#importing os library to use the relative path of file 
import os
#set relative path of file in a a variable
csv_path=os.path.join("Resources","budget_data.csv")

#variable to store list of months
months=[]

#variable to store list of profit/losses
profit_loss=[]

#variable to store list of change in profit/losses
profit_loss_change=[]

#variable to store count of months
tot_months=0

#variable to store total of profit and loss in the dataset
tot_profit_loss=0

#variable to store average chnage in profit and loss from previous year
avg_profit_loss_change=0.00

#variable to store greatest increase in profit
greatest_inc_profit=0

#variable to store date when greatest increase in profit was registered
greatest_inc_profit_date=""

#variable to store greatest decrease in loss
greatest_dec_loss=0

#variable to store date when greatest decrease in loss was registered
greatest_dec_loss_date=""

#Print the relative path of file
#print(csv_path)

#Open file in encoding:utf-8 and create a varible to hold content of file and start reading data in variable by row for processing
with open(csv_path,encoding="utf-8") as csv_file:
    
    #Create a variable that holds content of the file delimited by ","
    csv_reader=csv.reader(csv_file, delimiter=',')

    #Pass value of header row in csv_header list
    csv_header=next(csv_reader)

    #print header
    #print(csv_header)

    # Read each row of data after the header and append months in months[] list and profit_loss data in profit_loss[] list
    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
    #print(months,profit_loss,profit_loss_change) 

    #Read all values in profit_loss list from index 1 to calculate change in profit/loss from previous value
    #The first value in profit_loss list has not been considered as there is no previous value to compare

    for i in range(1,len(profit_loss)):  
        profit_loss_change.append(int(profit_loss[i]-profit_loss[i-1]))

        #find greatest increase in profit: 
        # Only those values considered for which profit/loss value is postive which would mean a profit
        #and check if value is greater than last stored value for greatest increase in profit
        if(profit_loss_change[i-1]>0 and profit_loss_change[i-1] >greatest_inc_profit):
            
            #set value for greatest_inc_profit to value in profit_loss_change list at index-1 
            # (since index of profit_loss_change list is 1 less than value of i )
            greatest_inc_profit=profit_loss_change[i-1]
            
             #set value for greatest_inc_profit_date to value in month list at that index
            greatest_inc_profit_date=months[i]

        #find greatest decrease in loss: 
        # Only those values considered for which profit/loss value is negative which would mean a loss
        #and check if value is less than last stored value for greatest decrease in profit
        if(profit_loss_change[i-1]<0 and profit_loss_change[i-1]<greatest_dec_loss):
            #set value for greatest_dec_loss to value in profit_loss_change list at index-1 
            # (since index of profit_loss_change list is 1 less than value of i )
            greatest_dec_loss=profit_loss_change[i-1]
            
            #set value for greatest_dec_loss_date to value in month list at that index
            greatest_dec_loss_date=months[i]

#set value for Total months
tot_months=len(months)

#set value for total profit/loss
tot_profit_loss=sum(profit_loss)

#set value for average chnage in profit/loss
avg_profit_loss_change=round((sum(profit_loss_change)/len(profit_loss_change)),2)   

# Print total months, Total Profit/Loss, Average chnage and Greatest Increase in Profites and Greatest decrease in Profits to terminal

print(f"""
  Financial Analysis
  ----------------------------
  Total Months: {tot_months}
  Total: ${tot_profit_loss}
  Average  Change: ${avg_profit_loss_change}
  Greatest Increase in Profits: {greatest_inc_profit_date} (${greatest_inc_profit})
  Greatest Decrease in Profits: {greatest_dec_loss_date} (${greatest_dec_loss})
  """)

#set path and name of file in which data would be written back
output_path=os.path.join("Analysis","budget_summary.csv")

#Print path and name of file
#print(output_path)

with open(output_path, 'w',newline='') as csv_output:

    # Initialize csv.writer
    csv_writer=csv.writer(csv_output, delimiter=',')

    #Write sheet header
    csv_writer.writerow(["Financial Analysis",""])
    csv_writer.writerow(["-----------------------------",''])

    #Write row for Total Months
    csv_writer.writerow(["Total Months",tot_months])
    #Write row for total of Profit/Loss
    csv_writer.writerow(["Total","$"+str(tot_profit_loss)])
    #Write row for average change in profit/loss
    csv_writer.writerow(["Average  Change","$"+str(avg_profit_loss_change)])
    #Write row for greatest increase in profit
    csv_writer.writerow(["Greatest Increase in Profits",greatest_inc_profit_date+" ($"+str(greatest_inc_profit)+")"])
    #Write row for greatest descrease in profit
    csv_writer.writerow(["Greatest Decrease in Profits",greatest_dec_loss_date+" ($"+str(greatest_dec_loss)+")"])
    

