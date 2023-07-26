# -*- coding: utf-8 -*-

from enum import Enum
from datetime import datetime

class DayOfWeek(Enum):
    TUESDAY = 1
    FRIDAY = 4

class Numbers:
    def __init__(self, source):
        date = source["date"]
        self.date = date
        self.numbers = source["balls"]
        self.stars = source["stars"]
        self.draw = source["draw"]
        # https://pynative.com/python-get-the-day-of-week/
        self.day_of_week = DayOfWeek(datetime.strptime(date, "%d-%b-%Y").weekday()).name

    def factory(dct):
        return Numbers(dct)

    def __repr__(self):
        return f"date: {self.date}, draw: {self.draw}, numbers: {self.numbers}, stars: {self.stars}. day of week: {self.day_of_week}"
