# Email Sender

This is a simple Python script that allows you to send emails using SMTP (Simple Mail Transfer Protocol).

## Setup

Before running the script, you need to provide some information about your SMTP server and email account. 

1. **SMTP Server**: Enter the address of your SMTP server (e.g., smtp.gmail.com).
2. **SMTP Port**: Specify the port number for your SMTP server (e.g., 587 for TLS).
3. **SMTP Username**: Enter your email address.
4. **SMTP Password**: Enter the password for your email account.
5. **From Email**: Enter the email address you want to send the email from.
6. **To Email**: Enter the recipient's email address.
7. **Subject**: Enter the subject of the email.
8. **Body**: Enter the body of the email.

## Running the Script

After providing the necessary information, execute the script. It will attempt to send the email using the provided SMTP server and credentials. If successful, it will print "Email sent successfully!" Otherwise, it will display an error message.

## Dependencies

This script requires the `smtplib` module, which is a part of the Python standard library. No additional installations are required.

## Notes

- Make sure you have enabled access to less secure apps in your email account settings if you are using Gmail or a similar service.
- Keep your SMTP credentials secure and avoid hardcoding them in the script for production use. Consider using environment variables or other secure methods for storing sensitive information.
- This script sends emails until you close it so be carefull
- I think it might be illegal to use idk
