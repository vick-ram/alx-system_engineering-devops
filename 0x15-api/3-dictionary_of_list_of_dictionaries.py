#!/usr/bin/python3
"""Script to export data in the json format"""
import requests
import json


def export_all_tasks_to_json():
    """Function to export data to json"""
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

    tasks_by_user = {}

    for task in todos_response.json():
        user_id = task['userId']
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []
        tasks_by_user[user_id].append({
            "username": next(
                user['username'] for user in users_response.json()
                if user['id'] == user_id
            ),
            "task": task['title'],
            "completed": task['completed']
        })

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(tasks_by_user, json_file, indent=4)

    print(f"Tasks exported to {json_file_name}")


export_all_tasks_to_json()
