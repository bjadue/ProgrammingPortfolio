# Brandon Jadue
# 9/6/23
# This program will convert the user-inputted temperature from Fahrenheit to Celsius.

# Program asks for input and inserts it into the variable.
tempF = int(input("What is the current temperature in Fahrenheit? "))
# The input is then put into the conversion equation.
tempC = 5 / 9 * (tempF - 32 )

# Previous debugging print calls.
# print(tempF)
# print(f"{tempC:.0f}")

# The program then reads back the statistics to the user.
print("\nThe temperature in Fahrenheit is " + str(tempF) + "°F.\nThis converts to " + (f"{tempC:.0f}") + "°C.")

# Diamond art time :D

print(f"{'*':^20}")
print(f"{'***':^20}")
print(f"{'*****':^20}")
print(f"{'*******':^20}")
print(f"{'*********':^20}")
print(f"{'***********':^20}")
print(f"{'*********':^20}")
print(f"{'*******':^20}")
print(f"{'*****':^20}")
print(f"{'***':^20}")
print(f"{'*':^20}")
