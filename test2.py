age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

while True:
    thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }

    x = input("enter: ").lower()
    print(x)
    if x in thisdict:
      print("Yes, " + x + " is one of the keys in the thisdict dictionary")
    else:
        print("It is not")