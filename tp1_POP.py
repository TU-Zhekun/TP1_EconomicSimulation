import random
from abc import ABC, abstractmethod

import numpy

namelist = range(1000)
person_dict = dict.fromkeys(namelist, 0)


# start with an uniform initialization (every individual has the same wealth)
def initialization(namelist, wealth):
    person_dict = dict.fromkeys(namelist, wealth)
    return person_dict


# pick two individual randomly among the population
def interaction(person_dict):
    person = random.sample(person_dict.keys(), 2)
    return person


def transaction(person, person_dict):
    sum = person_dict[person[0]] + person_dict[person[1]]
    person_dict[person[0]] = numpy.random.randint(0, sum)
    person_dict[person[1]] = sum - person_dict[person[0]]
    return person_dict


def ascendingDictByValue(list):
    return dict(sorted(list.items(), key=lambda data: data[1]))


def giniFormula(listWealth):
    n = len(listWealth)
    up = down = 0
    for i in range(n):
        up += (i + 1) * listWealth[i]
        down += listWealth[i]
    up = 2 * up
    down = n * down
    G = up / down - (n + 1) / n
    return G


def G(dict):
    return giniFormula(list(ascendingDictByValue(dict).values()))


person_dict = initialization(namelist, 1000000)

print("-----initial dict:")
print(person_dict)
for i in range(10000):
    transaction(interaction(person_dict), person_dict)

print("-----dict after simulation:")
print(person_dict)

print("-----dict sorted by Value:")
print(dict(sorted(person_dict.items(), key=lambda data: data[1])))

print("-----sorted values of dict as list")
print(ascendingDictByValue(person_dict).values())
print("+++\n-----Gini Parameter:")
print(G(person_dict))
