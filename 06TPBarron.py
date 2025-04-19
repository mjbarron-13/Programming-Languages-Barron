# Predefined budget (in pesos)
BUDGET = 15000  # You can adjust this value based on your budget

# Function to prompt the user for valid input
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Prompt the user for estimated costs in pesos
venue_cost = get_valid_input("Enter the estimated cost for the Venue (in pesos): ")
catering_cost = get_valid_input("Enter the estimated cost for Catering (in pesos): ")
decorations_cost = get_valid_input("Enter the estimated cost for Decorations (in pesos): ")
entertainment_cost = get_valid_input("Enter the estimated cost for Entertainment (in pesos): ")
miscellaneous_cost = get_valid_input("Enter the estimated cost for Miscellaneous (in pesos): ")

# Calculate the total estimated cost using augmented assignment operators
total_cost = 0
total_cost += venue_cost
total_cost += catering_cost
total_cost += decorations_cost
total_cost += entertainment_cost
total_cost += miscellaneous_cost

# Output the total cost
print(f"\nTotal estimated cost: {total_cost} pesos")

# Compare with the budget and indicate if within the budget
if total_cost <= BUDGET:
    print(f"The total cost is within the budget of {BUDGET} pesos.")
else:
    print(f"The total cost exceeds the budget of {BUDGET} pesos.")
