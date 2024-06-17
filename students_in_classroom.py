# 30 students - 5 rows
#Each row can seat an equal number students.
#Use for loop with the range function to assign and print a seat number for each student.
#Seat numbers should start at 1 and increase sequentially.
"""
total_students = 30
rows = 5

students_per_row = total_students // rows

for row in range(1, rows + 1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row-1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: Student {seat}")
"""

#list of item prices
#Use a for loop to iterate through the list of prices
# Calculate the total cost by adding up the prices of all the itmes
#Print the total cost at the end.

"""
item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]

total_cost = 0

for price in item_prices:
    total_cost += price # += is adding each entry of the item_prices list. 

print(f"The total cost is: ${total_cost:.2f}")
"""

#Ask the user for the size of the multiplication table they wish to generate.
# Use nested for loops to calculate the product of each pair of numbers.
# Display the multiplaction table in a formmated manner.

"""
table_size = int(input("Enter the size of the multiplication table: "))

for row in range(1, table_size, +1):
    for col in range(1, table_size, +1):
        product = row * col
        print(f"{product} \t", end="")
    print()
"""

table_size = int(input("Enter size of the multiplaction table: "))

for row in range(1, table_size, +1):
    for col in range(1, table_size, +1):
        product = row * col
        print(f"{product} \t", end="")
    print()