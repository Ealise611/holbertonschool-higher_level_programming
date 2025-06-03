#!/usr/bin/python3
"""
this module do serialization to convert CSV to JSON format
"""

import csv
import json


def convert_csv_to_json(filename: str):
    """
    this function convert csv to json
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False
