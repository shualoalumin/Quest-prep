import random

class Account:
    account_count = 0
    
    def __init__(self, name, balance):
        self.bank = "SC은행"
        self.name = name
        self.balance = balance
        self.deposit_count = 0
        self.deposit_history = []
        self.withdraw_history = []
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        self.account_number = f"{num1:03d}-{num2:02d}-{num3:06d}"
        
        Account.account_count += 1
        print(f"은행 이름: {self.bank}, 예금주: {self.name}, 계좌번호: {self.account_number}, 잔고: {self.balance:,}")
    
    def get_account_num(self):
        return Account.account_count
    
    def deposit(self, money):
        try:
            money = int(money)
            if money > 0:
                self.balance += money
                self.deposit_count += 1
                self.deposit_history.append(("입금", money, self.balance))
                
                if self.deposit_count % 5 == 0:
                    interest = int(self.balance * 0.01)
                    self.balance += interest
                    self.deposit_history.append(("이자지급", interest, self.balance))
                
                return money
            else:
                print("입금은 1원 이상만 가능합니다.")
        except (ValueError, TypeError):
            print("올바른 금액을 입력하세요")
            
    def withdraw(self, money):
        try:
            money = int(money)
            if money > 0:
                if self.balance >= money:
                    self.balance -= money
                    self.withdraw_history.append(("출금", money, self.balance))
                    return money
                else:
                    print("계좌 잔고 이상으로 출금할 수 없습니다.")
            else:
                print("금액이 잘못되었습니다.")
        except (ValueError, TypeError):
            print("올바른 금액을 입력하세요")
    
    def display_info(self):
        print(f"은행 이름: {self.bank}, 예금주: {self.name}, 계좌번호: {self.account_number}, 잔고: {self.balance:,}")
    
    def deposit_history(self):
        print("\n거래내역:")
        for i, (transaction_type, amount, balance) in enumerate(self.deposit_history, 1):
            print(f"{i}회: {transaction_type:<6} 금액: {amount:<8} 잔액: {balance}")
    
    def withdraw_history(self):
        for i, (transaction_type, amount, balance) in enumerate(self.withdraw_history, 1):
            print(f"{i}회: {transaction_type:<6} 금액: {amount:<8} 잔액: {balance}")

# 실행 코드
first_account = Account('차정은', 1000)
second_account = Account('박광석', 30000000)
third_account = Account('조웅제', 50000000)

print(f"\n생성된 계좌의 총 개수: {Account.account_count}")

# 거래 내역 테스트를 위한 반복 입금
my_account = Account("테스트", 1000)
for i in range(11):
    my_account.deposit(1000)

# 출금 테스트
my_account.withdraw(3000)

print("-" * 50)
my_account.deposit_history()
print("-" * 50)
my_account.withdraw_history()