"""import random

for _ in range(10):
    dice_roll = random.randint(1, 6)
    print("You rolled a " + str(dice_roll) + "!")
"""

"""
import random

playlist = ['song1', 'song2', 'song3', 'song4', 'song5']
random.shuffle(playlist)

for song in playlist:
    print(song)
"""

# Random Loop
import random

snacks = ['apple', 'banana', 'carrot stick', 'doughnut', 'chocolate bar']
picked_snack = ''

while picked_snack != 'chocolate bar':
    picked_snack = random.choice(snacks)
    print("You got a " + picked_snack + ".")
    if picked_snack != 'chocolate bar':
        print("Let's pick again!")
    else: 
        print("Yay! Chocolate bar wins!")
        
        