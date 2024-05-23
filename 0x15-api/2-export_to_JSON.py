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
                        "username": username
                    }
                    for t in todos  
            ]    
        }
    json.dump(task, jsonfile)
"""

export json format
{ "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
 {"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json


export in CSV as : "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
USER_ID.csv




Employee *NAME* is done with tasks(*DONE*/*TOTAL*):
     *TITLE*
     *TITLE*
     *TITLE*


https://jsonplaceholder.typicode.com/users?id=1
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
https://jsonplaceholder.typicode.com/todos?userId=5
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  ]

https://jsonplaceholder.typicode.com/todos?userId=5&completed=true
https://jsonplaceholder.typicode.com/todos?userId=5&completed=false
  """