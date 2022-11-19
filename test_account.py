from account import *


class Test:
    def setup_method(self):
        self.account1 = Account()
        self.account2 = Account('Jackie')
        self.account3 = Account('Jane')

    def teardown_method(self):
        del self.account3
        del self.account2
        del self.account1

    def test_init(self):
        assert self.account1.get_name() == 'John'
        assert self.account1.get_balance() == 0

        assert self.account2.get_name() == 'Jackie'
        assert self.account2.get_balance() == 0

        assert self.account3.get_name() == 'Jane'
        assert self.account3.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(500) is True
        assert self.account1.deposit(-500) is False
        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == 500
        # assert self.account1.deposit('500') is False

        assert self.account2.deposit(500) is True
        assert self.account2.deposit(-500) is False
        assert self.account2.deposit(0) is False
        assert self.account2.get_balance() == 500
        # assert self.account2.deposit('500') is False

        assert self.account3.deposit(500) is True
        assert self.account3.deposit(-500) is False
        assert self.account3.deposit(0) is False
        assert self.account3.get_balance() == 500
        # assert self.account3.deposit('500') is False

    def test_withdraw(self):
        self.account1.deposit(500)
        assert self.account1.withdraw(500) is True
        assert self.account1.get_balance() == 0
        self.account1.deposit(500)
        assert self.account1.withdraw(350) is True
        assert self.account1.withdraw(750) is False
        assert self.account1.withdraw(-500) is False
        assert self.account1.withdraw(0) is False
        assert self.account1.get_balance() == 150
        assert self.account1.withdraw('500') is False

        self.account2.deposit(500)
        assert self.account2.withdraw(500) is True
        assert self.account2.get_balance() == 0
        self.account2.deposit(500)
        assert self.account2.withdraw(350) is True
        assert self.account2.withdraw(750) is False
        assert self.account2.withdraw(-500) is False
        assert self.account2.withdraw(0) is False
        assert self.account2.get_balance() == 150
        assert self.account2.withdraw('500') is False

        self.account3.deposit(500)
        assert self.account3.withdraw(500) is True
        assert self.account3.get_balance() == 0
        self.account3.deposit(500)
        assert self.account3.withdraw(350) is True
        assert self.account3.withdraw(750) is False
        assert self.account3.withdraw(-500) is False
        assert self.account3.withdraw(0) is False
        assert self.account3.get_balance() == 150
        assert self.account3.withdraw('500') is False
