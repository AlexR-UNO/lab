

class Account:

    def __init__(self, name: str = 'John') -> None:
        """
        Constructor for Account; Defaults to an account under 'John' with balance of 0.

        :parameter name (str): Name of the Account
        """
        self._account_name = name
        self._account_balance = 0

    def deposit(self, deposit: float) -> bool:
        """
        Deposits the given number to the account balance.

        :parameter deposit: Float representing the amount to be added to the account balance.
        :return bool: True/False depending on if the deposit actually happens
        """

        try:
            if deposit > 0:
                self._account_balance += deposit
                return True
            else:
                return False
        except TypeError:
            return False

    def withdraw(self, charge: float) -> bool:
        """
        Withdraws the given number from the account balance.

        :parameter charge: Float representing the amount to be removed from the account balance.
        :return bool: True/False depending on if the withdrawal actually happens
        """
        try:
            if (charge > 0) and not (charge > self._account_balance):
                self._account_balance -= charge
                return True
            else:
                return False
        except TypeError:
            return False

    def get_balance(self) -> float:
        """
        Returns the account balance as a float
        :return float: The current balance of the account
        """
        return self._account_balance

    def get_name(self) -> str:
        """
        Returns the account name as a float
        :return str: The name of the Account
        """
        return self._account_name
