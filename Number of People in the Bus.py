def number(bus_stops):
    n = 0
    for i in range(len(bus_stops)):
        n = n + (bus_stops[i][0] - bus_stops[i][1])
    return n


print(number([[10, 0], [3, 5], [5, 8]]))
