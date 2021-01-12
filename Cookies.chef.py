from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, BakingTray, Oven 
from kitchen.ingredients import Butter, Egg, Salt, Flour, BakingPowder,Sugar, ChocolateChips

#First: Preheat the oven
oven=Oven.use()
oven.preheat(degrees=175)

#take a bowl
bowl = Bowl.use(name='batter')

#Mix sugar and Butter in little bits at a time
for i in range(4):
    butter= Butter.take(grams= 50)
    sugar = Sugar.take(grams=50)
    bowl.add(sugar)
    bowl.add(sugar)
    bowl.mix()

#Once this is smooth add the eggs seperately
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()

#And for flavor:salt
bowl.add (Salt.take(' a pinch'))

#I'm mixing the dry ingredients seperate bowl
bowl2=Bowl.use(name='dry contents')
flour= Flour.take(grams=300)
chocolate = ChocolateChips.take (grams=200)
bakingpowder = BakingPowder.take ('some')
bowl2.add(flour)
bowl2.add(chocolate)
bowl2.add (bakingpowder)
bowl2.mix()

#Now add wet and dry together
for i in range (5):
    bowl.add (bowl2.take('1/5'))
    bowl.mix()

#Let's try that batter!
Rosemary.taste(bowl)

#put generous scoopfuls of batter on the baking tray, making sure to keep distance!
tray = BakingTray.use('Cookies')
for i in range (16):
    tray.add(bowl.take('1/16'))

oven.add(tray)
oven.bake(minutes=10)

#Now serve!
plate = Plate.use()
cookies = tray.take()
plate.add(cookies)

#But wait for them to cool down!
Rosemary.serve(plate)
#Eet smakelijk!