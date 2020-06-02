#Importing csv library to read csv file , iterate data and write to CSV file
import csv
#importing os library to use the relative path of file 
import os
#set relative path of file in a a variable
csv_path=os.path.join("Resources","election_data.csv")

#Variable to set total number of votes
total_votes=0

#Dictionary to store unique list of candidates and their vote count
data_dict_candidate={}

#Open file in encoding:utf-8 and create a varible to hold content of file and start reading data in variable by row for processing
with open(csv_path,encoding="utf-8") as csv_file:
    
    #Create a variable that holds content of the file delimited by ","
    csv_reader=csv.reader(csv_file, delimiter=',')

    #Pass value of header row in csv_header list
    csv_header=next(csv_reader)

    #print header
    #print(csv_header)

    # Read each row of data after the header;
    # Add new candidate with vote as 1 if candidate is not found in list 
    # Add 1 to the value of the candidate if candidate is found
    for row in csv_reader:
       #Dictionary value to store each row of data as key:value pair for VoterId, County, Candidate
        total_votes+=1
        if row[2] in data_dict_candidate:
            data_dict_candidate[row[2]]= int(data_dict_candidate[row[2]])+1
        else:
            data_dict_candidate[row[2]]=1

#Print the result

print(f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------""")

# print candidates and their number of votes and percentage=number of votes/total votes
for key,value in data_dict_candidate.items():
    print (f"{key}: {(value/total_votes):.3%} ({value})")

print(f" -------------------------")

#print Winner using max and .get function
print(f"Winner : {max(data_dict_candidate,key=data_dict_candidate.get)}")
print(f" -------------------------")

#set path and name of file in which data would be written back
output_path=os.path.join("Analysis","election_summary.txt")


with open(output_path, 'w') as file_output:

    #Write sheet header and Total votes
    file_output.write(f"Election Results\n")
    file_output.write(f"------------------------------\n")
    file_output.write(f"Total Votes: {total_votes}\n")
    file_output.write(f"------------------------------\n")

    for key,value in data_dict_candidate.items():
        file_output.write(f"{key}: {(value/total_votes):.3%} ({value})\n")

    file_output.write("---------------------------\n")

    #output Winner using max and .get function
    file_output.write(f"Winner : {max(data_dict_candidate,key=data_dict_candidate.get)}\n")
    file_output.write("------------------------")
