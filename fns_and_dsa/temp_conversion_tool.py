FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
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
    except ValueError:
        print("Invalid temperature input. Please enter a numeric value.")
if __name__ =="__main__":
    main()