class Task:
    def __init__(self, title, description="", status="pending", due_date=None):
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

    def __repr__(self):
        return f"Task(title={self.title}, description={self.description}, status={self.status}, due_date={self.due_date})"

    def mark_completed(self):
        self.status = "completed"

    def mark_in_progress(self):
        self.status = "in progress"

    def update_details(self, title=None, description=None, due_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date