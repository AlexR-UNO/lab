

class Account:

    def __init__(self, name='John'):
        self._account_name = name
        self._account_balance = 0

    def deposit(self, deposit):
        if deposit > 0:
            self._account_balance += deposit
            return True
        else:
            return False

    def withdraw(self, charge):
        if (charge > 0) and not (charge > self._account_balance):
            self._account_balance -= charge
            return True
        else:
            return False

    def get_balance(self):
        return self._account_balance

    def get_name(self):
        return self._account_name

