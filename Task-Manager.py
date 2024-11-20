import json
import os
import hashlib

# ANSI color codes for terminal output
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


# Global list to store users
users = []


class User:
    """Represents a user with an email and hashed password."""

    def __init__(self, email, password):
        """Initializes a user with an email and hashed password."""
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password):
        """Hashes the password using SHA-256 for security."""
        return hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        """Converts the user object to a dictionary format."""
        return {"email": self.email, "password": self.password}

    @staticmethod
    def from_dict(data):
        """Creates a user object from a dictionary."""
        user = User(data["email"], "")
        user.password = data["password"]  # Directly set the hashed password
        return user


def load_users():
    """Loads users from a JSON file into the users list."""
    global users
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            users = [User.from_dict(user_data) for user_data in json.load(file)]


def save_users():
    """Saves all users to a JSON file."""
    with open("users.json", "w") as file:
        json.dump([user.to_dict() for user in users], file, indent=4)


def load_tasks_for_user(user_email):
    """Loads tasks specific to the logged-in user from a file."""
    tasks_file = f"tasks_{user_email.replace('@', '_').replace('.', '_')}.json"
    tasks = []
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            tasks = [Task.from_dict(task_data) for task_data in json.load(file)]
    return tasks


def save_tasks_for_user(user_email, tasks):
    """Saves tasks specific to the logged-in user to a file."""
    tasks_file = f"tasks_{user_email.replace('@', '_').replace('.', '_')}.json"
    with open(tasks_file, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)


def register_user():
    """Handles user registration."""
    email = input("Enter your email: ").strip().lower()
    password = input("Enter your password: ").strip()

    # Check if the email is already registered
    if any(user.email == email for user in users):
        print(f"{RED}Email already registered! Please try logging in.{RESET}")
        return None

    new_user = User(email, password)
    users.append(new_user)
    save_users()  # Save the updated users list
    print(f"{GREEN}User registered successfully!{RESET}")
    return new_user


def login_user():
    """Handles user login."""
    email = input("Enter your email: ").strip().lower()
    password = input("Enter your password: ").strip()

    # Find the user by email and check if the password matches
    user = next((user for user in users if user.email == email), None)

    if user and user.password == hashlib.sha256(password.encode()).hexdigest():
        print(f"{GREEN}Login successful!{RESET}")
        return user
    else:
        print(f"{RED}Invalid email or password!{RESET}")
        return None


def add_task(title, tasks, user_email):
    """Adds a new task to the task list and saves it."""
    task_id = len(tasks) + 1
    tasks.append(Task(task_id, title))
    save_tasks_for_user(user_email, tasks)  # Save tasks immediately after adding
    print(f"{GREEN}Task '{title}' added successfully!{RESET}")


def view_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print(f"{YELLOW}No tasks available. Please add some tasks!{RESET}")
    else:
        print(f"\n{HEADER}--------------------Task List---------------------{RESET}")
        for task in tasks:
            status = f"{GREEN}{COMPLETED_ICON} Completed{RESET}" if task.completed else f"{RED}{PENDING_ICON} Pending{RESET}"
            print(f"{BLUE}[{task.id}]  {task.title:<25} {status}")
        print("-" * 50)


def delete_task(task_id, tasks, user_email):
    """Deletes a task by its ID and saves the updated task list."""
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks_for_user(user_email, tasks)  # Save tasks after deletion
        print(f"{GREEN}Task with ID {task_id} deleted.{RESET}")
    else:
        print(f"{RED}Task with ID {task_id} not found.{RESET}")


def mark_task_complete(task_id, tasks, user_email):
    """Marks a task as completed and saves the updated task list."""
    task = next((t for t in tasks if t.id == task_id), None)
    if task:
        task.completed = True
        save_tasks_for_user(user_email, tasks)  # Save tasks after marking complete
        print(f"{GREEN}Task '{task.title}' marked as completed!{RESET}")
    else:
        print(f"{RED}Task with ID {task_id} not found.{RESET}")


def display_menu(current_user):
    """Displays the main menu for user interaction."""
    print("\n" + "=" * 60)
    print(f"{HEADER}Task Manager - Logged in as {current_user.email}{RESET}")
    print("=" * 60)
    print(f"1. {BLUE}Add Task{RESET}")
    print(f"2. {BLUE}View Tasks{RESET}")
    print(f"3. {BLUE}Delete Task{RESET}")
    print(f"4. {BLUE}Mark Task Complete{RESET}")
    print(f"5. {RED}Log Out{RESET}")
    print("=" * 60)


def main():
    """Main program loop to interact with the user."""
    load_users()  # Load existing users from the file

    print(f"{HEADER}Welcome to the Task Manager!{RESET}")

    current_user = None
    while current_user is None:
        choice = input(f"\nDo you have an account? (y/n): ").strip().lower()
        if choice == 'y':
            current_user = login_user()
        elif choice == 'n':
            current_user = register_user()
        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")

    while True:
        # Load tasks for the logged-in user
        tasks = load_tasks_for_user(current_user.email)

        display_menu(current_user)  # Show the menu
        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title, tasks, current_user.email)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id, tasks, current_user.email)
            except ValueError:
                print(f"{RED}Invalid task ID.{RESET}")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                mark_task_complete(task_id, tasks, current_user.email)
            except ValueError:
                print(f"{RED}Invalid task ID.{RESET}")
        elif choice == "5":
            save_tasks_for_user(current_user.email, tasks)  # Save before logging out
            print(f"{GREEN}Logging out...{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")


# Run the program
if __name__ == "__main__":
    main()
