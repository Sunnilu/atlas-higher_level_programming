#!/usr/bin/python3
'''load from json'''
import json

def load_from_json_file(filename):
    '''creates an objec from a JSON file'''
    with open(filename, 'r') as file:
        return json.load(file)
