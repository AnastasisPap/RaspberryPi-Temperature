import os
import time
import plain_email

#Measure current temperature
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        output = temp.replace("temp=", "")
        return(output[:2])

EMAIL_SUBJECT = "Raspberry pi Temperature"

while True:
        if int(measure_temp()) < 50:
                print("Current temperature is " + measure_temp() + " celsius")
                time.sleep(1)
        elif int(measure_temp()) > 50:
                message = "Hey this is your raspberry pi, this is a warning that your raspberry pi's temperature exceeds 50 celsius"
                plain_email.send_mail(EMAIL_SUBJECT, message)
                time.sleep(1000)
        elif int(measure_temp()) > 60:
                message = "Hey this is your raspberry pi, this is a warning that your raspberry pi's temperature exceeds 60 celsius"
                plain_email.send_mail(EMAIL_SUBJECT, message)
                time.sleep(1000)
        elif int(measure_temp()) > 80:
                DANGER_SUBJECT = "This raspberry pi is on FIIIIIIIIREEEEE"
                DANGER_MESSAGE = "!!!!!WARNING!!!!!" \
                         "YOUR RASPBERRY PI HAS EXCEEDED 80 DEGREES CELSIUS PLEASE CHECK IT NOW"
                plain_email.send_mail(DANGER_SUBJECT, DANGER_MESSAGE)
                break

