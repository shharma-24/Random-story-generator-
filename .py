import random

# Lists of words
names = ["Rahul", "Priya", "Aman", "Sneha", "Rohit"]
places = ["park", "school", "mall", "beach", "jungle"]
actions = ["dancing", "running", "singing", "jumping", "sleeping"]
things = ["pizza", "mobile", "dog", "car", "book"]

# Random selections
name = random.choice(names)
place = random.choice(places)
action = random.choice(actions)
thing = random.choice(things)

# Story generation
story = f"One day, {name} went to the {place}. There, he/she was {action} with a {thing}. Suddenly, something funny happened and everyone started laughing!"

# Output
print("\n🎉 Your Random Story:\n")
print(story)
