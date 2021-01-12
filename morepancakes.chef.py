from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk
import random


#take a bowl
bowl = Bowl.use(name='batter')
#here we can specify the number of servings of 8 pancakes we want (or let it be random!)
number= random.randint (1,10)
print(number)
print ('times a serving of 8 pancakes') 

#for that many pancakes we need a lot of batter!
for i in range(number):
    #whisk the eggs until frothy
    for egg in Egg.take(2):
        egg.crack()
        bowl.add(egg)
    bowl.mix()

    #Add a dash of salt
    bowl.add (Salt.take(' a dash'))

    #Mix in the flour in 50g batches
    for i in range(5):
        flour= Flour.take(grams= 50)
        bowl.add(flour)
        bowl.mix

    #Then add half the milk, mix, and then add the second half (does this actually do this?)
    for i in range(2):
        milk = Milk.take (ml=250)
        bowl.add(milk)
        bowl.mix
Rosemary.taste(bowl)

#Now it's time for baking!
pan = Pan.use(name='pancake')
for i in range(number):
    for i in range (8):
        pan.add(Butter.take('slice'))
        pan.add(bowl.take(f'1/{8*number}'))
        pan.cook(minutes=1)
        #flip it once golden brown
        pan.flip
        pan.cook(minutes=1)


#For the hungry ones: all the pancakes on one plate!
plate = Plate.use()
pancake = pan.take()
plate.add(pancake)

Rosemary.serve(pancake)
#Bon Appetit!