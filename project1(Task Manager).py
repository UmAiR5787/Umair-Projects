import json
print("======== Task Manager ======")
option=input("Enter '1' to add tasks\nEnter '2' to view Tasks.\nEnter '3' to remove an task\n\n")
tasks_list={
 
 } 
no=0
if option=="2":
 with open ("tasks.json","r") as file:
  tasks=json.load(file)
  for taskno,Tasks in tasks.items():
   print(f"{taskno}: {Tasks}")
elif option=="1":
 try:
  with open("tasks.json", "r") as file:
   tasks_list = json.load(file)
   no = len(tasks_list)
 except(FileNotFoundError, json.JSONDecodeError):
    tasks_list = {}
 while True:
   tasks=input("Enter Task: ( 'q' for quit) ")
   if tasks=="q":
      break
   no+=1
   tasks_list[f"Task no {no}"]=tasks
 with open("tasks.json","w") as file:
    json.dump(tasks_list,file)
 print("Tasks saved to json file successfully")
elif option=="3":
  try:
   with open ("tasks.json","r") as file:
    tasks=json.load(file)
  except(FileNotFoundError, json.JSONDecodeError):
    tasks = {}
  while True:
   taskdel=input("Enter the task no you want to delete('q' to exit): ")
   if taskdel=="q":
        break
   elif taskdel in tasks:
    for taskno,Tasks in tasks.items():
      if taskno==taskdel:
        try:
         del tasks[taskno]
         no-=1
        except IndexError:
          print("Task not not found")   
        with open ("tasks.json","w") as file:
            json.dump(tasks,file)  
            print("Task Removed Successfully!") 
        break  
     
    
