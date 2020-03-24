import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

class BankAccount(object):

    """ DECORATORS """
    def is_account_open(func):
        def wrapper(self, *args):
            if not self._isOpen:
                raise ValueError("Cannot access closed account from function {}".format(func.__name__))
            return func(self, *args)
        return wrapper

    """ METHODS """
    def __init__(self):
        self._balance = 0
        self._isOpen = False
        self._lock = threading.Lock()
        logging.debug('Created Bank account')


    @property
    @is_account_open
    def balance(self):
        return self._balance

    @balance.setter
    @is_account_open
    def balance(self, value):
        self.__check_amount_is_positive__(value)
        self._balance = value


    def get_balance(self):
        with self._lock:
            return self.balance

    def open(self):
        if self._isOpen:
            raise ValueError("Account already open")
        self._isOpen = True
        self.balance = 0
        

    def deposit(self, amount):
        with self._lock:
            self.balance += amount

    @is_account_open
    def withdraw(self, amount):
        self.__check_amount_is_positive__(amount)
        with self._lock:
            self.balance -= amount

    @is_account_open
    def close(self):
        with self._lock:
            self.balance = 0
            self._isOpen = False

    """ PRIVATE METHODS """
    def __check_amount_is_positive__(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive number", amount)