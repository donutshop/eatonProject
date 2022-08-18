import pandas as pd
import openpyxl
import numpy as np

while True:
    df = pd.read_excel(r"C:\Users\jetji\Desktop\test_tooloing_files.xlsx")

    col = pd.DataFrame(df, columns=["T", "RACK/CABINET", "ROW/BOX"])

    x = input("Enter: ")
    x = x.upper()

    s = col[df["T"] == x]
    print("--------------------------------")

    loc1 = s["RACK/CABINET"].values
    loc2 = s["ROW/BOX"].values

    str1 = str(loc1)
    str2 = str(loc2)

    print(str1)

    message = ("You can find this in cabinet", str1, "row", str2)
    j = ''.join(message)
    print(j)



    # cab = loc1({'value': [[41], [12], [15]]})
    # print(df.index)
    # print("You can find this in cabinet", s.values)
    # print(ser[:3])
