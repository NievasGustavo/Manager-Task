"""
Task Properties
Each task should have the following properties:
    · id: A unique identifier for the task
    · description: A short description of the task
    · status: The status of the task (todo, in-progress, done)
    · createdAt: The date and time when the task was created
    · updatedAt: The date and time when the task was last updated

 """
class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    
    def __str__(self) -> str:
        t = f"id: {self.id}"
        t += f"description: {self.description}"
        t += f"status: {self.colourTask()}"
        t += f"createdAt: {self.createdAt}"
        t += f"updatedAt: {self.updatedAt}"
        return t
    
    def toJson(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
    
    @classmethod
    def from_dict(cls, data):
        """Convierte un diccionario a un objeto Task."""
        return cls(
            id=data['id'],
            description=data['description'],
            status=data['status'],
            createdAt=data['createdAt'],
            updatedAt=data['updatedAt']
        )


    def colourTask(self) -> str:
        if self.status == "in-progress":
            return "\033[1;32m" + self.status + "\033[0m"
        elif self.status == "done":
            return "\033[1;34m" + self.status + "\033[0m"
        else:
            return "\033[1;31m" + self.status + "\033[0m"


if __name__ == "__main__":
    task = [Task(1, "Task 1", "todo", "2022-01-01", "2022-01-01"),
            Task(2, "Task 2", "in-progress", "2022-01-01", "2022-01-01"),
            Task(3, "Task 3", "done", "2022-01-01", "2022-01-01")]

    for t in task:
        print(t)
        