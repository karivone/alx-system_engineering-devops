#!/usr/bin/python3
'''
extend your Python script
export data in the JSON format
'''
import json
import requests


if __name__ == '__main__':
    url_base = 'https://jsonplaceholder.typicode.com'
    users_url = url_base + '/users'
    todos_url = url_base + '/todos'

    # Get all users
    response = requests.get(users_url)
    users = response.json()

    # Get all todos
    response = requests.get(todos_url)
    todos = response.json()

    # Group todos by user
    todos_by_user = {}
    for todo in todos:
        user_id = todo['userId']
        if user_id not in todos_by_user:
            todos_by_user[user_id] = []
        todos_by_user[user_id].append(todo)

    # Create JSON object
    todo_list = {}
    for user in users:
        user_id = user['id']
        todo_list[user_id] = []
        for todo in todos_by_user[user_id]:
            todo_item = {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            todo_list[user_id].append(todo_item)

    # Write JSON to file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(todo_list, file)
