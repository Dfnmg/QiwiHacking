from SimpleQIWI import *
print('Q I W I Software 1.0 / coded by m1wka!');
token=input('Enter token: ')
phone=input('Enter phone: ');
api = QApi(token=token, phone=phone)
print('Balance Founded')
print(api.balance)
api.pay(account="", amount=сумма, comment='')
print(api.balance)
input()
