# PROGRAM : DEPENDENCY FILE FOR app.py WHERE WE EXTRACT AND MANIPULATE DATA FROM CSV FILE
# CODED BY : SUMAN GANGOPADHYAY
# Email ID : linuxgurusuman@gmail.com
# GITHUB URL :
# DATE : 6-March-2021
# CAVEATS : Import this file in the app.py

import pandas as pd
import math
import statistics
import matplotlib as mat
import scipy as sci
import seaborn as sea
class Data_From_CSV_File():
    # READ THE CSV FILE
    try:
        file = pd.read_csv("data/test.csv")
    except:
        print("ERROR : Either Original CSV File Missing / Unknown Error !")
    # FILL ALL BLANK VALUES / NULL VALUES WITH ZERO OF EVERY COLUMNprint("ERROR : Either Original CSV File Missing / Unknown Error !")
    def __init__(self):
        self.file['ta'] = self.file['ta'].dropna()
        self.file['ta'] = self.file['ta'].fillna(0)
        self.file['da'] = self.file['da'].dropna()
        self.file['da'] = self.file['da'].fillna(0)
        self.file['hra'] = self.file['hra'].dropna()
        self.file['hra'] = self.file['hra'].fillna(0)
        self.file['total'] = self.file['total'].dropna()
        self.file['total'] = self.file['total'].fillna(0)
    # CALCULATE THE HRA OF EACH COLUMN
    def hra_calculator(self):
        self.file['ta'] = 0.4 * self.file['basic']
        return self.file['ta']
    # CALCULATE THE TA OF EACH COLUMN
    def ta_calculator(self):
        self.file['ta'] = 0.25 * self.file['basic']
        return self.file['ta']
    # CALCULATE THE DA OF EACH COLUMN
    def da_calculator(self):
        self.file['da'] = 0.5 * self.file['basic']
        return self.file['da']
    # CALCULATE THE GROSS SALARY
    def gross_salary(self):
        self.file['total'] = self.file['basic'] + self.file['ta'] + self.file['da'] + self.file['hra']
        return self.file['total']
    # REPLACE THE INITIAL ZERO VALUE OF TA, DA, HRA, TOTAL_SALARY WITH NEW CALCULATED VALUES
    def final_data(self):
        self.file['ta'] = self.ta_calculator()
        self.file['da'] = self.da_calculator()
        self.file['hra'] = self.hra_calculator()
        self.file['total'] = self.gross_salary()
        return self.file
    def data_transform(self):
        basic, ta, da, hra, total = [], [], [], [], []
        self.file['ta'] = self.ta_calculator()
        self.file['da'] = self.da_calculator()
        self.file['hra'] = self.hra_calculator()
        self.file['total'] = self.gross_salary()
        for i in self.file['basic']:
            basic.append(math.log10(i))
        for i in self.file['ta']:
            ta.append(math.log10(i))
        for i in self.file['da']:
            da.append(math.log10(i))
        for i in self.file['hra']:
            hra.append(math.log10(i))
        for i in self.file['total']:
            total.append(math.log10(i))
        self.file['basic'] = basic
        self.file['ta'] = ta
        self.file['da'] = da
        self.file['hra'] = hra
        self.file['total'] = total
        return self.file
    # CREATE A NEW CSV FILE AFTER SCALING THE DATA USING LOG TRANSFORMATION
    def new_file(self):
        try:
            columns = ('sl_no', 'name', 'place', 'basic', 'ta', 'da', 'hra', 'total')
            new_data = pd.DataFrame(self.data_transform(), columns = columns).to_csv('data/new_test_data.csv')
            print("SUCCESS : NEW CSV FILE CREATED SUCCESSFULLY")
            return new_data
        except:
            print("ERROR : Either Original CSV File Missing / Unknown Error !")
    # CREATE A BAR GRAPH USING THE SCALED DATA
    def bar_graph(self):
        d = self.data_transform()

