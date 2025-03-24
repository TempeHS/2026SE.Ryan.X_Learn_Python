num = [1, 2, 3]


for x in num:
    for y in num:
        if x != y:
            for z in num:
                if z != x and y !=z:
                    print(x, y, z)