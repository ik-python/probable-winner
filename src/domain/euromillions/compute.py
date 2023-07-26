# -*- coding: utf-8 -*-

import random

default_stars = {
    "1": 2,
    "2": 2,
    "3": 2,
    "4": 2,
    "5": 2,
    "6": 2,
    "7": 2,
    "8": 2,
    "9": 2,
    "10": 2,
    "11": 2,
    "12": 2,
}

# different strategies
# 1. Brute Force
# - remove all values that use to be there
# - randomly pick new values
# - 1. from each dozen
# - 2. randomize
# - 3. based on percentage from previous runs
class Compute:
    def __init__(self, rules, numbers):
        self.rules = rules
        self.numbers = numbers

    def compute(self):
        numbers = set()

        print(self.numbers)

        for e in self.numbers:
            for n in e.numbers:
                numbers.add(n)
            for s in e.stars:
                if s in default_stars:
                    if default_stars.get(s) > 1:
                        default_stars[s] -= 1
                    else:
                        del default_stars[s]

        numberDiff = self.diff(self.rules.numbers, numbers)
        sampling = random.sample(numberDiff, k=5)
        sampling.sort()
        vals = self.diff(numberDiff, sampling)
        result = filter(lambda x: x > 4 and x < 47, vals)
        result = list(result)
        result.sort()
        print(result)
        self.calc_stars(default_stars)

    def calc_stars(self, values):
        result = list()
        for k, v in values.items():
            if v == 1:
                result.append(k)
            if v == 2:
                result.append(k)
        print(result)

    # https://stackoverflow.com/questions/6486450/python-compute-list-difference
    def diff(self, l1, l2):
        # ll = lambda l1, l2: filter(lambda x: x not in l2, l1)
        # return ll(l1,l2)
        return set(l1) - set(l2)

    def __repr__(self):
        return f"numbers: {self.numbers}, rules: {self.rules}"
