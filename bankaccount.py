class name:

  class bankaccount:
    "simple bankaccount class"


def balance(self, amount=100):
  print("initialize account with balance")
  self.balance = amount


def deposit(self, amount=789):
  print("deposit amount to this account")
  self.balance = amount


def withdraw(self, amount=900):
  print("withdraw amount from this account")
  self.balance = amount


bankaccount = balance
bankaccount = deposit
bankaccount = withdraw
