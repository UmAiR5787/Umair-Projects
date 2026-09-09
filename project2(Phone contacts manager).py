import json
print("======== Phone Contacts Manager ========")
phone_contacts={}

def contacts_reader():
       with open("Phone-contacts.json", "r") as file:
        return json.load(file)
    
option=input("1.Add contacts\n2.View conatacts\n3.Remove contacts\n")
if option=="1":
 phone_contacts = contacts_reader()
 while True:
  name=input("Enter contacts Full Name: \n")
  pno=input("Enter phone number:  \n")
  lenghtofpno= len(pno)
  try:
     if lenghtofpno!=11:
         raise ValueError("Phone nunber should be 10 digits!\n")
     phone_contacts[name]=pno
     
     with open ("Phone-contacts.json","w") as file:
         json.dump(phone_contacts,file)
         print("Contacts saved successfully !!\n")  
  except ValueError as error:
   print("Error:",error)
  op=input("You want to again add an contact?\n('Y' for yes and 'Q' for quit)\n\n")
  if op in ["q","Q"]:
     break   
elif option=="2":
         contacts_list=contacts_reader()
         for index,(name,pno) in enumerate(contacts_list.items(),start=1):
            print(f"\n{index}.{name} ---> {pno}\n")
elif option=="3":
   contacts_list=contacts_reader()
   while True:
    condel=input("Which contact to delete (name only and 'Q' for quit): \n")
    if condel in ["Q","q"]:
       break
    elif condel in contacts_list:
     for names,pno in contacts_list.items():
      if names==condel:
          try:
              del contacts_list[names] 
          except IndexError:
                   print("contact not not found")   
          with open ("Phone-contacts.json","w") as file:
                     json.dump(contacts_list,file)  
                     print("Task Removed Successfully!\n") 
          break  
              
      


            