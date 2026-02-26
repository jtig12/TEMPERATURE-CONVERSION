# TEMPERATURE CONVERSION

### DESCRIPTION

    This app helps to convert temperature from the users from celcius to fahrenhiet and vice versa.

### Steps taken to develop the project

1. Firstly we give the user an input where they can input the temperature and the unit of the temperature
2. Then we write codes to convert celcius to fahrenheit.
   ```py
       if unit == "c".upper():
           temp = (temp * (9/5)) + 32
           unit = "℉"
           print(f"Your temperature is {temp} {unit}")
   ```
3. Then we writes codes to convert fahrenheit to celcius and also if it not an of this should display invalid.
   ```py
       elif unit == "f".upper():
           temp = (temp - 32) * (5/9)
           unit = "℃"
           print(f"Your temperature is {temp} {unit}")
       else:
           print(f"{unit} is an invalid unit of measurement")
   ```

## OUTCOME EXECUTION
