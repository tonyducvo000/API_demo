import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_users = {}

for todo in todos:
    if todo['completed']:
            try:  #add count if task completed
                todos_by_users[todo['userId']] += 1
            except KeyError:
                #KeyError - initialize if userId not found in todos_by users
                todos_by_users[todo['userId']] = 1

#sort the data, users with most completed task will appear first
top_users = sorted(todos_by_users.items(), key=lambda x: x[1], reverse=True)

#get the highest number of completed task
max_complete = top_users[0][1]

users = []
#get other users who have the same number of completed tasks as max_complete
for user, num_complete in top_users:
        if num_complete < max_complete:
                break
        users.append(str(user))

#feed users list into .join function.
max_users = " and ".join(users)

print(f"user(s) {max_users} completed {max_complete} TODOs")

#take in the raw json payload and filter out
#the users with most completed tasks
def keep(todo):
    is_complete = todo["completed"]
    is_max = str(todo["userId"]) in users
    return is_complete and is_max

with open("filtered.json", "w") as data_file:
    # apply keep function to each item in todos.  This is done by using filter() function
    # and store it as list using list() function
    filtered = list(filter(keep, todos))
    json.dump(filtered, data_file, indent=2)  #write resultant filtered data out to a json file.



