from passlib.hash import pbkdf2_sha512
from passlib.hash import pbkdf2_sha256
import sys


class encrypt:
    password = ""
    password_hash = ""
    mode = ""
    action = ""

    def getParams(param1, param2, param3, param4):

        password = param1
        password_hash = param2
        mode = param3
        action = param4

        if (mode == '256' and action == 'validate'):

            try:
                return pbkdf2_sha256.verify(password, password_hash)
            except:
                return "Not able to validate the password, make sure all the params are correct"

        if (mode == '256' and action == 'create'):

            try:
                return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
            except:
                return "Not able to create the password, make sure all the params are correct"

        if (mode == '512' and action == 'validate'):

            try:
                return pbkdf2_sha512.verify(password, password_hash)
            except:
                return "Not able to validate the password, make sure all the params are correct"

        if (mode == '512' and action == 'create'):

            try:
                return pbkdf2_sha512.encrypt(password, rounds=200000, salt_size=16)
            except:
                return "Not able to create the password, make sure all the params are correct"

        return "Please check the params, was not able to find what you need"



