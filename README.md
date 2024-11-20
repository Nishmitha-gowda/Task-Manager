<div align="center">

<img src="https://raw.githubusercontent.com/ivnvxd/ivnvxd/master/img/h_task_manager.png" alt="logo" width="270" height="auto" />
<h1>Task Manager</h1>
</div>
To assist users in effectively managing and monitoring their work, Task Manager is a small, command-line program. Users can interact with this application's clear and user-friendly text-based interface while adding tasks, viewing current tasks, marking tasks as completed, and deleting tasks. Your tasks are stored between sessions since the application keeps them in a 'tasks.json' file.

This is a Task Manager application that allows users to register, log in, and manage tasks. Each user has their own task list that is saved persistently, so when they log in again, their tasks are preserved.

- The program supports:

    - User registration and login with email and password.
    - Task creation, viewing, deletion, and marking tasks as completed.
    - Tasks are saved separately for each user, so each user has their own private task list

## Features
- **User Authentication**: Users can register and log in with email and password. Passwords are securely hashed using SHA-256 encryption.
- **Task Management**:
    - Add new tasks
    - View tasks with status (Pending or Completed)
    - Delete tasks
    - Mark tasks as completed
- **Persistent Storage**: User data and tasks are saved in separate JSON files, ensuring data is preserved across program runs.

## Technologies Used
- Python 3.x
- JSON for data persistence
- ANSI color codes for terminal output

## Prerequisites
- Python 3.x installed on your system.
- A terminal or command-line interface that supports ANSI escape codes (for color coding).
- No external dependencies; this program uses built-in Python libraries.


## How to Run
1. Clone the project:
```bash
>> git clone https://github.com/Nishmitha-gowda/Task-Manager.git
>> cd Task-Manager
```

2. Navigate to the directory and run the application:
```bash
>> python Task-Manager.py
```

## Task File
- The tasks are stored in a `tasks.json` file. This file will be created automatically upon adding the first task.

## Functionalities
- **Registration**
1. When you first start the program, you'll be asked if you have an account.
2. If you don’t, choose n to register a new user.
3. Enter a valid email address and password to register. Your password will be hashed before it is saved for security.

- **Login**
1. If you have an account, choose y at the prompt.
2. Enter your registered email address and password to log in.

- **Task Management**
 1. Once logged in, you'll be able to:
    - **Add Tasks**: You can add a new task by providing a title.
    - **View Tasks**: You can see all your tasks along with their completion status.
    - **Delete Tasks**: You can delete tasks by entering the task ID.
    - **Mark Tasks as Complete**: You can mark a task as completed.

- **Log Out**
1. To log out, select 5 from the menu, and the program will save your tasks and exit.

- **Color-Coded UI**
1. The application uses color codes for task statuses and feedback messages:
   - **Green** for success
   - **Red** for errors
   - **Yellow** for warnings
   - **Blue** for task list and menu options

## Data Storage
- **Users Data**:
    - The program stores registered users' data (email and hashed password) in the users.json file.
- **Tasks Data**:
    - Tasks are stored in a separate file for each user, named as tasks_<user_email>.json (e.g., tasks_user@example_com.json).
    - Each task has an ID, title, and completion status (pending/completed).
 
 ## Security Considerations
- Passwords are not stored in plain text. They are securely hashed using the SHA-256 algorithm.
- User task data is stored in JSON files and is not encrypted. For more advanced security, consider encrypting the task files.

## Notes
- Ensure that the users.json and task files for each user exist or will be created on the first run.
- Task files are saved per user based on their email, with @ and . replaced by underscores (_) to ensure valid file names.



   



