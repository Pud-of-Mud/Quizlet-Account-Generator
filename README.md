# Quizlet-Account-Generator
A Python script for generating Quizlet accounts all linked to a single email address to get the most out of free premium features.

## Usage
Place the beginning half of the target email into the `email` varable with the domain of the email into the `emailEnd` variable. Then, place the desired password for the accounts within the `password` variable. Do not use your email password! This is an unsafe practace for not only your email but for all of digital security. <br><br>
For example:

    password = "examplepassword"   # Note: The password you enter here will have an additional 'h' after it. 
    email = "youremailhere+"       # Note: you must place the '+' after the first half of the email.
    emailEnd = "@domain.com" 

## Warning!
Quizlet is known to send many emails to its users. Once many accounts are made to your address, you will be sent thousands of emails about promotions and to verify the account (which is unnecessary).

## Credits
- Code by @Pud-of-Mud
- webbot for browser interaction
