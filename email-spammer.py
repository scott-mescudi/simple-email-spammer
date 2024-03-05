import smtplib

smtp_server = input("Enter SMTP server (e.g., smtp.gmail.com): ")
smtp_port = int(input("Enter SMTP port (e.g., 587): "))
smtp_username = input("Enter your email address: ")
smtp_password = input("Enter your smtp password: ")

from_email = input("Enter your email address: ")
to_email = input("Enter recipient's email address: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")
message = f'Subject: {subject}\n\n{body}'

print("Exit program by closing terminal")
while True:
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, to_email, message)
      
