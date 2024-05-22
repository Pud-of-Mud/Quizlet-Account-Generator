import webbot
from webbot import Browser
import time
import random
erl = Browser()
targetWebsiteUrl = "https://quizlet.com"
clearDataUrl = "chrome://settings/clearBrowserData"
number = random.randint(1, 100000000000000000) 
numAccCreatedThisRun = 0

print("Do you want a single account or many accounts under one email address? ")

while repeat != "single" or "multi":
    repeat = input("single/multi: ") 

password = input("Please input the password you wish for the accounts. Note: It will end with an additional h afterwards \n")

# The + at the end of the email makes the duplicates function.
email = input("The beginning of the Email that will be used to create new accounts goes below. (everything before the @)\n" + "+") 
emailEnd = input("Input the domain of the Email below. (@mail.com) \n")

while True:
    
  erl.go_to(targetWebsiteUrl)
  erl.click(text='Sign up')
  
  # Sets the birthday of the user; has no affect on the accouns volitiy
  erl.click(text='Month')
  erl.click(text='January')
  
  erl.click(text='Day')
  erl.click(text='16')
  
  erl.click(text='Year')
  erl.click(text='2008') 

  # Sets the Email of the "user"
  erl.click(text='user@email.com')
  erl.type(email)
  erl.type(number)
  erl.type(emailEnd)
  
  # For some reason you must type the password in slowly to register
  erl.type(password, into='●●●●●●●●', clear=True)
  time.sleep(1)
  erl.click(text='●●●●●●●●')
  erl.type('h')
  time.sleep(1)
  
  erl.click(text='Sign up')

  #Refresh the page
  erl.go_to(targetWebsiteUrl)
  
  number = number + 1  # adds one to the current email address for the next account
  numAccCreatedThisRun = numAccCreatedThisRun + 1
  print(numAccCreatedThisRun + "account(s) created!")
    
  if repeat == "single":
    break
