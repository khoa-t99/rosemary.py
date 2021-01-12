from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, Plate,BakingTray, Fridge
from kitchen.ingredients import Sugar, Water, Flour, Salt, Butter, Apple, Lemon, Cornstarch, Cinnamon, Egg

flour = Flour.take(grams=300)
butter = Butter.take(grams=250)
sugar_1 = Sugar.take(grams=150)
sugar_2 = Sugar.take('spoon')
egg = Egg.take(1)
salt_1 = Salt.take('teaspoon')
salt_2 = Salt.take('pinch')
cornstarch = Cornstarch.take('spoonful')
water = Water.take(ml=200)
cinnamon = Cinnamon.take('teaspoon')


oven = Oven.use(180)
oven.preheat(degrees=180)

bowl_water = Bowl.use(name = 'chilled water')
bowl_water.add(water)

fridge = Fridge.use(degrees=4)
fridge.add(bowl_water)

bowl = Bowl.use(name = 'dough')
bowl.add(flour)
bowl.mix()
bowl.add(salt_1)
bowl.mix()
bowl.add(butter)
bowl.mix()
bowl.add(bowl_water.take())
bowl.mix()

fridge.add(bowl)


bowl_filling = Bowl.use(name = 'filling')
for i in range(6):
    apple = Apple.take()
    apple.peel()
    apple.slice()
    bowl_filling.add(apple)

lemon_1 = Lemon.take()
lemon_1.zest()
lemon_1.squeeze()
bowl_filling.add(lemon_1)
bowl_filling.add(sugar_1)
bowl_filling.add(cornstarch)
bowl_filling.add(salt_2)
bowl_filling.add(cinnamon)
bowl_filling.mix()

tray = BakingTray.use(name='Apple pie')
tray.add(bowl.take('3/4'))
tray.add(bowl_filling.take('1'))
tray.add(bowl.take('1/4'))

bowl_egg = Bowl.use(name='egg wash')
egg = Egg.take()
egg.crack()
bowl_egg.add(egg)
bowl_egg.mix()

lemon_2 = Lemon.take()
lemon_2.zest()

tray.add(bowl_egg.take())
tray.add(sugar_2)
tray.add(lemon_2)

oven = Oven.use(180)
oven.preheat(degrees=180)
oven.add(tray)
oven.bake(minutes=60)

plate = Plate.use()
plate.add(tray.take())
Rosemary.serve(plate)








