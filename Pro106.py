import csv
import plotly.express as px
import numpy as np 

def getDataSource(data_path):
    temp=[]
    iceCream_sale =[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temp.append(float(row["Temperature"]))
            iceCream_sale.append(float(row["Ice-cream Sales( â‚¹ )"]))
        return{"x":temp,"y":iceCream_sale }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation: ", correlation[0,1])

def main():
    data_path = "IceTemp.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

main()

