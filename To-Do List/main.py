from tabulate import tabulate
import sys
import csv

class Task:
    all_tasks = []

    def __init__(self, task: str):
        self.task = task.strip()
        if not self.task:
            raise ValueError("Task description cannot be empty")
        Task.all_tasks.append(self.task)
        print("Task added successfully!")

    @classmethod
    def view_task(cls):
        if not cls.all_tasks:
            print("\nNo tasks available!")
            return
        task_list = [("S.N.", "Task")] + list(enumerate(cls.all_tasks, 1))
        print("\n" + tabulate(task_list, tablefmt="rounded_grid"))

    @classmethod
    def delete_task(cls):
        if not cls.all_tasks:
            print("\nNo tasks to delete!")
            return
        
        cls.view_task()
        num = cls._get_valid_task_number("Enter the task number to delete: ")
        if cls.confirm_action(f"Are you sure you want to delete task {num}?"):
            cls.all_tasks.pop(num-1)
            print(f"Task {num} deleted successfully!")

    @classmethod
    def update_task(cls):
        if not cls.all_tasks:
            print("\nNo tasks to update!")
            return

        cls.view_task()
        num = cls._get_valid_task_number("Enter the task number to update: ")

        while True:
            try:
                new_task = input("Enter the new task: ").strip()
                if not new_task:
                    raise ValueError("Task description cannot be empty\n")
            except ValueError as e:
                print(f"Error: {e}")
                continue
            else:
                cls.all_tasks[num-1] = new_task
                print(f"Task {num} updated successfully!")
                break

    @classmethod
    def _get_valid_task_number(cls, prompt: str):
        while True:
            try:
                num = int(input(prompt))
                if not 1 <= num <= len(cls.all_tasks):
                    raise ValueError()
                return num
            except ValueError:
                print("Please enter a valid task number.\n")


    @staticmethod
    def confirm_action(prompt: str):
        while True:
            ch = input(f"{prompt} (Y/N): ").lower()
            if ch in ["y", "yes"]:
                return True
            elif ch in ["n", "no"]:
                return False
            else:
                print("Please enter 'Y' or 'N'.")

    @classmethod
    def load_tasks_from_csv(cls):
        fileName = "tasks.csv"
        try:
            with open(fileName, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cls.all_tasks.append(row["Task"])
        except FileNotFoundError:
            return

    @classmethod
    def save_tasks_to_csv(cls):
        fileName = "tasks.csv"
        if not cls.all_tasks:
            print("No tasks to save!")
            return
        try:
            with open(fileName, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["S.N.","Task"])
                writer.writeheader()
                rows = [{"S.N.": index, "Task": task} for index, task in enumerate(cls.all_tasks,1)]
                writer.writerows(rows)
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")
        else:
            print(f"Tasks saved successfully to {fileName}.")

def main():
    print("\nTo-Do List")
    menu = [
        ("Key", "Action"),
        ("V", "View Tasks"),
        ("A", "Add a task"),
        ("D", "Delete a task"),
        ("U", "Update a task"),
        ("E", "Exit the Program"),
    ]
    Task.load_tasks_from_csv()
    while True:
        print("\n" + tabulate(menu, tablefmt="rounded_grid"))
        choice = input("Choose an option: ").strip()

        try:
            match choice:
                case "V" | "v":
                    Task.view_task()
                case "A" | "a":
                    task_description = input("\nEnter the task: ")
                    Task(task_description)
                case "D" | "d":
                    Task.delete_task()
                case "U" | "u":
                    Task.update_task()
                case "E" | "e":
                    if Task.confirm_action("\nAre you sure you want to exit?"):
                        if Task.confirm_action("\nDo you want to save the tasks before exiting?"):
                            print("Saving the tasks to a CSV file...")
                            Task.save_tasks_to_csv()
                        else:
                            print("Tasks were not saved.")
                        sys.exit("Exiting the program!\n")
                case _:
                    print("\nInvalid option!")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()