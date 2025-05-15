import smtplib

# Sample credentials (for demonstration purposes only)
smtp_s = "smtp.gmail.com"
smtp_p = 587
smtp_u = "rohit@gmail.com"
smtp_p = "rohit#@tiger"

# Create a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)

# Start TLS for security
server.starttls()

try:
    # Log in to the server
    server.login(smtp_user, smtp_p)
    print("Logged in successfully")

    # You can now send emails using server.sendmail() method
    # Example:
    # from_address = "your_email@example.com"
    # to_address = "recipient@example.com"
    # message = """\
    # Subject: Test Email
    #
    # This is a test email.
    # """
    # server.sendmail(from_address, to_address, message)

except smtplib.SMTPAuthenticationError:
    print("Failed to log in. Check your credentials.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection to the SMTP server
    server.quit()
