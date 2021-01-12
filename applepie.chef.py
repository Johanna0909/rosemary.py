from kitchen.ingredients.Ingredient import Sugar
from kitchen import Rosemary
from kitchen.utensils import Oven, Bowl, PieDish, Fridge, Plate
from kitchen.ingredients import Butter, Egg, Salt, Water, Flour, Milk, Apple, Lemon, Cinnamon, Cornstarch

#To have some cold water, we need to put it in the fridge
fridge = Fridge.use(degrees=5)
water= Water.take(ml=100)
water_bowl= Bowl.use(name='water')
water_bowl.add(water)
fridge.add(water_bowl)

#Not forget to preheat the oven already
oven=Oven.use()
oven.preheat(degrees= 180)

#Let's get to mixing
bowl = Bowl.use(name='dough')
bowl.add(Flour.take(grams=300))
bowl.add(Salt.take('a teaspoon'))
bowl.mix()

#gradually knead in the butter
for i in range (5):
    bowl.add(Butter.take(grams=50))
    bowl.mix()

#Now we'll gradually add the water from the fridge to the dough, while still mixing
cold__water = fridge.take()
for i in range (10):
    bowl.add(cold__water.take('1/10'))
    bowl.mix()

#The dough now needs to rest in the fridge
fridge.add(bowl)

#While it is chilling, we prepare the filling
#We start by peeling and slicing the apples
for apple in Apple.take(6):
    apple.peel()
    apple.slice()

#Then get zest and juice from a lemon
lemon=Lemon.take()
lemon_bowl=Bowl.use ('Lemon Zest and Juice')
lemon_zest= lemon.zest()
lemon_bowl.add(lemon_zest)
lemon_juice= lemon.squeeze()
lemon_bowl.add (lemon_juice)

#And put the filling together
bowl2=Bowl.use()
bowl2.add(apple)
bowl2.add(Sugar.take(grams=150))
bowl2.add(Cornstarch.take('a spoonful'))
bowl2.add(Salt.take('a pinch'))
bowl2.add (Cinnamon.take('a teaspoon'))
bowl2.add(lemon_bowl.take('1/2'))

#Let Rosemary try this wonderful mixture
Rosemary.taste(bowl2)

#let's put it all together! First the pie dough:
pie_dough= fridge.take()
dish=PieDish.use(name='Apple Pie')
dish.add(bowl.take('3/4'))
#Then the filling:
dish.add(bowl2.take())
#And a nice cover of pie dough again
dish.add(bowl.take('1/4'))

#A nice eggwash for a nice crust
bowl3=Bowl.use('Eggwash')
egg=Egg.take()
egg.crack()
bowl3.add(egg)
bowl3.add(Sugar.take('a spoonful'))
#we are now adding both the zest and the juice, it gives more flavor!
bowl3.add(lemon_bowl.take('1/2'))
bowl3.mix()

#Adding the eggwash on the pie
dish.add(bowl3.take())

#And in the oven it goes!
oven.add(dish)
oven.bake(minutes=60)

#Now serve the whole pie on one !
plate = Plate.use()
Apple_Pie = dish.take()
plate.add(Apple_Pie)

Rosemary.serve(plate)