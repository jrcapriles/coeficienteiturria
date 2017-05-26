#!/usr/bin/python
# coding: utf-8

import json
import matplotlib.pyplot as plt
from datetime import datetime

team_names = {"1" : "Tibu de la gente",
              "2" : "[b.A] El Chacho",
              "3" : "Arios Rompebolas",
              "4" : "Cydonia Knights BBC",
              "5" : "Dr Respect & Mr Rage",
              "6" : "JPs Logrono Rockies",
              "7" : "Las Taras de Doug",
              "8" : "Los Grandes",
              "9" : "OGM_Gansa",
              "10": "Red Sox Pohio",
              "11": "TheMBullets",
              "12": "Nordics" }

plot_linestyles =  {"1" : "",
                    "2" : "",
                    "3" : "",
                    "4" : "",
                    "5" : "",
                    "6" : "",
                    "7" : "",
                    "8" : "--",
                    "9" : "--",
                    "10": "--",
                    "11": "--",
                    "12": "--" }


plot_colors =  {"1" : "b",
                "2" : "g",
                "3" : "r",
                "4" : "c",
                "5" : "m",
                "6" : "y",
                "7" : "k",
                "8" : "b",
                "9" : "g",
                "10": "r",
                "11": "c",
                "12": "k" }


json_dic = open("data/ci_accum_by_date.json", "r")
data = json.load(json_dic)


for i in data:
    print i


print "Data from my team"

date = []
teams = { "1":[0],
          "2":[0],
          "3":[0],
          "4":[0],
          "5":[0],
          "6":[0],
          "7":[0],
          "8":[0],
          "9":[0],
         "10":[0],
         "11":[0],
         "12":[0]}

for i in data:
   
    date.append(datetime.strptime(i["date"],"%Y-%m-%d"))
    for key in team_names:
        if key in i:
            teams[key].append(teams[key][-1]+i[key])
        else:
            teams[key].append(teams[key][-1])

print date
print teams 

fig = plt.figure(1)
ax = fig.add_subplot(111)

#fig, ax = plt.subplots()

for key in team_names:
    print team_names[key]
    ax.plot(date, teams[key][1:], plot_linestyles[key], color=plot_colors[key], label=team_names[key].decode('unicode-escape'), markersize=10)

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1,0.5))
ax.grid('on')

fig.savefig('img/ci_figure.jpg', bbox_extra_artists=(lgd,), bbox_inches='tight')


#legend = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5)) #(loc='upper center', shadow=True)
#frame = legend.get_frame()
#frame.set_facecolor('0.80')

# Set the fontsize
#for label in legend.get_texts():
#    label.set_fontsize('large')
#    for label in legend.get_lines():
#        label.set_linewidth(1.5)  # the legend line width
#        plt.show()
plt.show()
