#!/usr/bin/python3

'''Gather data from an API'''

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    done_tasks = []
    for task in todos:
        if task.get("completed"):
            done_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
              user.get("name"), len(done_tasks), len(todos)))
    print("\n".join("\t {}".format(task) for task in done_tasks))
