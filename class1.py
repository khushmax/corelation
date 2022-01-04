import csv
import numpy as np

def getDataSource(data_path):
    marksInPercentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x":marksInPercentage , "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between percentage and days present is :",correlation[0,1])

def setup():
    data_path = "./data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()




    
    