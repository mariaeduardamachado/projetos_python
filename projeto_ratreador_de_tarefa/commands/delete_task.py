def delete_task(task_manager, task_id):
    """Delete a task by its ID."""
    task = task_manager.get_task(task_id)
    if task:
        task_manager.remove_task(task_id)
        print(f"Task '{task.title}' has been deleted.")
    else:
        print(f"Task with ID '{task_id}' not found.")