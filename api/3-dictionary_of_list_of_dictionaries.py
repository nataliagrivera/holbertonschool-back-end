#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    data = {}
    for user in users:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user.get("id"))
        response = requests.get(url)
        tasks = response.json()
        tasks = [{"task": task.get("title"),
                  "completed": task.get("completed"),
                  "username": user.get("username")} for task in tasks]
        data[user.get("id")] = tasks
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
