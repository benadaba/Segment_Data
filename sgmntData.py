# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:24:02 2016

@author: Bernard.
"""



import pandas as pd

# read csv file
dataFile = pd.read_csv("TrendData.csv")


# Change Dates to consistent format
print("Fixing timestamps...")

dataFile['Date'] = pd.to_datetime(dataFile['Date'], format='%d/%m/%Y')


'''
Would want to split the dates into months ; with startDate being the first
day of the month and entry was made and endDate being the last day of the month
an entry was made
'''

# Define aggregation calculations
aggregations = {
    'Date': { # work on the "Date" column
        'startDate': 'min',  # get the first date entry, and call this result 'startDate'
        'endDate': 'max' # get last date entry, call result 'endDate'
    },
    'Value': {     # Now work on the "Value" column
        'startValue': 'last',   # Find the first value that was entered in the month, call the result "startValue"
        'endValue': 'first' # Find the last value that was entered in the month, call the result "endValue"
    }
}
 

# split Data on into Months and Year , and get the first and last entries for both months
# and assign the respective first and last entered values for the month and store in a dataframe
result = dataFile.groupby([dataFile['Date'].dt.month, dataFile['Date'].dt.year]).agg(aggregations)    # get the first date per group
                                                                         
                                     
print(result)

#convert and output dataframe as CSV file
result.to_csv('outputResult.csv')
