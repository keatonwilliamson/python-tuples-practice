print("")
print("")

# 1. Create a tuple named zoo that contains 10 of your favorite animals.
# 2. Find one of your animals using the tuple.index(value) syntax on the tuple.

animals = ("dog", "cat", "fish", "dolphin", "wombat", "lizardman", "fishbat", "snake", "africansnowfrog", "worm")
print(animals.index("fish"))

# 3.Determine if an animal is in your tuple by using value in tuple syntax.

animal_to_find = "dolphin"
if animal_to_find in animals:
    print(animals[animals.index(animal_to_find)])
    # Print that the animal was found

# 4. You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"
# Create a variable for the animals in your zoo tuple, and print them to the console.

(barkDude, kitty, swimmy, bigSwimmy, idk, yeah, notReal, dangerWorm, defNotReal, real) = animals
print(dangerWorm)

# 5. Convert your tuple into a list.
animalList = list(animals)
for animal in animalList:
    print(animal)
print()
    
# 6. Use extend() to add three more animals to your zoo.
animalList.extend(["kangaroo", "spider", "eagle"])
for animal in animalList:
    print(animal)

# 7. Convert the list back into a tuple.
animalTuple = tuple(animalList)
print(animalTuple)





