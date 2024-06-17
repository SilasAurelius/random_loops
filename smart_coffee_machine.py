# Initialize the coffee reservoir level
coffee_reservoir = 10
# List types of coffee types
coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"]

# Start dispensing coffee
while coffee_reservoir > 0:
    # Check if there is still coffee types available.
    if coffee_types:
        # Dispense the first type of coffee
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}.")
        # Decrement the coffee reservoir
        coffee_reservoir -= 1
        print(f"Coffee types left: {coffee_types}")
    else: 
        print("No more coffee types available.")
        break
# Coffee reservoir empty
print("The coffee reservoir is now empty")