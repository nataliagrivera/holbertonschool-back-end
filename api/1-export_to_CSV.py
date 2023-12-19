#!/usr/bin/python3
"""Using employee ID returns information about his/her TODO list progress"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)  # Get the response from the API
    name = response.json().get("name")  # Get the name of the user
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    # Get the response from the API for the user_id from the argv
    response = requests.get(url)
    tasks = response.json()  # Get the tasks of the user
    with open("{}.csv".format(argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:  # Write the tasks in the CSV file
            writer.writerow([argv[1], name, task.get("completed"),
                            task.get("title")])  # Write the row
