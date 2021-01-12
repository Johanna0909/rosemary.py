from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk

#take a bowl
bowl = Bowl.use(name='batter')

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
for i in range (8):
    pan.add(Butter.take('slice'))
    pan.add(bowl.take('1/8'))
    pan.cook(minutes=1)
    #flip it once golden brown
    pan.flip
    pan.cook(minutes=1)

    #If you only want single pancakes on your plate:
    #plate = Plate.use()
    #pancake = pan.take()
    #plate.add(pancake)

#For the hungry ones: 8 pancakes on one plate!
plate = Plate.use()
pancake = pan.take()
plate.add(pancake)

Rosemary.serve(plate)
#Eet smakelijk!