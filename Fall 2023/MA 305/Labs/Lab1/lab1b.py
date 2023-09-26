"""
Name: Krystian Confeiteiro
Professor: Dr. Sam
Course: MA-305 - Introduction to Scienfific Computing
Assignment: Lab 1 (Part B) - Problem 2
Script name: lab1a.py
Date: 09/25/2023
"""

# problem 2
## define function to convert F -> C
def int_strs_to_list(ints):
    return list(map(lambda x: int(x), ints.split()))

def f_to_c(*temps):
    return [round(((9/5)*temp) + 32, 3) for temp in temps]

print("\nProblem 3:\n----------")
print("Please enter temperatures in Fahrenheit.")
print("(You can enter a single temperature or\nmultiple temperatures separated by a space)")

temps = (-40, 0, 30, 100)
temps_input = input("\nTemperatures: ")
temps_input_calcd = f_to_c(*int_strs_to_list(temps_input))
calcd_temps = f_to_c(*temps)

print("\nConverting -40°F, 0°F, 30°F, 100°F to °C:")
[print(f"{i + 1}) {temp}°C") for i, temp in enumerate(calcd_temps)]

print(f"\nCalculated Tempereatures (from input):")
[print(f"{i + 1}) {temp}°C") for i, temp in enumerate(temps_input_calcd)]
