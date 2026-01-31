#   function to add a task in the dictionary
def add_task(strg):

    name = input("Please enter a task: ").lower()
    date = input("Please enter the dealdline for the task (Date/Month/Year)").lower()
    status = input("What's the status of this task (Completed/Unfinished): ").lower()
    strg[name] = {"Deadline" : date, "Status" : status}

    again()


#   function to view a task from the dictionary
def view_task(strg):

    if strg == {}:
        
        print("The task list is empty, Add some tasks first.")
    for key, value in strg.items():
        print(f"Task: {key.capitalize()}\nDate: {value["Deadline"]}\nStatus: {value["Status"]}")

    again()
    

#   function to update the task's status
def update_task(strg):
    
    task_name = input("Enter the name of the task: ")
    if task_name in strg:
        new_status = input("Is this task completed or unfinished?, Or type same if you don't want to change this field: ").lower()
        if new_status == "same":
            pass
        else:
            strg[task_name]["Status"] = new_status
        new_date = input("Enter the new deadline for this task (Date/Month/Year), Or type 'same' if you don't want to change the deadline: ").lower()
        if new_date == "same":
            pass
        else:
            strg[task_name]["Deadline"] = new_date
    else:
        print("The task is not found in the saved list.")

    again()
    

#   function to remove a task from the dictionary
def remove_task(strg):

    if strg == {}:
        print("The task list is empty, Add some tasks first.")
    
    else:
        remove = input("Enter the name for the task to remove: ")
        if remove not in strg:
            print("This task is not saved in the list.")
        else:
            strg.pop(remove)
    
    again()


# this fuction promts the user to use the program again or not.
def again():
    while True:
        quit = input("Do you wanna exit the list (yes/no)").lower()
        if quit == "yes":
            print("Bye")
            exit()
        elif quit == "no":
            break
        else:
            print("I don't understand.")    


#this is the main print statment
def main_list(strg):

    while True:

        print("""
        Menu:
        1) View tasks
        2) Add tasks
        3) Update tasks
        4) Remove tasks
          """)

        task = input("Choose an option: ").lower()
        if task == "add" or task == "add task" or task == "2":
            add_task(strg)
            # again()
        elif task == "view" or task == "view task" or task == "1":
            view_task(strg)
            # again()
        elif task == "update" or task == "update task" or task == "3":
            update_task(strg)
            # again()
        elif task == "remove" or task == "remove task" or task == "4":
            remove_task(strg)
            # again()
        else:
            print("I don't understand, Please select from the bellow options.")


# main dictionary
tasks = {}
print("Welcome to ToDo list.")
main_list(tasks)
