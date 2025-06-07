import csv
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

startpoint = 1959
endpoint = 2023

def findAvearge(startYear,endYear):
    endYear = endYear + 1
    start = startYear - startpoint
    cutsection = start + (endYear-startYear)
    #print(start)
    #print(cutsection)
    print(f"Average from {startYear} to {endYear} for average temperatures are {sum(avg_temp_data[start:cutsection])/ (endpoint - startpoint)}")
    print(f"Average from {startYear} to {endYear} for carbon emissions are {sum(glob_carb_emiss_data[start:cutsection]) / (endpoint - startpoint)}")
    print(f"Average from {startYear} to {endYear} for co2 concentration are {sum(ppm_data_data[start:cutsection]) / (endpoint - startpoint)}")

def findVaryingChangeNumber(startYear,endYear):
    endYear = endYear + 1
    start = startYear - startpoint
    cutsection = start + (endYear-startYear)
    print(f"Varying numbers from {startYear} to {endYear} for temperatures are {np.var(avg_temp_data[start:cutsection],ddof=1)}")
    print(f"Varying numbers from {startYear} to {endYear} for carbon emissions are {np.var(glob_carb_emiss_data[start:cutsection],ddof=1)}")
    print(f"Varying numbers from {startYear} to {endYear} for co2 concentration are {np.var(ppm_data_data[start:cutsection],ddof=1)}")

def findVariationFromMean(startYear,endYear):
    endYear = endYear + 1
    start = startYear - startpoint
    cutsection = start + (endYear - startYear)
    print(f"Varying numbers from mean of {startYear} to {endYear} for temperatures are {np.std(avg_temp_data[start:cutsection], ddof=1)}")
    print(f"Varying numbers from mean of {startYear} to {endYear} for carbon emissions are {np.std(glob_carb_emiss_data[start:cutsection], ddof=1)}")
    print(f"Varying numbers from mean of {startYear} to {endYear} for co2 concentration are {np.std(ppm_data_data[start:cutsection], ddof=1)}")

## function I made back in old stats class, allowed me to obtain five number summary
def quartiles(data, datasize):

    if datasize % 2 == 0:
        median = (data[datasize // 2 - 1] + data[datasize // 2]) / 2

        firstQuartileData = data[0: datasize // 2]

        firstQuartileDataLength = len(firstQuartileData)


        thirdQuartileData = data[datasize // 2: datasize]

        thirdQuartileDataLength = len(thirdQuartileData)

        if firstQuartileDataLength % 2 == 0:

            firstQuartileNumber = (firstQuartileData[firstQuartileDataLength // 2 - 1] + firstQuartileData[firstQuartileDataLength // 2]) / 2

            thirdQuartileNumber = (thirdQuartileData[thirdQuartileDataLength // 2 - 1] + thirdQuartileData[thirdQuartileDataLength // 2]) / 2

        else:

            firstQuartileNumber = firstQuartileData[firstQuartileDataLength // 2]

            thirdQuartileNumber = thirdQuartileData[thirdQuartileDataLength // 2]

    else:
        median = data[datasize // 2]

        firstQuartileData = data[0: datasize // 2]

        firstQuartileDataLength = len(firstQuartileData)

        thirdQuartileData = data[ (datasize // 2) + 1: datasize]

        thirdQuartileDataLength = len(thirdQuartileData)


        if firstQuartileDataLength % 2 == 0:

            firstQuartileNumber = (firstQuartileData[firstQuartileDataLength // 2 - 1] + firstQuartileData[firstQuartileDataLength // 2]) / 2

            thirdQuartileNumber = (thirdQuartileData[thirdQuartileDataLength // 2 - 1] + thirdQuartileData[thirdQuartileDataLength // 2]) / 2

        else:

            firstQuartileNumber = firstQuartileData[firstQuartileDataLength // 2]

            thirdQuartileNumber = thirdQuartileData[thirdQuartileDataLength // 2]

    # Print the median of the list
    print("min: ",data[0])
    print("max: ", data[-1])
    print("Median of list is : " + str(median))
    print("first Quartile: ", firstQuartileNumber)
    print("third Quartile: ", thirdQuartileNumber)

    Iqr = thirdQuartileNumber - firstQuartileNumber
    print("IQR: ", Iqr)
    print( "upper fence: ", thirdQuartileNumber + ( 1.5 * Iqr ) )
    print( "lower fence: ", firstQuartileNumber - ( 1.5 * Iqr) )


def findFiveNumberSummary(startYear,endYear):
    print("###temperatures five number summary###")
    endYear = endYear + 1
    start = startYear - startpoint
    cutsection = start + (endYear - startYear)
    quartiles(avg_temp_data[start:cutsection],len(avg_temp_data[start:cutsection]))
    print()
    print("###carbon emissions five number summary###")
    quartiles(glob_carb_emiss_data[start:cutsection], len(glob_carb_emiss_data[start:cutsection]))
    print()
    print("###Co2 concentration (ppm) five number summary###")
    quartiles(ppm_data_data[start:cutsection], len(ppm_data_data[start:cutsection]))

def median(data):
    sorted_data = sorted(data)
    n = len(data)

    # Median
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    print(median)

def findMedian(startYear, endYear):
    endYear = endYear + 1
    start = startYear - startpoint
    cutsection = start + (endYear - startYear)
    print("median for temperatures")
    median(avg_temp_data[start:cutsection])
    print("median for carbon emissions")
    median(glob_carb_emiss_data[start:cutsection])
    print("median for co2 conentration (ppm)")
    median(ppm_data_data[start:cutsection])


findAvearge(1959,2023)
print()
findVaryingChangeNumber(1959,2023)
print()
findVariationFromMean(1959,2023)
print()
findFiveNumberSummary(1959,2023)
print()
findMedian(1959,2023)

