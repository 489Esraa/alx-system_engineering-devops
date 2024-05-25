#!/usr/bin/python3
"""write with the json format"""
import json
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and
    #   convert the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the
    #   given user ID and convert the response to a JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        task = {
            user_id: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": username,
                    }
                    for t in todos  
            ]    
        }
        json.dump(task, jsonfile)
    