#!/usr/bin/python3
"""Python script to export data in the json format"""
import json
import requests
import sys


def export_tasks_to_json(employee_id):
    """takes employee id and returns todos in json"""
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

    tasks_data = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        } for task in tasks
    ]

    json_file_name = f"{employee_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump({str(employee_id): tasks_data}, json_file, indent=4)

    print(f"Tasks exported to {json_file_name}")


if len(sys.argv) > 1:
    try:
        employee_id = int(sys.argv[1])
        export_tasks_to_json(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
else:
    print("Usage: python3 script.py <employee_id>")
