def list_tasks(task_manager):
  tasks = task_manager.get_all_tasks()
  if not tasks:
     print("No tasks available.")
     return

  print("Current Tasks:")
  for task in tasks:
      status = task.status
      print(f"- {task.title} [{status}]")