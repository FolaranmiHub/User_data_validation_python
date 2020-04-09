import random
import string

characters = string.ascii_letters

   #empty dictionary
container = {}

while True:
  #Ask for firstName, lastName and Email
  
  fname = input("Enter firstName here \n")
  lastname = input("Enter lastName here \n")
  email = input("Enter email here \n")
  
  details = [fname, lastname, email]
  
#Generate random password using first 2 letters of firstName, last 2 letters of lastName and random string of 5 in length
   
  length = 5
  splitting = f"{fname[0:2]}{lastname[-2:]}"
  password = f"{splitting}{(''.join(random.choice(characters)for i in range(length)))}"
  print(f"Your password is: {password}")
     
   #Ask if s/he is ok with the password
     
  password_ok = input("Do you like this password? if yes, enter yes. if no, enter new password")
   
  password_loop = True
  
  while password_loop:
    
    if password_ok == "yes":
      
#If okay with generated password, print staff data
      
      staff_data = {
        "firstName": fname, "lastName": lastname,
        "email": email, "password": password
      } 
      
      print(staff_data)
      
          
      password_loop = False;
        
 #Prompt them to input prefered password if not satisfied
    else:
      password = input("Enter new password equal or longer than 7")
 
    password_len = True
    while password_len:
      
      
      if len(password) >= 7:
        
        details.append(password)
     
        
       
        password_len = False
        password_loop = False
       
      
      else:
        print("Your password is less than 7")
        
        
        password = input("Enter new password here: \n")
        
  #while False:
    
    
     #def new_user():
       
  new_user = input("Would you like to enter a new user?")
  
  
  if (new_user == "no"):
    
    while False:
      
      for item in container:
        print(item)
      
        
    
       
    
      

  
  
  
  
  




























    