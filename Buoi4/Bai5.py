l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l1 = [j for i in l for j in (i if isinstance(i, list) else [i])]
print(l1)
