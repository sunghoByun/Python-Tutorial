bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

time = 0
while len(truck_weights) > 0 :
    lenTruck = 0
    weightTruck = 0
    while True:
        tmpTruck = truck_weights[0]
        if weightTruck + tmpTruck <= weight:
            weightTruck += tmpTruck
            lenTruck +=1
            truck_weights.pop(0)
        else:
            break
    if lenTruck == 1:
        time += bridge_length
    else:
        time += bridge_length + (lenTruck - 1)

    if len(truck_weights) <= 1 :
        time += 1

print(time)
