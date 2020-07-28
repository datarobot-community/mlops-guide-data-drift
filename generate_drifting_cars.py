import auto_mpg
import json

cars = []

for i in range(0, 1500):
    cars.append(auto_mpg.Car())

carsDict = [dict(car) for car in cars]

with open('resources/drifting_cars.json', mode='w') as drifting_cars:
    json.dump(carsDict, drifting_cars)
