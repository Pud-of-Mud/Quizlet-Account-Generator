import webbot
import time
import random
erl = webbot.Browser()
targetWebsiteUrl = "https://quizlet.com"
clearDataUrl = "chrome://settings/clearBrowserData"
number = random.randint(1, 100000000000000000) 
numAccCreatedThisRun = 0

# Password of the accounts created 
# NOTE: Will have 'h' at the end after the password
password = "i9A1D3nj3a1hjhg"

# The Email that will be used to create new accounts goes below  
email = "exampleemail+"    # Make sure to put the + at the end.
emailEnd = "@mail.com"

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
  erl.click(text='user@quizlet.com')
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
  print("account created!")
