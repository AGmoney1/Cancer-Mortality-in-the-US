import json


f1 = open("data/cancer_data.csv", "r")
lines = f1.readlines()


f3 = open("data/state_population.csv", "r")
lines2 = f3.readlines()

f5 = open("data/year_cancer_data.csv", "r")
lines3 = f5.readlines()

dictionary1 ={}
dictionary2 ={}
dictionary3 ={}
dictionary4={}


lines_list=[]
for individual in lines:
    new=individual.split(',')
    lines_list.append(new)
lines2_list=[]
for individual in lines2:
    new=individual.split(',')
    lines2_list.append(new)
lines3_list=[]
for individual in lines3:
    new=individual.split(',')
    lines3_list.append(new)


for individual_line in lines_list:
    if individual_line[0] not in dictionary1:
        dictionary1[individual_line[0]]={}
    if individual_line[1] not in dictionary1[individual_line[0]]:
        dictionary1[individual_line[0]][individual_line[1]]={}
    if individual_line[2] not in dictionary1[individual_line[0]][individual_line[1]]:
        dictionary1[individual_line[0]][individual_line[1]][individual_line[2]]={}
    death_value_nospaces=individual_line[3].strip().replace(" ", "")
    death_value=int(death_value_nospaces)
    dictionary1[individual_line[0]][individual_line[1]][individual_line[2]]=death_value

for individual_line in lines2_list:
    if individual_line[0] not in dictionary2:
        dictionary2[individual_line[0]]={}
    if individual_line[0] not in dictionary4:
        dictionary4[individual_line[0]]={}
    if individual_line[1] not in dictionary2[individual_line[0]]:
        dictionary2[individual_line[0]][individual_line[1]]={}
    if individual_line[1] not in dictionary4[individual_line[0]]:
        dictionary4[individual_line[0]][individual_line[1]]={}
    population_value_nospaces=individual_line[2].strip().replace(" ", "")
    population_value=int(population_value_nospaces)
    dictionary2[individual_line[0]][individual_line[1]]=population_value
    print(individual_line)
    death_state_value_nospaces=individual_line[3].strip().replace(" ", "")
    death_state_value=int(death_state_value_nospaces)
    dictionary4[individual_line[0]][individual_line[1]]=death_state_value

for individual_line in lines3_list:
    if individual_line[0] not in dictionary3:
        dictionary3[individual_line[0]]={}
    if individual_line[1] not in dictionary3[individual_line[0]]:
        dictionary3[individual_line[0]][individual_line[1]]={}
    death_value_nospaces=individual_line[2].strip().replace(" ", "")
    death_value=int(death_value_nospaces)
    dictionary3[individual_line[0]][individual_line[1]]=death_value


# Create the dictionary here

f1.close()
f3.close()
f5.close()

#Save the json object to a file
f2 = open("cancer_data.json", "w")
json.dump(dictionary1, f2, indent = 4)
f2.close()

f4 = open("state_population.json", "w")
json.dump(dictionary2, f4, indent = 4)
f4.close()
f7 = open("state_deaths.json", "w")
json.dump(dictionary4, f7, indent = 4)
f7.close()

f6 = open("year_cancer_data.json", "w")
json.dump(dictionary3, f6, indent = 4)
f6.close()