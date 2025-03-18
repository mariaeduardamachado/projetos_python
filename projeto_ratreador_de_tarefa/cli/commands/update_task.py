def update_task(task_manager, task_id, title=None, description=None, status=None):
    """
    Update the details or status of an existing task.

    Parameters:
    - task_manager: An instance of TaskManager to manage tasks.
    - task_id: The ID of the task to be updated.
    - title: The new title for the task (optional).
    - description: The new description for the task (optional).
    - status: The new status for the task (optional).
    """
    task = task_manager.get_task(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return

    if title:
        task.title = title
    if description:
        task.description = description
    if status:
        task.status = status

    task_manager.update_task(task)
    print(f"Task {task_id} updated successfully.")