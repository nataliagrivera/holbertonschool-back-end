#!/usr/bin/python3
"""Using employee ID returns information about his/her TODO list progress"""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    user_id = argv[1]  # Retrieve user ID from command line arguments
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response_user = requests.get(url_user)  # Get the user information from API
    user_info = response_user.json()  # Convert user information to JSON format
    name = user_info.get("name")  # Get the name of the user

    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response_tasks = requests.get(url_tasks)  # Get tasks information for user
    tasks = response_tasks.json()  # Convert tasks information to JSON format
    completed_tasks = [task for task in tasks if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

    # Create CSV file with user tasks information
    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME',
                         'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in tasks:
            task_completed_status = "Completed" if task.get(
                "completed") else "Not Completed"
            writer.writerow([user_id, name,
                             task_completed_status, task.get("title")])

    print(f"Tasks information exported to {csv_file_name} successfully.")
