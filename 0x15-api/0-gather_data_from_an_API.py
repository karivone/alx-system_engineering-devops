#!/usr/bin/python3
#Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

import requests
import sys

employee_id = sys.argv[1]

# Fetching the employee name
employee_url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
employee_data = requests.get(employee_url).json()

if 'name' in employee_data:
    employee_name = employee_data['name']
else:
    employee_name = 'Unknown'

# Fetching the employee's todo list
todo_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
todo_data = requests.get(todo_url).json()

# Counting the number of completed tasks
completed_tasks = [todo for todo in todo_data if todo['completed']]
num_completed_tasks = len(completed_tasks)
num_total_tasks = len(todo_data)

# Displaying the progress report
print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")
for task in completed_tasks:
    print(f"\t {task['title']}")

