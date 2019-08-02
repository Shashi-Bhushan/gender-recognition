#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import numpy as np
import pandas as pd


def combine_url_by_comma(row):
    splitted_row = row.split(',')

    return [splitted_row[0], "%2C".join(splitted_row[1:])]


def read_dataset():
    with open('dataset/UserIdToUrl/part-00000', 'r') as input_file:
        file_split: List[str] = input_file.read().split()

        return list(map(combine_url_by_comma, file_split))


def clean_dataset(dataset):
    print(dataset[0:10])


if __name__ == '__main__':
    dataset = read_dataset()

    clean_dataset(dataset)