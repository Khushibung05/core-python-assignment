def calculate_fare(distance):
    base = 50
    per_km = 10
    return base + distance * per_km

# Example
trips = [5, 10, 3]
total = 0
for i, d in enumerate(trips, start=1):
    fare = calculate_fare(d)
    print(f"Trip {i}: ${fare}")
    total += fare

print("Total Fare:", f"${total}")
