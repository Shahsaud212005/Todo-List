#main dictionary
tasks = {}

while True:
    #this is the main print statment
    print("""Welcome to ToDo list,
        What can i do for you today?, Available options (View tasks, Add tasks, Update tasks, Remove tasks)""")
    task = input("").lower()

#   function to add a task in the dictionary
    if task == "add" or task == "add task":
        name = input("Please enter a task: ").lower()
        date = input("Please enter the dealdline for the task (Date/Month/Year)").lower()
        status = input("What's the status of this task (Completed/Unfinished): ").lower()
        tasks[name] = {"Deadline" : date, "Status" : status}


#   function to view a task from the dictionary
    elif task == "view" or task == "view task":
        if tasks == {}:
            print("the task list is empty")
        for key, value in tasks.items():
            print(f"Task {key} : Date {value["Deadline"]} : Status {value["Status"]}")

#   function to update the task's status
    elif task == "update" or task == "update task":
        task_name = input("Enter tha name of the task: ")
        if task_name in tasks:
            new_status = input("Is this task completed or unfinished?: ").lower()
            if new_status == "completed":
                tasks[task_name] = {"Deadline" : date, "Status" : new_status}
            elif new_status == "unfinished":
                tasks[task_name] = {"Deadline" : date, "Status" : new_status}
        else:
            print("The task is not found in the saved list.")


#   function to remove a task from the dictionary
    elif task == "remove" or task == "remove task":
        remove = input("Enter the name for the task to remove: ")
        tasks.pop(remove)

    else:
        print("I don't understand, Please select from the given options (View tasks, Add tasks, Update tasks, Remove tasks).")
        task = input("").lower()

#   function to exit or use the list again
    exit = input("Do you wanna exit the list (yes/no)").lower()
    if exit == "yes":
        print("Bye")
        break
    elif exit == "no":
        continue
    else:
        print("I don't understand.")