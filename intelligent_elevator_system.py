current_floor = 5
requested_stops = [1, 3, 4]

# Start the elevator
while current_floor > 0:
    #Check if the current floor is a request stop.
    if current_floor in requested_stops:
        print(f"Stopping at floor {current_floor}.")
        requested_stops.remove(current_floor)
    # Move the elevator down a floor
    current_floor -= 1
    print(f"Descending to floor {current_floor}.")

# Ground floor reached
print("The elevator has reached the ground floor.")

"""while current_floor > 0:
    if current_floor in requested_stops:
        print(f"Stopping at floor {current_floor}.")
        requested_stops.remove(current_floor)
    current_floor -= 1
    print(f"Descending to floor {current_floor}.")
print("The elevator has reached the bottom floor.")
"""