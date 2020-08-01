# -*- coding: utf-8 -*-


class Numbers:
    def __init__(self, dct):
        self.date = dct["date"]
        self.numbers = dct["balls"]
        self.stars = dct["stars"]
        self.draw = dct["draw"]

    def factory(dct):
        return Numbers(dct)

    def __repr__(self):
        return f"date: {self.date}, draw: {self.draw}, numbers: {self.numbers}, stars: {self.stars}"
