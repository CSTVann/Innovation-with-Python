population_a = (100, 150, 230, 120, 180, 100 ,140, 95, 81, 21,4)
population_b = (300, 420,530,420,400,300,40,5,1,1,1)

oldA = sum(population_a[7:])#[7:] its mean take from index 7 to end (95, 81, 21,4)
oldB = sum(population_b[7:])


sumA, sumB = sum(population_a), sum(population_b)

oldRateA, oldRateB = oldA/sumA, oldB/sumB

print('The degrees of aging in town A and B are {:5.3f} and {:5.3f} respectively'.format(oldRateA,oldRateB))