import uuid, requests, json
from datetime import timedelta, date

file = open("token.txt","r")

token = file.readline()

### SETTINGS:

content = "Run 1 Mile" # Task Name
start_date = date(2020, 1, 1) # Select a start date -> format: date(YYYY, M, D)
end_date = date(2021, 1, 1) # Select an end date (non-inclusive) -> format: date(YYYY, M, D)

###

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for due_date in daterange(start_date, end_date):
	requests.post("https://api.todoist.com/rest/v1/tasks",
    data=json.dumps({
        "content": content,
        "due_string": due_date.strftime("%Y-%m-%d"),
        "due_lang": "en",
        "priority": 4
    }),
    headers={
        "Content-Type": "application/json",
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": "Bearer %s" % token
    }).json()