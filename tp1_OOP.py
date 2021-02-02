from abc import ABC, abstractmethod
import numpy
import random

namelist = range(1000)
person_dict = dict.fromkeys(namelist, 0)


class VInitialization(ABC):
    # start with an uniform initialization (every individual has the same wealth)
    def initialization(self, namelist, wealth):
        person_dict = dict.fromkeys(namelist, wealth)
        return person_dict


class VInteraction(ABC):
    # pick two individual randomly among the population
    def interaction(self, person_dict):
        person = random.sample(person_dict.keys(), 2)
        return person


class VTransaction(ABC):
    def transaction(self, person, person_dict):
        sum = person_dict[person[0]] + person_dict[person[1]]
        person_dict[person[0]] = numpy.random.randint(0, sum)
        person_dict[person[1]] = sum - person_dict[person[0]]
        return person_dict

class Initialization(VInitialization):
    pass

class Interaction(VInteraction):
    pass

class Transaction(VTransaction):
    pass

