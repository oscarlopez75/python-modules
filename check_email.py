import sys
import re

def check_email(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        return False
    else:
        return True



if __name__ == "__main__":
    print(check_email(sys.argv[1]))
