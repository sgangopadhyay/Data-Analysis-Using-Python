# PROGRAM : Python Module for Statistical Methods 
# PROGRAMMED BY : Suman Gangopadhyay
# DATE : 2-March-2021
# E-MAIL : linuxgurusuman@gmail.com
# CAVEATS : None
# GITHUB URL : https://github.com/sgangopadhyay/my-statistics-module.git

import math
class Basic_Statistics():
    sum = 0.0
    mean = 0.0
    number = 0.0
    coefficient_of_range = 0.0
    average = 0.0
    # CHECK WHETHER THE NUMBERS IN THE LIST ARE ACTUALLY INTEGERS / FLOAT
    def check_number_in_list(self,data):
        number_count = 0
        not_number_count = 0
        total_elements = int(len(data))
        for data in data:
            if (isinstance(data, int) == True or isinstance(data, float) == True):
                number_count = number_count + 1
            elif (isinstance(data, int) == False or isinstance(data, float) == False):
                not_number_count = not_number_count + 1
        if (total_elements == number_count):
            return True
        else:
            return False
    # Calculation the Sum of all the datas of a Dataset
    def sum_of_datas(self, data):
        if (self.check_number_in_list(data)==True):
            for i in range(0, len(data)):
                self.sum = self.sum + data[i]
            return (float(self.sum))
        else:
            return ("ERROR (TOTAL SUM) : INT / FLOAT not in Data")
    # Calculation the MEAN / ARITHMATIC AVERAGE of a Dataset
    def nmean(self, data):
        res = 0
        if (self.check_number_in_list(data)==True):
            self.mean = self.sum_of_datas(data)
            res = self.mean/len(data)
            return (float(res))
        else:
            return ("ERROR(NUMERIC AVERAGE) : INT / FLOAT not in Data")

    # Calculation the MEAN /  ARITHMATIC AVERAGE DISCREET SERIES of a Dataset
    def dsmean(self, data, frequency):
        res_list = []
        if(self.check_number_in_list(data)==True and self.check_number_in_list(frequency)==True):
            if (len(data) == len(frequency)):
                for i in range(0, len(data)):
                    res_list.append(data[i] * frequency[i])
                    self.sum = self.sum + res_list[i]
                return (self.sum)
            else:
                print("ERROR : The data of elements in Series and Frequency is not matching")
        else:
            return ("ERROR(ARITHMATIC AVERAGE DISCREET SERIES) : INT / FLOAT not in Data")

    # Calculation the MEDIAN of a Dataset
    def median(self, data):
        if (self.check_number_in_list(data) == True):
            data.sort()
            # FOR EVEN NUMBER SERIES
            if (len(data) % 2 == 0):
                self.number = (len(data) + 1) / 2
                return ((data[int(self.number) - 1] + data[int(self.number)]) / 2)
            # FOR ODD NUMBER SERIES
            elif (len(data) % 2 != 0):
                self.number = (len(data) + 1) / 2
                return (data[int(self.number - 1)])
        else:
            return ("ERROR(MEDIAN) : INT / FLOAT not in Data")

    # Calculation the MODE of a Dataset 
    def mode(self, data):
        if(self.check_number_in_list(data)==True):
            pass
        else:
            return ("ERROR(MODE) : INT / FLOAT not in Data")

    # Calculation the GEOMETRIC MEAN of a Dataset
    def gmean(self, data):
        new_log_list = []
        if(self.check_number_in_list(data)==True):
            for i in range(0, len(data)):
                new_log_list.append(math.log10(data[i]))
            for i in range(0, len(new_log_list)):
                self.sum = self.sum + new_log_list[i]
            return (10 ** (self.sum / len(new_log_list)))
        else:
            return ("ERROR(GEOMETRIC MEAN) : INT / FLOAT not in Data")


    # Calculation of the HARMONIC MEAN of a Dataset
    def hmean(self, data):
        if (self.check_number_in_list(data)==True):
            for i in range(0, len(data)):
                self.sum = self.sum + 1 / data[i]
                self.mean = len(data) / self.sum
                return (self.mean)
        else:
            return ("ERROR(HARMONIC MEAN) : INT / FLOAT not in Data")

    # Calculation the CO-EFFICIENT OF RANGE of a Dataset
    def cofrange(self, data):
        if (self.check_number_in_list(data)==True):
            data.sort()
            max = data[-1]
            min = data[0]
            self.coefficient_of_range = float((max - min) / (max + min))
            return (self.coefficient_of_range)
        else:
            return ("ERROR(RANGE COEFFICIENT) : INT / FLOAT not in Data")

    # Calculation of Standard Deviation
    def standard_deviation(self, data):
        if (self.check_number_in_list(data)==True):
            self.average = self.nmean(data)
            dev_mean = []
            square_dev = []
            a = 0.0
            b = 0.0
            sum_of_stand_dev_square = 0.0
            for i in data:
                a = i - self.average
                b = a * a
                dev_mean.append(a)
                square_dev.append(b)
            for i in square_dev:
                self.sum = self.sum + i
            print (float(self.sum))
            print(dev_mean)
            print(square_dev)


# CLASS FOR REGRESSION, LINEAR REGRESSION, MULTIPLE REGRESSION
# class Regression(Basic_Statistics):
#     def __init__(self):
#         pass
#     def linear(self, data):
#         if isinstanceself.mean(data, int) == True or isinstance(data, float) == True:
#             pass
#         else:
#             return ("ERROR : INT / FLOAT not in Data")
#     def multiple(self, data):
#         if isinstance(data, int) == True or isinstance(data, float) == True:
#             pass
#         else:
#             return ("ERROR : INT / FLOAT not in Data")
#     coefficient_of_range = 0.0
#
x = [160,160,161,162,163,163,163,164,164,170]
y = [2,3,4]
z= [9.0, 9.0, 4.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 49.0]

s = Basic_Statistics()

print(s.standard_deviation(x))
# print(s.sum_of_datas(z))
