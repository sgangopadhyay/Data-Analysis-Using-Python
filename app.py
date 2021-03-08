# PROGRAM : A SMALL PROGRAM TO DEMONSTRATE DATA ANALYTICS USING PYTHON
# CODED BY : SUMAN GANGOPADHYAY
# Email ID : linuxgurusuman@gmail.com
# GITHUB URL :
# DATE : 6-March-2021
# CAVEATS : This is the main file to be run in the Python terminal with many dependencies
# DEPENDENCIES : data.py, suman_stat.py, graph.py

from flask import Flask
from flask import request, render_template, redirect, url_for
import suman_stat
import data
import graph

# d = data.Suman()
#
# print(d.final_data())
#
# data1 = [160,160,161,162,163,163,163,164,164,170]
#
# s = suman_stat.Pure_Statistics()
#
# print(s.nmean(data1))
d = data.Data_From_CSV_File()
g = graph.Graph()
s = suman_stat.Basic_Statistics()

print(g.bar_graph())