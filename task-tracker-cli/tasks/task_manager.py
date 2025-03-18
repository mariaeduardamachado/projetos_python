class Task:
    def __init__(self, title, description='', status='pending', due_date=None):
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description='', due_date=None):
        task = Task(title, description, status='pending', due_date=due_date)
        self.tasks.append(task)

    def update_task(self, index, title=None, description=None, status=None, due_date=None):
        if 0 <= index < len(self.tasks):
            if title is not None:
                self.tasks[index].title = title
            if description is not None:
                self.tasks[index].description = description
            if status is not None:
                self.tasks[index].status = status
            if due_date is not None:
                self.tasks[index].due_date = due_date

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def list_tasks(self):
        return self.tasks

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None