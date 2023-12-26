from pprint import pprint
from todoist_api_python.api import TodoistAPI

api = TodoistAPI("755a8992983b0540febf3a6c66c4d9c16a7b9d31")

def display_menu():
    """
    Menu to navigate program functions
    """
    print("Options:")
    print("1. Show tasks")
    print("2. Create tasks")
    print("3. Change account")

def get_user_input():
    """
    Record user input and return it if valid
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a valid choice (1-3).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def user_choice(user_choice):
    """
    Sub-menus depending on user choice from menu
    """
    if user_choice == 1:
        print("Which tasks do you wanna view?")
        print("1. My day")
        print("2. Today")
        print("3. Weekly")
    elif user_choice == 2:
        print("Create task")
        
    elif user_choice == 3:
        print("You selected Option 3.")

def view_tasks(user_choice):
    """
    Sub-menu if user choose to view tasks
    """
    if user_choice == 1:
        print("option 1")
    elif user_choice == 2:
        get_todays_tasks()
    elif user_choice == 3:
        print("option 3")
        

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
    
    pprint(tasks)



def main():
    display_menu()
    user_input = get_user_input()
    user_choice(user_input)
    user_input = get_user_input()
    view_tasks(user_input)
    


main()