#Adding keys and values to a dictionary using input function

dictionary = {"a":1, "b":2, "c":3}
dictionary2 = {}

while True:

  key = input("enter keys here: ")
  value = input("enter values here: ")

  x = dictionary.keys() #show keys
  y = dictionary.values() #show values
  print(x,y)

  dictionary[key] = value #to add a key
  print(x)

  dictionary2[key] = value #input as an argument to add key elements

  print(dictionary.items())
  print(dictionary2.items())
