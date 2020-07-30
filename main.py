#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# import argparse

from src import utils

FORMAT = "%(asctime)s %(name)s %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logging.getLogger("winner").setLevel(logging.INFO)

history_file = "assets/history/euromillions-draw.csv"


if __name__ == "__main__":
    logging.info("lets check for a winner")
    numbers = utils.read_csv(file=history_file, depth=5)
    for n in numbers:
        logging.info(n)
    numbers_balls = list(range(1, 49))
    numbers_stars = list(range(1, 12))

    print(numbers_balls)
    print(numbers_stars)
