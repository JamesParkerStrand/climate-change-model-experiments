import csv
from sklearn.linear_model import LinearRegression
import numpy as np

years_data = []
avg_temp_data = []
glob_carb_emiss_data = []
ppm_data_data = []

with open("C:/Users/Parke/Desktop/extra credit geology/Temperature-CO2-data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # print("Column names:", reader.fieldnames) # debugging of dataset
    for row in reader:
        yearData = row['ï»¿the-year']
        avgTempData = row['Annual-Average-Temperature-(Celsius)']
        globcarbemiss = row['Global-carbon-emissions-(billion tonnes of CO2)']
        ppmdata = row['Co2-concentration (ppm)']
        if yearData != '':
            years_data.append(int(yearData))
            avg_temp_data.append(float(avgTempData))
            glob_carb_emiss_data.append(float(globcarbemiss))
            ppm_data_data.append(float(ppmdata))

##answers question 2 on climate model activity
model = LinearRegression()
model.fit(np.asarray(years_data).reshape(-1,1), ppm_data_data)

rate = model.coef_[0]

print(f"Question 2 Rate: {rate}")

## goes on to answer question 3-6
print("answers question 3-6")
model2 = LinearRegression()
model2.fit(np.asarray(ppm_data_data).reshape(-1,1), avg_temp_data)

slope2 = model2.coef_[0]
intercept2 = model2.intercept_

print(f"Slope: {slope2}, Intercept: {intercept2}")
print(model2.predict([[350]]))
print(model2.predict([[400]]))
print(model2.predict([[450]]))

## question 7
print("answers question 7")
def Co2concentrationPredictor(yearTimePrediction):
    global rate
    b = 414.2 - rate * 2020
    return rate*yearTimePrediction+b
print(Co2concentrationPredictor(2100))

print("answers question 8")
def tempPredictor(yearPrediction):
    return slope2*Co2concentrationPredictor(yearPrediction)+intercept2
print(tempPredictor(2100))
