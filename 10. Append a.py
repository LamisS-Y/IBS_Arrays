# - Create a variable named `animals`
#   with the following content:
#   `["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr", "gorill",
#    "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "pirahn"]`
#
# - Add all elements an `"a"` at the end

animals = ["koal", "pand", "zebr", "anacond", "bo", "chinchill", "cobr", "gorill", "hyen", "hydr", "iguan", "impal", "pum", "tarantul", "pirahn"]
animals_with_a = []
for each_animal in animals: #it needs to be tols that a is added to each element of the list
    animals_with_a.append(each_animal+"a")
print(animals_with_a)