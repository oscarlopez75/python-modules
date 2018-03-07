from passlib.hash import pbkdf2_sha512
from passlib.hash import pbkdf2_sha256
import sys

#password = ""
#password_hash = ""
#mode = ""
#action = ""

def getParams(param1, param2, param3, param4):
    global password
    password = param1
    global password_hash
    password_hash = param2
    global mode
    mode = param3
    global action
    action = param4



    if (mode == '256' and action == 'validate') :
        return validate_256()
    if (mode == '256' and action == 'create') :
        return create_256()
    if (mode == '512' and action == 'validate') :
        return validate_512()
    if (mode == '512' and action == 'create') :
        return create_512()


def validate_256():
    global password
    global password_hash

    passOk = pbkdf2_sha256.verify(password, password_hash)

    return passOk

def validate_512():
    global password
    global password_hash

    passOk = pbkdf2_sha512.verify(password, password_hash)

    return passOk

def create_256():
    global password

    return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)



def create_512():
    global password

    return pbkdf2_sha512.encrypt(password, rounds=200000, salt_size=16)


# sys.argv[2] = password
# sys.argv[3] = hash
# sys.argv[4] = mode 512 or 256
# sys.argv[5] = create or validate

if __name__ == "__main__":

    arguments = len(sys.argv)

    if arguments >= 5:
        getParams(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Number of arguments invalid")
