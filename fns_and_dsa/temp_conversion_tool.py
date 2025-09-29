FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32




temperature = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    converted = convert_to_celsius(temperature)
    print(f"\nTemperature in Fahrenheit: {temperature}")
    print(f"Temperature in Celsius: {converted:.2f}")
    print(f"Conversion factor used: {FAHRENHEIT_TO_CELSIUS_FACTOR:.2f}")

elif unit == "C":
    converted = convert_to_fahrenheit(temperature)
    print(f"\nTemperature in Celsius: {temperature}")
    print(f"Temperature in Fahrenheit: {converted:.2f}")
    print(f"Conversion factor used: {CELSIUS_TO_FAHRENHEIT_FACTOR:.2f}")

else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
temperature = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    converted = convert_to_celsius(temperature)
    print(f"\nTemperature in Fahrenheit: {temperature}")
    print(f"Temperature in Celsius: {converted:.2f}")
    print(f"Conversion factor used: {FAHRENHEIT_TO_CELSIUS_FACTOR:.2f}")

elif unit == "C":
    converted = convert_to_fahrenheit(temperature)
    print(f"\nTemperature in Celsius: {temperature}")
    print(f"Temperature in Fahrenheit: {converted:.2f}")
    print(f"Conversion factor used: {CELSIUS_TO_FAHRENHEIT_FACTOR:.2f}")

else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")