#!/usr/bin/python3
"""Python script to export data in the csv format"""
import requests
import csv
import sys


def export_tasks_to_csv(employee_id):
    """A function that takes in employee id and fetches data
    into csv file related to that employee
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching todos: HTTP {todos_response.status_code}")
        return
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print(f"Error fetching users: HTTP {users_response.status_code}")
        return

    user = next(
        (user for user in users_response.json() if user['id'] ==
         employee_id),
        None
    )
    if not user:
        print(f"User with ID {employee_id} not found.")
        return

    tasks = [
        task for task in todos_response.json()
        if task['userId'] == employee_id
    ]
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )
        for task in tasks:
            writer.writerow([
                employee_id,
                user['username'],
                task['completed'],
                task['title']
            ])

    print(f"Tasks exported to {csv_file_name}")


if len(sys.argv) > 1:
    try:
        employee_id = int(sys.argv[1])
        export_tasks_to_csv(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
else:
    print("Usage: python3 script.py <employee_id>")
