from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Plate
from kitchen.ingredients import Flour, Egg, Milk, Salt, Butter



salt = Salt.take('pinch')

bowl = Bowl.use(name = 'eggs')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()

bowl.add(salt)

bowl = Bowl.use(name = 'eggs')
for i in range(5):
    flour = Flour.take(grams=50)
    bowl.add(flour)
bowl.mix()


for i in range(2):
    milk = Milk.take(ml=250)
    bowl.add(milk)
bowl.mix()

pan = Pan.use(name='pancakes')
for i in range(8):
    pan.add(Butter.take('slice'))
    pan.add(bowl.take('1/8'))
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)
pancakes = pan.take()

plate = Plate.use()
plate.add(pancakes)
Rosemary.serve(plate)


