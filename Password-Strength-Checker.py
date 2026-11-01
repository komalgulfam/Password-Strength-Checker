password=input("enter your password")
passwordlength=False
specialcharac=False
uppercase=False
numbers=False
alphanum=False
count=0
if len(password)>=8:
    passwordlength=True
for i in password:
    if i in "@_!#":
        specialcharac=True
if password[0].isupper():
    uppercase=True
for i in password:
    if i in "0123456789":
        numbers=True

for i in password:
    if "a"<=i<="z" or "A"<=i<="Z":
        count=count+1    
if count>=8:
    alphanum=True
if passwordlength and specialcharac and uppercase and numbers and alphanum:
    print("your password is strong")
else:
    print("your password is weak")
