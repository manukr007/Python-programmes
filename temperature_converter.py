temp = float(input("Input the  temperature to be converted?"))
convert = input("Convert to (F)ahrenheit or (C)elsius?")

if convert == "C":
  result = int(round((9 * temp) / 5 + 32))
  convention = "Fahrenheit"
elif convert == "F":
  result = int(round((temp - 32) * 5 / 9))
  convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", convention, "is", result, "degrees.")