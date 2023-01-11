# Name: Jacob Summers
# Date: 10.31.22
# Course: 325 Section 400
# Assignment 5
# Description: Algorithm calculates the number of dogs that can be fed with a given number of treats.

def feedDog(hunger_level, buscuit_size):
    """Algorithm returns the total number of dogs that will be satisfied with given hunger levels and amount of food.
    Hunger levels of dogs are passed to function in list, with food values passed in different list."""
    hunger_level.sort()
    buscuit_size.sort()

    happy_pups = 0
    food_index = 0
    dog_index = 0
    dog_dinner = buscuit_size[food_index]

    while food_index < len(buscuit_size) and dog_index < len(hunger_level):
        if dog_dinner >= hunger_level[dog_index]:
            happy_pups += 1
            food_index += 1
            dog_index += 1
            if food_index < len(buscuit_size):
                dog_dinner = buscuit_size[food_index]

        else:
            food_index += 1
            if food_index < len(buscuit_size):
                dog_dinner += buscuit_size[food_index]

    return happy_pups


#hunger_level = [30]
#buscuit_size = [5,5,5,5,5]
#print(feedDog(hunger_level, buscuit_size))
