from oscar_modules.check_email import check_email

class check_email_basic:

    def __init__(self, email):
        self.email = email

    def check_email(self):
        return check_email(self.email)



