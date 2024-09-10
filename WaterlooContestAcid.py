acid = 250
water = 0
beaker = acid + water
acid_tank = 0

#Code for dilute#
def dilute(beaker, acid, water):
  water += 100
  beaker = acid + water
  return water, beaker

#Code for overflow
def overflow(beaker, acid, water):
  if beaker > 500:
    discarded = beaker - 500
    acid_percent = acid/beaker
    water_percent = water/beaker
    beaker = acid + water
    acid = acid - acid_percent*discarded
    water = water - water_percent*discarded
    beaker = acid + water
  return beaker, acid, water

#Acidize#
def acidize(beaker, acid, water):
  acid += 50  
  beaker = acid + water
  return acid, beaker

#Neutralize: Discards half the beaker and replaces said half with pure water.
def neutralize(beaker, acid, water):
  discarded = beaker/2
  if beaker>0:
    acid_percent = acid/beaker
    water_percent = water/beaker
    acid = acid - acid_percent*discarded
    water = water - water_percent*discarded
    beaker = acid + water
  return beaker, acid, water

#Extract
def extract(beaker, acid, water, acid_tank):
  acid_percent = acid/beaker
  water_percent = water/beaker
  
  acid_tank += beaker*acid_percent*0.1
  acid = acid - beaker*acid_percent*0.1
  water = water - beaker*water_percent*0.1
  beaker = acid + water
  return beaker, acid, water, acid_tank

#validate input
while True:
  num_runs = int(input())
  if num_runs>=1 and num_runs<=50:
    break
  else:
    print()

#Choose correct option
for x in range(num_runs):
  operation_chosen = input()

  if operation_chosen == "Dilute":
    water, beaker = dilute(beaker, acid, water)
    beaker, acid, water = overflow(beaker, acid, water)

    
  elif operation_chosen == "Acidize":
    acid, beaker = acidize(beaker, acid, water)
    beaker, acid, water = overflow(beaker, acid, water)


  elif operation_chosen == "Neutralize":
    beaker, acid, water = neutralize(beaker, acid, water)
    beaker, acid, water = overflow(beaker, acid, water)

  
  elif operation_chosen == "Extract":
    beaker, acid, water, acid_tank = extract(beaker, acid, water, acid_tank)
    beaker, acid, water = overflow(beaker, acid, water)


print(acid_tank)