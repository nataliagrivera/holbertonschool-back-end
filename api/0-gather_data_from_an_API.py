#!/usr/bin/python3
"""With employee ID, returns information about his/her TODO list"""
import requests
from sys import argv

if __name__== "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url) # Get the response from the API for the user_id
    json_response = response.json() # Convert the response to JSON format
    name = json_response.get("name") # Get the name of the user
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    response = requests.get(url) # Get the response from the API for the user_id
    json_response = response.json() # Convert the response to JSON format
    tasks = []
    for task in json_response:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, len(tasks), 
                                                          len(json_response)))
    