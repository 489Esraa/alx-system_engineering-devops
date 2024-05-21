#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


def get_user_name(user_id):
    """Get the list of users"""
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "users"
    """Format the url"""
    url_to_call = f"{url}/{endpoint}/{user_id}"
    """Get the response"""
    response = requests.get(url_to_call)
    json_response = response.json()
    return json_response


def get_user_todos(user_id):
    """Get the list of todos"""
    url = "https://jsonplaceholder.typicode.com"
    endpoint = "todos"
    """Format the url"""
    url_to_call = f"{url}/users/{user_id}/{endpoint}"
    """Get the response"""
    response = requests.get(url_to_call)
    json_response = response.json()
    return json_response


if __name__ == "__main__":
    """Get User TODOS"""
    user_id = sys.argv[1]
    user = get_user_name(user_id)
    user_todos = get_user_todos(user_id)
    user_name = user.get("name")
    total_tasks = len(user_todos)
    completed_tasks_list = list(map(lambda x: x.get("completed"), user_todos))
    completed_tasks = completed_tasks_list.count(True)
    print(f"Employee {user_name} is done with "
          f"tasks({completed_tasks}/{total_tasks}):")
    for task in user_todos:
        if task.get("completed"):
            print(f"\t {task.get('title')}")