<div align="center">

<img src="https://raw.githubusercontent.com/ivnvxd/ivnvxd/master/img/h_task_manager.png" alt="logo" width="270" height="auto" />
<h1>Task Manager</h1>
</div>
To assist users in effectively managing and monitoring their work, Task Manager is a small, command-line program. Users can interact with this application's clear and user-friendly text-based interface while adding tasks, viewing current tasks, marking tasks as completed, and deleting tasks. Your tasks are stored between sessions since the application keeps them in a 'tasks.json' file.
With color-coded status indications, this Python project improves the user experience by utilizing ANSI color codes. A simple CRUD (Create, Read, Update, Delete) interface is provided by the system for task management, and tasks are represented as objects.

## Features
- **Add Tasks**
- **View Tasks**
- **Mark Tasks as Completed**
- **Delete Tasks**
- **Persistent Storage**

## Technologies Used
- Python 3.x
- JSON for data persistence
- ANSI color codes for terminal output

## Prerequisites
- Python 3.x installed on your system.
- A terminal or command-line interface that supports ANSI escape codes (for color coding).

## How to Run
1. Clone the project:
```bash
>> git clone https://github.com/Nishmitha-gowda/Task-Manager.git
>> cd python-project-52
```

2. Navigate to the directory and run the application:
```bash
>> python task_manager.py
```

## Task File
- The tasks are stored in a tasks.json file. This file will be created automatically upon adding the first task.

## Functionalities
- **Add Task**:
Allows you to add a task with a title. The task will be added to the list and saved in the `tasks.json` file.
- **View Tasks**:
Displays a list of all tasks, showing their ID, title, and status (either "Pending" or "Completed").
- **Delete Task**:
Allows you to delete a task by its ID. The task will be removed from the list and the changes will be saved to the `tasks.json` file.
- **Mark Task as Complete**:
Allows you to mark a task as completed by its ID. The task's status will change, and the updated status will be saved in the `tasks.json` file.
- **Exit**:
Exits the application and saves any changes to the tasks.json file.
- **User-Friendly CLI**: The program features a clean menu system with color-coded feedback for task status (completed or pending).
    - **Green** for success
    - **Red** for errors
    - **Yellow** for warnings
    - **Blue** for task list and menu options
 



