#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import logging
import argparse

FORMAT = '%(asctime)-15s %(name)s %(levelname)-8s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logging.getLogger('winner').setLevel(logging.INFO)


def read_file(file):
    pass


if __name__ == '__main__':
    print('test')
