# Initialize a countdown variable with the starting number.
# Creat an empty list to store the numbers you land on.
# Write a while loop that counts down from the starting number.
# Append the numbers you land on to the list.
# Use list slicing to display the final list of numbers.

"""
countdown_number = 10
current_number = []

while countdown_number > 0:
    current_number.append(countdown_number)
    print(f"The current number is: {current_number}")
    countdown_number -= 1
    continue
if current_number == 0:
    print("The current number is now 0")
    print(current_number[1, 11])"""
    
count = 10
    
landed_number = []
    
while count > 0:
    count -= 1
    if count % 2 == 1:
        continue
    landed_number.append(count)
        
print("Numbers landed on:",landed_number[::-1])
