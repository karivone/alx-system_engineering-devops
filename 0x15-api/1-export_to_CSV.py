#!/usr/bin/python3
'''
Gather data from an API
Export data in the CSV format
'''

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        task_data = [
                {
                    "userId": user_id,
                    "username": username,
                    "completed": task.get("completed"),
                    "title": task.get("title")
                }
                for task in todos
        ]
        writer.writerows(task_data)
