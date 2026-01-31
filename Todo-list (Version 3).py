tasks = {}  # To store task info with deadline and status

while True:
    print("""Welcome to ToDo list,
        what can I do for you today? Available options: (View tasks, Add tasks, Update tasks, Remove tasks)""")
    task = input("").lower()

    if task == "add":
        name = input("Please enter a task: ").lower()
        deadline = input("Please enter the deadline for the task (date/month/year): ").lower()
        status = input("What's the status of this task (completed/unfinished): ").lower()

        # Store task info as a dictionary with deadline and status
        tasks[name] = {"deadline": deadline, "status": status}

    elif task == "view":
        for key, value in tasks.items():
            print(f"Task: {key} | Deadline: {value['deadline']} | Status: {value['status']}")
        
    elif task == "remove":
        remove = input("Enter the name of the task to remove: ").lower()
        if remove in tasks:
            del tasks[remove]
            print(f"Task '{remove}' removed.")
        else:
            print("Task not found.")

    elif task == "update":
        update_task = input("Enter the name of the task to update: ").lower()
        if update_task in tasks:
            new_status = input("Enter the new status (completed/unfinished): ").lower()
            tasks[update_task]["status"] = new_status
            print(f"Task '{update_task}' status updated to {new_status}.")
        else:
            print("Task not found.")
    
    exit_program = input("Do you want to exit (yes/no): ").lower()
    if exit_program == "yes":
        print("Okay, bye!")
        break
    elif exit_program == "no":
        continue
    else:
        print("I don't understand.")
