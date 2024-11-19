# Task-Manager
Task Manager is a lightweight, command-line productivity tool designed to help users efficiently manage and track their tasks.The **Task Manager CLI** is a simple, command-line application that allows users to manage tasks efficiently. With this tool, users can add tasks, view existing tasks, mark tasks as completed, and delete tasks, all while interacting with a clean and intuitive text-based interface. The application stores the tasks persistently in a `tasks.json` file, ensuring your tasks are saved between sessions.
This project is written in Python and uses ANSI color codes to enhance the user experience with color-coded status indicators. Tasks are represented as objects, and the system provides a basic CRUD (Create, Read, Update, Delete) interface for task management.

## Features
- Add new tasks
- View all tasks with their status (completed or pending)
- Delete tasks by ID
- Mark tasks as completed
- Save and load tasks to/from `tasks.json`

## How to Run
1. Navigate to the directory and run the application:
   ```bash
   python task_manager.py
