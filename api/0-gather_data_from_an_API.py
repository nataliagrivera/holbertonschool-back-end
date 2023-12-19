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
    
    completed = [task for task in tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(name, len(completed),
                                                          len(tasks)))
    for task in completed:
        print("\t {}".format(task.get("title")))
    