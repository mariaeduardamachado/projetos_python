def add_task(task_manager):
  title = input("Enter the task title: ")
  description = input("Enter the task description: ")
  status = "pending"  # Default status for a new task
  due_date = input("Enter the due date (optional, format YYYY-MM-DD): ")

  task_manager.add_task(title, description, status, due_date)
  print(f"Task '{title}' added successfully.")