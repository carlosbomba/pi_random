#trying out code from Joma Techs video

import random

def pi_random(n):
  point_inside = 0
  point_total = 0
  for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x**2 + y**2
    if distance <= 1:
      point_inside += 1
    point_total +=1
  return 4 * point_inside/point_total