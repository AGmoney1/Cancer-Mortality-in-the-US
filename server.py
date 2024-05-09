from flask import Flask, request
from flask import render_template
import json
import math


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f1 = open("data/cancer_data.json", "r")
    data1 = json.load(f1)
    f1.close()
    f2 = open("data/year_cancer_data.json", "r")
    data2 = json.load(f2)
    f2.close()
    cancer_types=list(data1.keys())
    cancers_length=len(cancer_types)-1
    all_years = sorted(list(data1[cancer_types[0]].keys()))
    years_length=len(all_years)-1
    states=list(data1[cancer_types[0]][all_years[0]].keys())
    states_length=len(states)-1
    other_data=[]
    year_sum=0
    for yearINT in range(years_length+1):
        """data_list.append((data2[cancer_types[2]][all_years[yearINT]]))"""
        for i in range (1,5):
            year_sum+=(data2[cancer_types[i]][all_years[yearINT]])
            other_value=data2[cancer_types[0]][all_years[yearINT]]-year_sum
        other_data.append(other_value)
        year_sum=0
    return render_template('macro.html',data1=data1, data2=data2, cancer_types=cancer_types, all_years=all_years,states_length=states_length, years_length=years_length, states=states,other_data=other_data)

@app.route('/year/<int:year>', methods=['GET'])
def year(year):
    f1 = open("data/cancer_data.json", "r")
    data1 = json.load(f1)
    f1.close()
    f2 = open("data/year_cancer_data.json", "r")
    data2 = json.load(f2)
    f2.close()
    f3 = open("data/state_population.json", "r")
    data3 = json.load(f3)
    f3.close()
    f4 = open("data/state_deaths.json", "r")
    data4 = json.load(f4)
    f4.close()
    selected_year = request.args.get('year')
    str_year=str(year)
    cancer_types=list(data2.keys())
    all_years = sorted(list(data2[cancer_types[0]].keys()))
    years_length=len(all_years)-1
    all_years2 = sorted(list(data3.keys()))
    states2=list(data3[all_years2[0]].keys())
    all_years3 = sorted(list(data4.keys()))
    states3=list(data4[all_years3[0]].keys())
    national_pop=0
    nat_deaths=0
    nat_death_by_can=data2[cancer_types[0]][str_year]
    for state in states2:
        national_pop+=data3[str_year][state]
    for state in states3:
        nat_deaths+=data4[str_year][state]
    print((nat_death_by_can/nat_deaths)*100)
    can_deaths_percent=(round((nat_death_by_can/nat_deaths)*10000))/100
    return render_template('year.html', data1=data1,data2=data2, data3=data3, data4=data4, year=year, str_year=str_year, cancer_types=cancer_types,all_years=all_years,years_length=years_length, states2=states2, national_pop=national_pop, nat_deaths=nat_deaths, nat_death_by_can=nat_death_by_can,can_deaths_percent=can_deaths_percent)

@app.route('/about')
def state():
    f1 = open("data/cancer_data.json", "r")
    data1 = json.load(f1)
    f1.close()
    cancer_types=list(data1.keys())
    all_years = sorted(list(data1[cancer_types[0]].keys()))
    return render_template('about.html', all_years=all_years)

app.run(debug=True)



"""function showValue(path, year, data3, data1, data4, cancer_types) {
        const stateClass = path.childNodes[1].innerHTML
        const value1 = data1[cancer_types[0]][year][stateClass];
        const value2 = data4[year][stateClass];
        const value3 = data3[year][stateClass];
        document.getElementById("value1").innerHTML = `Data 1: ${value1}`;
        document.getElementById("value2").innerHTML = `Data 2: ${value2}`;
        document.getElementById("value3").innerHTML = `Data 3: ${value3}`;
        document.querySelectorAll(".value").forEach(el => el.style.display = 'block');
    }"""

