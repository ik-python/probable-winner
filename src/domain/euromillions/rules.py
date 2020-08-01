# -*- coding: utf-8 -*-


class Rules:
    def __init__(self):
        self.numbers = list(range(1, 51))
        self.stars = list(range(1, 13))

    def __repr__(self):
        return f"numbers: {self.numbers}, stars: {self.stars}"
