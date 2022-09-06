from math import floor


def nb_year(p0, percent, aug, p):
    pop = p0
    for i in range(1, 200):
        pop = pop * (1+(percent/100)) + aug
        pop = floor(pop)
        if pop >= p:
            return i


print(nb_year(1500, 5, 100, 5000))
