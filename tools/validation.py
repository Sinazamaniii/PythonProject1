import re

def username_validator(username):
    if re.match(r"^[a-zA-Z\d]{10,20}$", username):
        return username
    else:
        raise ValueError("Invalid username !!!")



def password_validator(password):
    if re.match(r"^[a-zA-Z\d$@]{8,14}$", password):
        return password
    else:
        raise ValueError("Invalid password !!!")

def nickname_validator(nickname):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", nickname):
        return nickname
    else:
        raise ValueError("Invalid nickname !!!")