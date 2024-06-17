"""
booth_types = ["Food", "Games", "Music", "Crafts"]
schedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time}, Item Needed: {item}")
"""

bag_index = ["water", "phone", "wallet"]

for x in (bag_index):  # This for loop will print one item per line from the referrenced list.
    print(x)

"""
for x in range(1, 11, 2): # setting the range(1, 11, 2) means that I want it to start with 1, go to 10, and move in incriments of 2.
    print(x)
    
for x in range(1, 21):
    if x == 13:
        continue # Skipping 13 in the count
    else:
        print(x)
"""