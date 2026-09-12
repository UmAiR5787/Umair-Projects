import secrets
import smtplib
from email.message import EmailMessage

otp=str(secrets.randbelow(900000) + 100000 )


msg=EmailMessage()
msg["Subject"]="OTP Verification Email"
msg["From"]="syedumairzaidi10@gmail.com"
msg["To"]="syedumairzaidi10@gmail.com"
msg.set_content(f"Hello, Your OTP is {otp}")
try:
 server=smtplib.SMTP("smtp.gmail.com",587)
 server.starttls()
 server.login("syedumairzaidi10@gmail.com","vknf dcph drky fnen")
 server.send_message(msg)
 print("OTP verify e-mail has been sent succesfully!")
 verify=input("Enter OTP for verification:")
 if verify==otp:
  print("Your Allowed!")
 else:
  print("You'r not Allowed!") 
 server.quit()
except Exception as e:
 print(f"Error! Email nahi bheji ja saki: {e}") 

