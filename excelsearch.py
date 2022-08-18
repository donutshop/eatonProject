import openpyxl as openpyxl
import pandas as pd
import syspath as syspath
import xlrd as xlrd
import csv
import wave
import numpy


#x = input("look for: " )

#cols = [1,5,6,7]
#df = pd.read_excel(r"C:\Users\jetji\Desktop\pandas\test_panda2.xlsx", usecols=cols)
#print(df)

df1 = pd.read_excel(r"C:\Users\jetji\Desktop\pandas\test_panda2.xlsx")
#print(df1)

#if 'FJ189' in ['T']:
#   print("yes")
#else:
#   print("not here")
#x = input("enter: ")

#test =  pd.DataFrame({"x": [1, 2, 3, 4, 5 ], "y": [2, 4, 6,8,9]})
#print(test)
#while True:
   # search = input("find: ")
#df1 = df1["T"].str.find(search) # find a string in a column
#print(df1[["T", "WORK CENTRE"]].to_dict())
while True:
    if "T55916" in df1["T"]:
        print("yes")
    else:
        print("no")
        break







