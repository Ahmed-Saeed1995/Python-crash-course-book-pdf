try:
    with open("cats.txt") as cat_list:
        cats = cat_list.read()
        print(cats)

    with open("dogs.txt","r") as dog_list:
        dogs = dog_list.read()
        print(dogs)

except FileNotFoundError:
    pass
    # print("There`s file missing here !, please check beck the correct directory")
