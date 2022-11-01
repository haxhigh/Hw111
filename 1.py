import csv
from dataclasses import dataclass
import statistics as st
import plotly.figure_factory as pf
import pandas as pd
import random

df = pd.read_csv("C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/Hw111/medium_data.csv")
df2 = pd.read_csv("C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/Hw111/savings2 copy.csv")

file = df["reading_time"].tolist()
file2 = df["reading_time"].tolist()

samplingMean = st.mean(file2)
print(samplingMean)

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(file) - 1)
        value = file[random_index]
        dataSet.append(value)
    mean = st.mean(dataSet)
    return mean

def show_fig(meanList):
    df = meanList
    mean = st.mean(df)
    fig = pf.create_distplot([df],["reading time"])
    fig.show()

def setUp():
    meanList = []
    for i in range(0,100):
        meanSet = random_set_of_mean(30)
        meanList.append(meanSet)
    #show_fig(meanList)
    mean = st.mean(meanList)
    stdev = st.stdev(file)
    print("The mean is: " + str(mean))
    if(mean > samplingMean):
        zScore = (mean - samplingMean) / stdev
        print("The zScore is: "+str(zScore))
setUp()