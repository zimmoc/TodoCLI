from pprint import pprint
from todoist_api_python.api import TodoistAPI
import sys

api = TodoistAPI("755a8992983b0540febf3a6c66c4d9c16a7b9d31")


### MENUS

def display_menu():
    """
    Menu to navigate program functions
    """
    print("\n")
    print("Options:")
    print("1. Show tasks")
    print("2. Create tasks")
    print("3. Change account")
    print("4. Exit program")
    print("\n")

def user_choice(user_choice):
    """
    Sub-menus depending on user choice from menu
    """
    if user_choice == 1:
        print("\n")
        print("Which tasks do you wanna view?")
        print("1. Overdue")
        print("2. Today")
        print("3. Weekly")
        print("4. Return to previous menu")
        print("\n")
    elif user_choice == 2:
        print("Create task")
        create_task()
        return_to_menu()
        
    elif user_choice == 3:
        print("You selected Option 3.")
    elif user_choice == 4:
        print("Exiting program...")
        sys.exit()

def return_to_menu():
    """
    Restarts main() function to give the impression that the user
    is sent back to main menu
    """
    print("\n")
    input("Press Enter to go back to menu...")
    print("\n")
    main()

def return_to_tasks_menu():
    """
    Restarts main() function to give the impression that the user
    is sent back to main menu
    """
    print("\n")
    input("Press Enter to return to tasks menu...")
    print("\n")
    user_input = 1
    user_choice(user_input)
    user_input = get_user_input()
    view_tasks(user_input)

### USER INPUT RESPONSE
        
def get_user_input():
    """
    Record user input and return it if valid
    """
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_tasks(user_choice):
    """
    Sub-menu if user choose to view tasks
    """
    if user_choice == 1:
        get_overdue_tasks()
        return_to_tasks_menu()
    elif user_choice == 2:
        get_todays_tasks()
        return_to_tasks_menu()
    elif user_choice == 3:
        get_weekly_tasks()
        return_to_tasks_menu()
    elif user_choice == 4:
        main()


### API FUNCTIONS

## Get tasks from api 

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
    
    print("\n")
    print("Tasks due today")
    print("----------")
    for task in tasks:
        task_name = task.content
        due_date = task.due.date
        print(f"{task_name} - {due_date}")
    print("----------")

def get_overdue_tasks():
    """
    Get tasks marked with the today or overdue filter tag
    """
    try:
        tasks = api.get_tasks(
            filter='overdue'
        )
    except Exception as error:
        print(error)
    print("\n")
    print("Overdue tasks")
    print("----------")
    for task in tasks:
        task_name = task.content
        due_date = task.due.date
        print(f"{task_name} - {due_date}")
    print("----------")

def get_weekly_tasks():
    """
    Get tasks due before next monday
    """
    try:
        tasks = api.get_tasks(
            filter='due before: mon'
        )
    except Exception as error:
        print(error)
    
    print("\n")
    print("Tasks due this week")
    print("----------")
    for task in tasks:
        task_name = task.content
        due_date = task.due.date
        print(f"{task_name} - {due_date}")
    print("----------")

## Create tasks
    
def create_task():
    print("\n")
    task_name = input("Enter task: ")
    task_due = input("Enter task due date(ex. tomorrow, 2025-01-01): ")
    try:
        task = api.add_task(
            content=str(task_name),
            due_string=str(task_due),
    )
        
    except Exception as error:
        print(error)
    
    created_name = task.content
    created_due_date = task.due.date
    print("\n")
    print("Successfully created task")
    print("----------")
    print(f"Task name: {created_name}")
    print(f"With due date: {created_due_date}")

### MAIN
    
def main():
    display_menu()
    user_input = get_user_input()
    user_choice(user_input)
    user_input = get_user_input()
    view_tasks(user_input)

main()