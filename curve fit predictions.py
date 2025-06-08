import csv
from scipy.optimize import curve_fit
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

def quadratic_func(x,a,b,c):
    return a*((x)**2)+b*x+c

def expGrowth_func(x,k,a,b,d,c):
    return k*(a**(b*x+d))+c

def linear_func(x,m,b):
    return m*x+b

temperatureModelQuad = curve_fit(quadratic_func, years_data,avg_temp_data)

carbEmissQuad = curve_fit(quadratic_func, years_data,glob_carb_emiss_data)

ppmQuad = curve_fit(quadratic_func, years_data,ppm_data_data)



temperatureExp = curve_fit(expGrowth_func, years_data,avg_temp_data,maxfev=100000)

carbEmissExp = curve_fit(expGrowth_func, years_data,glob_carb_emiss_data,maxfev=100000)

ppmExp = curve_fit(expGrowth_func, years_data,ppm_data_data,maxfev=100000)



linearTemp = curve_fit(linear_func,years_data,avg_temp_data)

linearEmiss = curve_fit(linear_func,years_data,glob_carb_emiss_data)

linearPpm = curve_fit(linear_func,years_data,ppm_data_data)

def temperaturePredictionQuad(x):
    return quadratic_func(x,temperatureModelQuad[0][0],temperatureModelQuad[0][1],temperatureModelQuad[0][2])

def carbEmissPrediction(x):
    return quadratic_func(x, carbEmissQuad[0][0], carbEmissQuad[0][1], carbEmissQuad[0][2])

def ppmPrediction(x):
    return quadratic_func(x, ppmQuad[0][0], ppmQuad[0][1], ppmQuad[0][2])



def temperaturePredictionExp(x):
    return expGrowth_func(x,temperatureExp[0][0],temperatureExp[0][1],temperatureExp[0][2], temperatureExp[0][3], temperatureExp[0][4])

def carbEmissPredictionExp(x):
    return expGrowth_func(x, carbEmissExp[0][0], carbEmissExp[0][1], carbEmissExp[0][2], carbEmissExp[0][3],
                          carbEmissExp[0][4])

def ppmPredictionExp(x):
    return expGrowth_func(x, ppmExp[0][0], ppmExp[0][1], ppmExp[0][2], ppmExp[0][3],
                          ppmExp[0][4])



def temperaturePredictionLinear(x):
    return linear_func(x,linearTemp[0][0],linearTemp[0][1])

def emissionPredictionLinear(x):
    return linear_func(x,linearEmiss[0][0],linearEmiss[0][1])

def ppmPredictionLinear(x):
    return linear_func(x,linearPpm[0][0],linearPpm[0][1])


print("temperatures for the year 2100 based on the quadratic, then exponential, then linear fit will be:")
print(temperaturePredictionQuad(2100))
print(temperaturePredictionExp(2100))
print(temperaturePredictionLinear(2100))

print("carbon emissions for the year 2100 based on the quadratic, then exponential, then linear fit will be:")
print(carbEmissPrediction(2100))
print(carbEmissPredictionExp(2100))
print(emissionPredictionLinear(2100))

print("Co2 concentration for the year 2100 based on the quadratic, then exponential, then linear fit will be:")
print(ppmPrediction(2100))
print(ppmPredictionExp(2100))
print(ppmPredictionLinear(2100))