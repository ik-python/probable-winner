# -*- coding: utf-8 -*-

import random

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
        stars = set()
        for e in self.numbers:
            for n in e.numbers:
                numbers.add(n)
            for s in e.stars:
                stars.add(s)

        numberDiff = self.diff(self.rules.numbers, numbers)
        sampling = random.sample(numberDiff, k=5)
        sampling.sort()
        print(sampling)
        print(self.diff(numberDiff, sampling))
        # todo: remove values sampled

    # https://stackoverflow.com/questions/6486450/python-compute-list-difference
    def diff(self, l1, l2):
        # ll = lambda l1, l2: filter(lambda x: x not in l2, l1)
        # return ll(l1,l2)
        return set(l1) - set(l2)

    def __repr__(self):
        return f"numbers: {self.numbers}, rules: {self.rules}"
