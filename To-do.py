task = []
print("1. Add your tasks today")
print("2. View tasks")
print("3. Delete tasks")
print("4. Save & Exit")


def add_task():
    task.append(input("enter your task : ").strip(","))
    print("Task added.")
def view_task():
    for i, t in enumerate(task): #enumerate is used to get index and value
        print(f"{i+1}. {t}")

def delete_task(task):
    view_task()
    task_index = int(input("Enter the task number to delete : ")) - 1
    if 0 <= task_index < len(task):
        del task[task_index]
        print("Task deleted.")
    else:
        print("Invalid task number.")
while True:
    choice = input("enter your choice : ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        with open("tasks.txt", "w") as f:
            for t in task:
                f.write(t + "\n")
            print("Tasks saved. Exiting...")