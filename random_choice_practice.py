# Import the random module to use its choice selection capabilities.
# Create a list of participant names, including 'Alex'.
# Use a while loop to repeatedly draw a name randomly from the list of participants.
# The loop should only terminate when 'Alex' is drawn.
# Ensure that the loop does not produce any output until 'Alex' is drawn.

"""
import random

names = ['Alex', 'Drew', 'Franklin', 'Ralphy', 'Higgins']

while 'Alex' not in random.choices(names, k=1):
    pass
print("Congratulations, Alex! You've won the lucky draw!")
 """
 
 # Import the random module to utlitze its random selection feature.
 # Define a list of directions that the entity can take.
# Use a for loop to simulate 10 steps.
# In each iteration, randomly select a direction and simulate taking a step in the direction.
# Print out the direction of each step.

"""
import random 

directions = ['West', 'East', 'North', 'South']

for step in range(10):
    step_direction = random.choice(directions)
    print(f"Step {step + 1}: The entity moves 10 steps to the {step_direction}")
"""

"""
import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1}, Dice2 {dice2}")
    if dice1 == dice2:
        print(f"Both dice landed on {dice1}.")
        break
"""

# Use the random.shuffle() method to randomize the list of questions.
# Use a for loop to iterate through the shuffled list and present each question.
# Print out each question to the user.

import random

questions = ['What is 1 + 1?', 'What is your favorite color?', 'What is your name?']

random.shuffle(questions)
for x in questions:
    print(x)
