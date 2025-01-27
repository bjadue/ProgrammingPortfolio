# Brandon Jadue
# 1/24/24
# This program will collect, convert, and plot temperature data.
import matplotlib.pyplot as graph

temperatures_fahrenheit = []
temperatures_celsius = []
dayCount = []

def tempConvert(fTemp):
    cTemp = int((fTemp - 32) * 5/9)
    temperatures_celsius.append(cTemp)

for i in range(0, 5):
    curTemp = int(input("Enter a temperature in Fahrenheit: "))
    temperatures_fahrenheit.append(curTemp)
    tempConvert(curTemp)
    dayCount.append(i)

# print(temperatures_fahrenheit)
# print(temperatures_celsius)
colors = ['red', 'blue']

graph.title("Weekly Temperature Analysis")
graph.xlabel("Week Days")
graph.ylabel("Temperature")
graph.grid()

graph.xlim(xmin=0, xmax=4)
graph.xticks([0, 1, 2, 3, 4],
             ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

graph.plot(dayCount, temperatures_fahrenheit, color=colors[0], label='Fahrenheit (°F)')
graph.plot(dayCount, temperatures_celsius, color=colors[1], label='Celsius (°C)')
graph.legend()
graph.show()

# another successful coding assignment *celebration sounds*