def calculate_average(values):
    """Return the average of a list of numbers."""
    return sum(values) / len(values)

values = [72, 55, 101, 90]
print(calculate_average(values))

stations = [
    ['A1', 62],
    ['B5', 97],
    ['C3', 155]
]
for station in stations:
    print(f"{station[0]} → {station[1]}")
  
def report_status(stations, threshold):
    """
    For each [id, pm25] in stations,
    print "id → pm25 µg/m³ (safe)" if pm25 < threshold,
    else "(danger!)"
    """
    for station in stations:
        id, pm25 = station
        if pm25 < threshold:
            print(f"{id} → {pm25} µg/m³ (safe)")
        else:
            print(f"{id} → {pm25} µg/m³ (danger!)")
