import pandas as pd

while True:
    df = pd.read_excel(r"C:\Users\jetji\Desktop\test_tooloing_files.xlsx")

    x = input("Enter: ")
    x = x.upper()
    y = "T"
    find = df[df[y] == x]

    print(find.values)
    print("=========================")
