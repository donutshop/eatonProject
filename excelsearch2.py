import openpyxl

#this code is from https://pythonguides.com/python-read-excel-file/#:~:text=To%20read%20an%20excel%20file%20in%20Python%2C%20we,is%20used%20to%20extract%20data%20from%20a%20spreadsheet.



path = r"C:\Users\jetji\Desktop\test_excel.xlsx" #the r figure is for transforming a string to a raw string
        #raw string treats backlash as a literal character.
x = input("enter: ")

workbook = openpyxl.load_workbook(path) # create object for path
sheet = workbook.active
cell= sheet.cell(row="", col="")
if x in sheet:
    print(cell.value)
else:
    print("not here")

#print(cell_obj.value)
