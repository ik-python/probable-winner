#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Compute numbers
## ./main.py --draw 1663

import argparse
import sys
import logging

from src.domain.euromillions.rules import Rules
from src.domain.euromillions.compute import Compute

from src import utils

FORMAT = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt="%d-%b-%y %H:%M",)
logging.getLogger("winner").setLevel(logging.INFO)

history_file = "assets/history/eu-{draw}.csv"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI to helm pick number for Euro Millions", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--draw', type=str, help="Select draw history.")
    parser.add_argument('--depth', default=6, type=int, help="Choose depth, number of draws.")
    parser.add_argument('--day', default=6, type=int, help="Choose day of a week.")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    logging.info(f'arguments >> {args}')

    logging.info("lets check for a winner")
    numbers = utils.read_csv(file=history_file.format(draw=args.draw), day='FRIDAY', depth= args.depth)

    rules = Rules()
    cmp = Compute(rules, numbers)

    cmp.compute()
