import re


class check_email_basic:

    def __init__(self, email):
        self.email = email

    def check_email(self):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)

        if match == None:
            return False
        else:
            return True



