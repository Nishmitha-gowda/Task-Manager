import json
import os

# ANSI color codes for terminal output (to style terminal text)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
PENDING_ICON = "❌"
COMPLETED_ICON = "✅"
HEADER = "\033[1m"  # Bold text

class Task:
    """Represents a single task."""
    
    def __init__(self, task_id, title, completed=False):
        """Initializes a task with an ID, title, and completion status."""
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        """Converts the task object to a dictionary format."""
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        """Creates a task object from a dictionary."""
        return Task(data["id"], data["title"], data["completed"])

# Global list to store tasks
tasks = []

def load_tasks():
    """Loads tasks from a JSON file into the tasks list."""
    if os.path.exists("tasks.json"):  # Check if the tasks.json file exists
        with open("tasks.json", "r") as file:  # Open the file in read mode
            for task_data in json.load(file):  # Load JSON data
                tasks.append(Task.from_dict(task_data))  # Convert each task and add to the list

def save_tasks():
    """Saves all tasks to a JSON file."""
    with open("tasks.json", "w") as file:  # Open the file in write mode
        json.dump([task.to_dict() for task in tasks], file, indent=4)  # Save tasks as a JSON array

def add_task(title):
    """Adds a new task to the task list."""
    task_id = len(tasks) + 1  # Assign a new ID based on the current number of tasks
    tasks.append(Task(task_id, title))  # Create a new task and append it to the tasks list
    print(f"{GREEN}Task '{title}' added successfully!{RESET}")  # Output confirmation message

def view_tasks():
    """Displays all tasks with their status."""
    if not tasks:  # Check if the task list is empty
        print(f"{YELLOW}No tasks available. Please add some tasks!{RESET}")  # Inform the user
    else:
        print(f"\n{HEADER}--------------------Task List---------------------{RESET}")
        for task in tasks:  # Loop through each task
            status = f"{GREEN}{COMPLETED_ICON} Completed{RESET}" if task.completed else f"{RED}{PENDING_ICON} Pending{RESET}"
            # Print task details (ID, title, and status)
            print(f"{BLUE}[{task.id}]  {task.title:<25} {status}")
        print("-" * 50)  # Print a separator line

def delete_task(task_id):
    """Deletes a task by its ID."""
    task = next((t for t in tasks if t.id == task_id), None)  # Find task by ID
    if task:
        tasks.remove(task)  # Remove the task from the list
        print(f"{GREEN}Task with ID {task_id} deleted.{RESET}")  # Confirm deletion
    else:
        print(f"{RED}Task with ID {task_id} not found.{RESET}")  # If task ID is not found

def mark_task_complete(task_id):
    """Marks a task as completed."""
    task = next((t for t in tasks if t.id == task_id), None)  # Find task by ID
    if task:
        task.completed = True  # Mark the task as completed
        print(f"{GREEN}Task '{task.title}' marked as completed!{RESET}")  # Confirm the update
    else:
        print(f"{RED}Task with ID {task_id} not found.{RESET}")  # If task ID is not found

def display_menu():
    """Displays the main menu for user interaction."""
    print("\n" + "="*30)  # Print separator line
    print(f"{HEADER}Task Manager{RESET}")  # Print the title of the application
    print("="*30)
    print(f"1. {BLUE}Add Task{RESET}")
    print(f"2. {BLUE}View Tasks{RESET}")
    print(f"3. {BLUE}Delete Task{RESET}")
    print(f"4. {BLUE}Mark Task Complete{RESET}")
    print(f"5. {RED}Exit{RESET}")
    print("="*30)

def main():
    """Main program loop to interact with the user."""
    load_tasks()  # Load existing tasks from file at the start of the program
    while True:
        display_menu()  # Show the menu
        choice = input("\nEnter your choice: ")  # Get user input

        if choice == "1":
            title = input("Enter task title: ")  # Ask user for task title
            add_task(title)  # Add the task to the list
        elif choice == "2":
            view_tasks()  # Display all tasks
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))  # Get task ID for deletion
                delete_task(task_id)  # Delete the specified task
            except ValueError:
                print(f"{RED}Invalid task ID.{RESET}")  # Handle invalid input
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))  # Get task ID to mark as complete
                mark_task_complete(task_id)  # Mark the specified task as complete
            except ValueError:
                print(f"{RED}Invalid task ID.{RESET}")  # Handle invalid input
        elif choice == "5":
            save_tasks()  # Save tasks before exiting the program
            print(f"{GREEN}Goodbye!{RESET}")  # Output goodbye message
            break  # Exit the loop and end the program
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")  # Handle invalid menu choice

# Run the program
if __name__ == "__main__":
    main()  # Start the main program loop
