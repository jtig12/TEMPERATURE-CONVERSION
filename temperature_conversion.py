# temperature conversion

temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in celsius or fahrenheit (c/f): ").upper()

if unit == "c".upper():
    temp = (temp * (9/5)) + 32
    unit = "℉"
    print(f"Your temperature is {temp} {unit}")
elif unit == "f".upper():
    temp = (temp - 32) * (5/9)
    unit = "℃"
    print(f"Your temperature is {temp} {unit}")
else:
    print(f"{unit} is an invalid unit of measurement")
