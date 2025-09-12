'''7. Taxi Fare Calculation
Scenario:
A taxi service calculates fares based on the following rates: 
- **Base fare**: $50 
- **Distance fare**: $10/km 
Write a program to calculate the total fare for multiple trips.
Requirements:
- Use a function to calculate fare for each trip.
Input Example:
trips = [5, 10, 3]  # Distances in km
Expected Output:
Trip 1: $100
Trip 2: $150
Trip 3: $80
Total Fare: $330
 '''
def calculate_fare(distance, base_fare=50, per_km=10):
    return base_fare + (distance * per_km)
trips = list(map(int, input("Enter trip distances in km (space separated): ").split()))
total_fare = 0
trip_number = 1 
for distance in trips:
    fare = calculate_fare(distance)
    print("Trip", trip_number, ":", "$" + str(fare))
    total_fare += fare
    trip_number += 1
print("Total Fare:", "$" + str(total_fare))
