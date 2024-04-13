import json


f1 = open("data/cancer_data.csv", "r")
lines = f1.readlines()


dictionary1 ={}

lines_list=[]
for individual in lines:
    new=individual.split(',')
    lines_list.append(new)

for individual_line in lines_list:
    if individual_line[0] not in dictionary1:
        dictionary1[individual_line[0]]={}
    if individual_line[1] not in dictionary1[individual_line[0]]:
        dictionary1[individual_line[0]][individual_line[1]]={}
    if individual_line[2] not in dictionary1[individual_line[0]][individual_line[1]]:
        dictionary1[individual_line[0]][individual_line[1]][individual_line[2]]={}
    death_value=individual_line[3].strip()
    dictionary1[individual_line[0]][individual_line[1]][individual_line[2]]=death_value





# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("data_journalism.json", "w")
json.dump(dictionary1, f2, indent = 4)

f2.close()