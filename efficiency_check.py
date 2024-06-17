# Initialize the battery level
battery = 0
increment = 10 #Inital charging increment

# Start charging the battery
while battery < 100:
    # Charge battery
    battery += increment
    print(f"Battery at {battery}%")
    
    # Check the efficiency and adjust the charging rate.
    if battery == 50:
        print("Efficiency check: Increasing charge rate.")
        increment = 15
    elif battery == 80:
        print("Efficiency check: Reducing charge rate to prevent overcharging.")
        increment = 5
    
    
print("Battery fully charged!")