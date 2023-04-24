#!/usr/bin/python3
# Python script that, using this REST API, for a given employee ID, returns
# information about his/her TODO list progress.
import requests
import sys


def display():
    # Fetching the employee name
    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    try:
        employee_name = requests.get(user_url).json()['name']
    except KeyError:
        print(f"Invalid employee ID: {sys.argv[1]}")
        return

    # Fetching the employee's todo list
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
    todo_data = requests.get(todo_url).json()

    # Extracting completed tasks and their titles
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    task_titles = [task['title'] for task in completed_tasks]

    # Displaying the progress report
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{len(todo_data)}):")
    print('\n'.join([f"\t{title}" for title in task_titles]))


if __name__ == "__main__":
    display()
