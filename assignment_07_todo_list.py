# =============================================================================
def display_menu():
    """Displays the main menu."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompts the user for a task description and adds it to the list."""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    """Displays all tasks currently in the list."""
    if not tasks:
        print("Your task list is empty!")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Shows the task list and removes the one the user selects."""
    if not tasks:
        print("Your task list is empty! Nothing to delete.")
        return

    view_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        return

    removed = tasks.pop(index - 1)
    print(f'Task "{removed}" has been removed.')


if __name__ == "__main__":
    tasks = []
    choice = None

    while choice != "4":
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        print()