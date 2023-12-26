from pprint import pprint
from todoist_api_python.api import TodoistAPI

api = TodoistAPI("755a8992983b0540febf3a6c66c4d9c16a7b9d31")

def get_todays_tasks():
    """
    Get tasks market with the "Today" tag from todoist
    """
    try:
        tasks = api.get_tasks(
            filter='today'
        )
    except Exception as error:
        print(error)
    
    return tasks



def main():
    tasks = get_todays_tasks()
    pprint(tasks)

main()