EMAIL_ADRESS = "your_email_adress"
PASSWORD = "your_password"
TARGET_ADRESS = input('Please enter the target email: ')
#Check if the target email is an email
if(TARGET_EMAIL.find('@') == -1):
    print('Please enter a valid email')
    TARGET_EMAIL = input('Who do you want to send this email to? ')


