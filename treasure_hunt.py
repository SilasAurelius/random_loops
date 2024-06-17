caves = [False, False, True, False, False]

# Iterate over the caves.
for i, cave in enumerate(caves):
    # Check if the cave has the treasure.
    if cave:
        print(f"Treasure found in cave {i +1}!")
        break # Stop searching once the treasure is found.