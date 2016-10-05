import random
# Modify the word jumble with a list of at least 15 words on a different topic,
# change the directions to tell the user what the topic is,
# and make it so the user has to keep guessing till they get it right.

# created U.S. states, single words, no spaces

state = ["Alabama", "California", "Alaska", "Connecticut", "Colorado", "Iowa", "Florida", "Georgia",
         "Indiana", "Kentucky", "Massachusetts", "Montana", "Oklahoma", "Vermont", "Wyoming", "Minnesota",
         "Nevada", "Oregon", "Pennsylvania", "Washington", "Illinois", "Tennessee", "Nebraska", "Texas"]
# converted states to all caps

states = [element.upper() for element in state]

# variables

selection = random.choice(states)
answer = selection
jumble = list(selection)

# instructions to player

print("This is a jumble of U.S. states. Try to guess the state, the game will continue until the correct answer is given, Good Luck. \n")

# scramble the letters

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,
print "\n"

# user inputs, continue guessing until answered correctly
# converts any answer given to all caps

guess = raw_input("What is the name of the state? \n")
guess = guess.upper()
if guess == answer:
    print("That is correct!!")
while guess != answer:
    print ("Incorrect, try again!! ")
    guess = raw_input("\nWhat is the name of the state? \n")
    guess = guess.upper()
    if guess == answer:
        print ("That is correct!!")
