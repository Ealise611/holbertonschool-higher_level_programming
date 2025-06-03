#!/usr/bin/python3
"""
this module do serialization to convert CSV to JSON format
"""

import csv
import json


def convert_csv_to_json(filename):
    with open('input.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
    with open('output.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
