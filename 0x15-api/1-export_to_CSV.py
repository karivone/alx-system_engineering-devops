#!/usr/bin/python3
#extend your Python script to export data in the CSV format
import csv
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

    # Writing data to CSV file
    filename = f"{sys.argv[1]}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                'USER_ID': task['userId'],
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    # Displaying the progress report
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{len(todo_data)}):")
    print('\n'.join([f"\t{task['title']}" for task in completed_tasks]))
    print(f"\nTask data exported to {filename}")

if __name__ == "__main__":
    display()

