#!/usr/bin/python3

'''
Gather data from an API
Export data in a JSON format file
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                  "task": task.get("title"),
                  "completed": task.get("completed"),
                  "username": username}
                   for task in todos]}, jsonfile)
