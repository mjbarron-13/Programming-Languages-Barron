# Function to get valid float input
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get valid string input
def get_string_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please enter a valid string.")

# Accepting trip details
starting_location = get_string_input("Enter the starting location: ")
destination = get_string_input("Enter the destination: ")
mode_of_transport = get_string_input("Enter the mode of transport (e.g., car, bus, bike): ")

# Accepting distance and speed details
distance = get_float_input("Enter the distance of the trip (in kilometers): ")
speed = get_float_input("Enter the average speed of travel (in km/h): ")

# Calculate the estimated travel time
travel_time = distance / speed

# Determine if the travel time exceeds 5 hours
long_trip = travel_time > 5

# Display the travel details
print("\nTrip Details:")
print(f"Starting Location: {starting_location}")
print(f"Destination: {destination}")
print(f"Mode of Transport: {mode_of_transport}")
print(f"Distance: {distance} km")
print(f"Speed: {speed} km/h")
print(f"Estimated Travel Time: {travel_time:.2f} hours")

# If travel time is greater than 5 hours, recommend a rest stop
if long_trip:
    print("Warning: The trip will take more than 5 hours. A rest stop is recommended.")

