# -*- coding: utf-8 -*-

import os
import csv

from .domain.euro_millions.numbers import Numbers


def printer(txt):
    print(txt)


# TODO: utils not necessary should know about Numbers
def read_csv(file, depth=1):
    result = []
    with open(f"{os.getcwd()}/{file}", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # This should model specific
            balls = [
                int(row["Ball 1"]),
                int(row["Ball 2"]),
                int(row["Ball 3"]),
                int(row["Ball 4"]),
                int(row["Ball 5"]),
            ]
            stars = [row["Lucky Star 1"], row["Lucky Star 2"]]

            result.append(
                Numbers.factory(
                    {
                        "date": row["DrawDate"],
                        "balls": balls,
                        "draw": row["DrawNumber"],
                        "stars": stars,
                    }
                )
            )
            depth -= 1
            if depth <= 0:
                break
    return result
