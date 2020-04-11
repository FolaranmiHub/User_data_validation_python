import random
import string

  #Ask for firstName, lastName and Email
  
def Ask_details():
  
  FirstName = input("Enter First Name here \n")
  LastName = input("Enter Last Name here \n")
  User_email = input("Enter Email here \n")
  
  staff_details = [FirstName, LastName, User_email]
  
  return staff_details
  
#Generate random password using first 2 letters of firstName, last 2 letters of lastName and random string of 5 in length
def get_password(staff_details):
  
  characters = string.ascii_letters
  length = 5
  rand_password = ''.join(random.choice(characters)for i in range(length))
  password = (staff_details[0][0:2] + staff_details[1][-2:] + str(rand_password))
  
  return password
  
  
Argument = True
Main_container = []

while True:
  
  staff_details = Ask_details()
  password = get_password(staff_details)
  
  print("Your generated password is " + str(password))
  
    
   #Ask if s/he is ok with the password
     
  password_ok = input("Do you like this password? If yes, enter Yes. If No, enter new password")
   
  while True:
    
    if password_ok == "Yes":
     
#If okay with password, add details to staff_details
      staff_details.append(password)
      Main_container.append(staff_details)
      
      break
        
 #Prompt them to input prefered password if not satisfied
    else:
      
      pre_password = input("Enter preferred password equal or longer than 7 \n")
      
      while True:
        
        if len(password) >= 7:
          
          staff_details.append(pre_password)
          Main_container.append(staff_details)
        
          break 
          
        else:
          print("Your password is not upto 7 characters")
          pre_password = input("Enter new chosen password here \n")
          break
    
    
 #Add a different user detail    
  new_user = input("Would you like to enter a new user? Yes/No \n")
  
  
  if new_user == "No":
    
    Argument = False
    for item in Main_container:
      print(item)
      
  else:
    
    Argument = True
  
      
        
    
       
    
      

  
  
  
  
  




























    