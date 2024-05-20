#!/usr/bin/python3

"""
This script fetches TODO list data from a REST API
and displays the progress for a given employee
"""
import requests
import sys


def get_employee_tasks(employee_id):
    """Function that accepts employee id to get his/her
    related completed todos over total
    """
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Error fetching data: HTTP {response.status_code}")
        return

    tasks = [
        task for task in response.json()
        if task['userId'] == employee_id
    ]
    completed_tasks = [
        task for task in tasks if task['completed']
    ]
    users_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user_response = requests.get(users_url)
    employee_name = user_response.json().get('name', 'Unknown Employee')
    print(
        f"Employee {employee_name} is done with tasks("
        f"{len(completed_tasks)}/{len(tasks)}):"
    )
    for task in completed_tasks:
        print(f"\t {task['title']}")


if len(sys.argv) > 1:
    try:
        employee_id = int(sys.argv[1])
        get_employee_tasks(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
else:
    print("Usage: python3 script.py <employee_id>")
