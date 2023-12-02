todo_list = []


while(True):
    process  = input("What task do you want? [add / view / remove / exit]\n")
    
    if(process == "add"):
        task = input("Enter a task: ")
        todo_list.append(task)
        print(f"Task created with title: {task}")
    elif(process == "view"):
        if not todo_list:
            print("No tasks to display")
        else:
            for task in todo_list:
                print(task)
    elif(process == "remove"):
        if todo_list:
            task = input("Enter task name you want to remove: ")
            if task in todo_list:
                todo_list.remove(task)
                print(f"Task {task} removed")
            else:
                print("This task doesn't exist in Todo List")
        else:
            print("No tasks to remove")
    elif(process == "exit"):
        break
    else:
        print("Not valid request")