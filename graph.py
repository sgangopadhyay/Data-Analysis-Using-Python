import data
import suman_stat
import math
import statistics
import pandas as pd
import numpy as np

class Graph():
    def __init__(self):
        file = data.Data_From_CSV_File()
        file =  pd.read_csv(file.new_file())
    def bar_graph(self):
        print(self.file)

