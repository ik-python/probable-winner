#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from src.domain.euromillions.rules import Rules
from src.domain.euromillions.compute import Compute

# import argparse

from src import utils

FORMAT = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%d-%b-%y %H:%M",)
logging.getLogger("winner").setLevel(logging.INFO)

history_file = "assets/history/eu-1617.csv"


if __name__ == "__main__":
    logging.info("lets check for a winner")
    numbers = utils.read_csv(file=history_file, depth=9)
    for n in numbers:
        logging.info(n)

    rules = Rules()
    cmp = Compute(rules, numbers)

    cmp.compute()
