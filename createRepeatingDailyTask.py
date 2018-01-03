import uuid, requests, json
from datetime import timedelta, date

file = open("token.txt","r")

token = file.readline()

### SETTINGS:

content = "Run 1 Mile" # Task Name
start_date = date(2018, 11, 1) # Select a start date -> format: date(YYYY, M, D)
end_date = date(2019, 1, 1) # Select an end date (non-inclusive) -> format: date(YYYY, M, D)

###

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for due_date in daterange(start_date, end_date):
	r = requests.post("https://beta.todoist.com/API/v8/tasks",
	    params={"token": token},
	    data=json.dumps({"content": content,
	                     "due_date": due_date.strftime("%Y-%m-%d"),
	                     }),
	    headers={
	        "Content-Type": "application/json",
	        "X-Request-Id": str(uuid.uuid4()),
	    }
	)
