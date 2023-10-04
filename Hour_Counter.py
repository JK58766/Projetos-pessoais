# Programa que calcula o horárop em que um evento ficará disponível em determinada quantidade de tempo

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))

print("Current Time =", current_time)

howManyH = int(input("How many hours until the event?"))
howManyM = int(input("How many minutes until the event?"))
print(f"{howManyH}:{howManyM} until the event")
i = 0
j = 0

while i < howManyH:
    hour = hour + 1
    if hour >= 24:
        hour = 0
    
    i = i + 1

while j < howManyM:
    minute = minute + 1
    if minute > 60:
        minute = 0
        hour = hour + 1
    j = j +1

if minute < 10:
    minute = "0" + str(minute)
    
print(f"The event will be at {hour}:{minute}.")
