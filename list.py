class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def remove_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print(f"Task '{description}' removed.")
                return
        print(f"Task '{description}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.description} - Priority: {task.priority}")

    def prioritize_tasks(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        print("Tasks prioritized.")

    def recommend_task(self, keyword):
        recommended_tasks = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if recommended_tasks:
            print("Recommended tasks:")
            for task in recommended_tasks:
                print(f"{task.description} - Priority: {task.priority}")
        else:
            print("No tasks match the description.")

# Example usage
task_manager = TaskManager()

s=int(input("enter how many tasks"))
for k in range(s):
    task=input("enter task name")
    prior=int(input("enter priority which is unique then others"))
    task_manager.add_task(task,prior)
#task_manager.add_task("Complete project report", 2)
#task_manager.add_task("Prepare presentation slides", 3)
#task_manager.add_task("Send email to team", 1)
print('%'*6)
task_manager.list_tasks()

remove_tasks=input("enter yes to remove task")
if(remove_tasks=="yes"):
    task_manager.list_tasks()
    ss=input("enter task name to remove")
    task_manager.remove_task(ss)

task_manager.list_tasks()

task_manager.prioritize_tasks()
task_manager.list_tasks()


