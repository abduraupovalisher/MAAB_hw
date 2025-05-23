import json

def load_tasks(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

tasks = load_tasks('tasks.json')
display_tasks(tasks)
def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks

    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

calculate_statistics(tasks)
def json_to_csv(json_filename, csv_filename):
    tasks = load_tasks(json_filename)
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

json_to_csv('tasks.json', 'tasks.csv')

