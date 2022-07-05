def deposit(balance, money): #입금 함수, 입금액,잔액 전달 받아 반환해준다ㅣ.
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money): #출금
    if balance >= money: #출금가능
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 불가능합니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance-money-commission #2개의 값을 반환한다.

balance = 0
balance = deposit(balance,1000)
print(balance)

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
print(balance)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
