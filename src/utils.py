# -*- coding: utf-8 -*-

import os
import csv

from .models.numbers import Numbers


def printer(txt):
    print(txt)


def read_csv(file, depth=1):
    count = 0
    result = []
    with open(f"{os.getcwd()}/{file}", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(
                Numbers.factory(
                    {"date": row["DrawDate"], "balls": row["Ball 1"], "draw": row["DrawNumber"],}
                )
            )
            count += 1
            if count >= depth:
                break
    return result
