from SimpleQIWI import *
print('Q I W I Software 1.0 / coded by m1wka!');
token=input('Enter token: ')
phone=input('Enter phone: ');
api = QApi(token=token, phone=phone)
print('Balance Founded')
print(api.balance)
api.pay(account=input("Enter your qiwi: "), amount=сумма, comment=input("comment: ")
print(api.balance)
input()
