#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)
    name = response.json().get("username")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    response = requests.get(url)
    tasks = response.json()
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": name} for task in tasks]
    data = {argv[1]: tasks}
    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump(data, jsonfile)
