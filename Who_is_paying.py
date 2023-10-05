import random  # need import for choosing randomly a name from a list.

names_string = input(
    "Nennen Sie mir bitte alle Namen, getrennt mit Komma. example: Apfel,Nana,... ")

# names is a list, inside them are names separated by ',' with the split() function
names = names_string.split(",")

# we need length of the list, for knowing what should be the random() upper-limit.
names_length = len(names)

randomChoice = random.randint(0, names_length-1)
# lists starts indexing from 0. - So names[0] = asd, ...
# but our randomChoice starts from 1. -> so we need to match indexing with random choosens number. This is why we use '-1' at the end of randint().

PayingPerson = names[randomChoice]
print(PayingPerson + " is going to buy the meal today!")


# just for testing purposes
print(randomChoice)
print(names_length)
print(names[3])
