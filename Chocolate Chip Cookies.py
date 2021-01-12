from kitchen import Rosemary
from kitchen.utensils import Bowl, Oven, Plate,BakingTray, Fridge
from kitchen.ingredients import Sugar, Egg, Flour, ChocolateChips, BakingPowder, Butter,Salt


butter = Butter.take('one part')
sugar = Sugar.take(grams=200)
salt = Salt.take('pinch')
flour = Flour.take(grams=300)
chocolate_chips = ChocolateChips.take(grams=200)
baking_soda = BakingPowder.take('some')
tray = BakingTray
fridge = Fridge

bowl = Bowl.use(name = 'cookie batter')
bowl.add(butter)
bowl.add(sugar)
bowl.mix()
bowl.add(salt)
bowl.add(flour)
bowl.add(chocolate_chips)
bowl.add(baking_soda)
bowl.mix()

tray = BakingTray.use(name= 'cookies')
tray.add(bowl.take())

oven = Oven.use(175)
oven.preheat(degrees=175)
oven.add(tray)
oven.bake(minutes=10)

plate = Plate.use()
plate.add(tray.take())
Rosemary.serve(plate)

