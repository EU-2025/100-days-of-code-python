import smtplib

my_email = "example@gmail.com"
password = "pass123"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="friend@gmail.com", 
        msg="Subjet:Hello\n\nThis is the body of my mail."
    )