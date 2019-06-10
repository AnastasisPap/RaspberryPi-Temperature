import smtplib
import config


def send_mail(subject, message):
    try:
	#Email server
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
	#Connect to the email
        server.login(config.EMAIL_ADRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(config.EMAIL_ADRESS, config.TARGET_ADRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

subject = input('What do you want the subject to be? ')
message = input('What do you want to tell the target? ')
send_mail(subject, message)
