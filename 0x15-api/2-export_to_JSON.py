#!/usr/bin/python3
#extend your Python script to export data in the JSON format.
import requests
import json
import sys

def get_employee_todo_list(employee_id):
    # Get employee name
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    employee_name = response.json().get('name')

    # Get employee todo list
    response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))
    todo_list = response.json()

    # Create JSON object
    json_data = {
        str(employee_id): [
            {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": employee_name
            } for todo in todo_list
        ]
    }

    # Write to file
    with open('{}.json'.format(employee_id), 'w') as f:
        json.dump(json_data, f)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        get_employee_todo_list(employee_id)
    else:
        print('Usage: python {} EMPLOYEE_ID'.format(sys.argv[0]))

