#getting user email address
email=input("Enter your email address: ").strip()

#slice out username
username=email[:email.index("@")]

#slice out domain
doamin=email[email.index(@)+1:]

#output format message
output=print("Your email address is",email,/
             "username is",username,/
             "domain is",domain)

#final output
print(output)


