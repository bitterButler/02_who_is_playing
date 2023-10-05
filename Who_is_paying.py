import random  # need import for choosing randomly a name from a list.

names_string = input(
    "Nennen Sie mir bitte alle Namen, getrennt mit Komma. example: Apfel,Nana,... ")

# names is a list, inside them are names separated by ',' with the split() function
names = names_string.split(",")

# we need length of the list, for knowing what should be the random() upper-limit.
names_length = len(names)


print(names_length)
print(names[3])
