# TodoCLI
TodoCLI is a Python terminal program, which runs in the Code Institute mock terminal on heroku.

TodoCLI offers a simple and efficient solution, providing users with a direct and convenient way to stay organized in their tasks, all from the comfort of their terminal environment.

[Here is the live version of my project.](https://todoist-ci-68350e20c8b6.herokuapp.com/)

![Mockup](/assets/images/readme/mockup.png)

## Features

### Existing Features
- __Main menu__

  - Menu where the user can choose what function they want to use
  - Option to exit program
  - Error handling for invalid user inputs

![Task Viewer](/assets/images/readme/menu.png)

- __Task viewer__

  - View active tasks filtered by overdue, due today or due this week
  - User can go back to menu and choose anoter filter or return to main menu

![Task Viewer](/assets/images/readme/taskviewer.png)

- __Task Creation__

  - Create tasks directly from the terminal
  - Date handling which can handle multiple input methods, like Today, tuesday
  or YYYY-MM-DD
  - Confirmation message with created task and due date

![Task creation](/assets/images/readme/taskcreation.png)

  - Error handling for due date input
  - Must be Today, tomorrow or a valid weekday if not in YYYY-MM-DD format
![Date error handling](/assets/images/readme/datehandling.png)

- __Complete tasks__

  - Display tasks due this week with a number to identify each task
  - Enter number identifier to complete that task
  - Visual confirmation of task completed with due date

![Task completion](/assets/images/readme/completetask.png)

### Future Features

- Change todoist API token in the terminal
    - Currently you have to change the api in run.py
- Improved GUI
    - colors to better visually reflect due dates
    - Interactive menu instead of "choose number option"
    - General improvement in design

## Testing
I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs: Typos in due dates, out of bounds inputs, strings where numbers are expected.
- Tested in my local terminal and the Code Institute Heroku terminal

### Bugs
Solved bugs
- I had problems deploying the project on heroku, I had forgotten to add the dependencies to requirements.txt. After i fixed that it started up with no problems.

### Validator Testing
- PEP8
  - No errors were returned when passing through the [PEP8 validator](https://pep8ci.herokuapp.com/)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deploymet
    - Create a new Heroku app
    - Set cvar: PORT - 8000
    - Set the buildbacks to Python and NodeJS in that order
    - Link th Heroku app to this repository
    - Enable automatic deploys
    - Click on Deploy

## TECHNOLOGIES USED

### Languages:

- [Python 3.9.1](https://www.python.org/downloads/release/python-391/): used to anchor the project and direct all application behaviour.

### Frameworks/Libraries, Programmes, and Tools:

#### Python modules/packages:

##### Standard library imports:

- [datetime](https://docs.python.org/3/library/datetime.html) was used to handle dates.
- [sys](https://docs.python.org/3/library/sys.html) was used to create the exit function for the program
- [pprint](https://docs.python.org/3/library/pprint.html) used to print api response during development to easier read and analyze the data.

##### Third-party imports:

- [Todoist API Client](https://pypi.org/project/todoist-api-python/) was used to implement my Todoist account and communicate with their services.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) Program used to write all the code.
- [GitHub](https://github.com/) website used to host all the project files.
- [Heroku](https://www.heroku.com/) was used to deploy the project.
- [pipreqs](https://github.com/bndr/pipreqs) I used pipreqs to auto generate my requirements.txt, which wasn't needed in the end but it's a great tool that im sure i will keep using.



# Credits 

To understand how to request data from Todoist i used their [Todoist API documentation](https://developer.todoist.com/rest/v2/#overview)

I also used Google whenever I couldn't make something work, which led me to various forums and help sites where people were asking about the same problem. I used that information to identify what was breaking my code and implemented fixes accordingly.

### Documentation

Creating these projects always introduce you to new ways to do things when searching for problems, other than forums and frantic googling i used these documentations to solve/understand problems i encountered
- [datetime](https://www.geeksforgeeks.org/python-datetime-timedelta-function/)
- [datetime strings](https://www.geeksforgeeks.org/converting-string-yyyy-mm-dd-into-datetime-in-python/)
- [Sys exit](https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python)
