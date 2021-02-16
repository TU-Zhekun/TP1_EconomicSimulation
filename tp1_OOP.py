# https://github.com/TU-Zhekun/TP1_EconomicSimulation

from abc import ABC, abstractmethod
import numpy
import random

namelist = range(1000)
person_dict = dict.fromkeys(namelist, 0)


class PopInitialization():
    # start with an uniform initialization (every individual has the same wealth)
    def initialization(self, namelist, wealth):
        person_dict = dict.fromkeys(namelist, wealth)
        return person_dict


class PopInteraction():
    # pick two individual randomly among the population
    def interaction(self, person_dict):
        person = random.sample(person_dict.keys(), 2)
        return person


class PopTransaction():
    def transaction(self, person, person_dict):
        sum = person_dict[person[0]] + person_dict[person[1]]
        person_dict[person[0]] = numpy.random.randint(0, sum)
        person_dict[person[1]] = sum - person_dict[person[0]]
        return person_dict


# ===============================================================
class IInitialization(ABC):
    @abstractmethod
    def initialization(self, namelist, wealth):
        person_dict = dict.fromkeys(namelist, wealth)
        return person_dict


class IInteraction(ABC):
    @abstractmethod
    def interaction(self, person_dict):
        person = random.sample(person_dict.keys(), 2)
        return person


class ITransaction(ABC):
    @abstractmethod
    def transaction(self, person, person_dict):
        sum = person_dict[person[0]] + person_dict[person[1]]
        person_dict[person[0]] = numpy.random.randint(0, sum)
        person_dict[person[1]] = sum - person_dict[person[0]]
        return person_dict


# ===============================================================
class Initialization(IInitialization):
    def initialization(self, namelist, wealth):
        person_dict = dict.fromkeys(namelist, wealth)
        return person_dict

    def initialization2(self, namelist, wealth):
        for name in namelist:
            person_dict[name] = random.randint(0, 1000000)
        return person_dict


class Interaction(IInteraction):
    def interaction(self, person_dict):
        person = random.sample(person_dict.keys(), 2)
        return person


class Transaction(ITransaction):
    def transaction(self, person, person_dict):
        sum = person_dict[person[0]] + person_dict[person[1]]
        person_dict[person[0]] = numpy.random.randint(0, sum)
        person_dict[person[1]] = sum - person_dict[person[0]]
        return person_dict

    def transaction2(self, person, person_dict):
        person_dict[person[0]] = person_dict[person[0]] + person_dict[person[1]]
        person_dict[person[1]] = 0
        return person_dict


# =====================================================
class Calculator():
    def ascendingDictByValue(self, list):
        return dict(sorted(list.items(), key=lambda data: data[1]))

    def giniFormula(self, listWealth):
        n = len(listWealth)
        up = down = 0
        for i in range(n):
            up += (i + 1) * listWealth[i]
            down += listWealth[i]
        up = 2 * up
        down = n * down
        G = up / down - (n + 1) / n
        return G

    def G(self, dict):
        return self.giniFormula(list(self.ascendingDictByValue(dict).values()))

trans = Transaction()
inter = Interaction()
init = Initialization()
cal = Calculator()

person_dict = init.initialization2(namelist, 1000000)

print(person_dict)
print("111111111111111111111111111")
for i in range(10000):
    a = inter.interaction(person_dict)
    trans.transaction2(a, person_dict)

print(person_dict)
G = cal.G(person_dict)
print(G)
