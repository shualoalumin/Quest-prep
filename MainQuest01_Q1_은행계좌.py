import random

class Account:
    account_count = 0
    
    def __init__(self, name, balance):
        self.bank = "SC은행"
        self.name = name
        self.balance = balance
        self.deposit_count = 0
        self.deposits = []
        self.withdraws = []
        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        self.account_number = f"{num1:03d}-{num2:02d}-{num3:06d}"
        
        Account.account_count += 1
    
    def get_account_num(self):
        return Account.account_count
    
    def deposit(self, money):
        try:
            money = int(money)
            if money > 0:
                self.balance += money
                self.deposit_count += 1
                self.deposits.append((money, self.balance))
                
                if self.deposit_count % 5 == 0:
                    interest = int(self.balance * 0.01)
                    self.balance += interest
                    print(f"{interest}원의 이자가 입금되었습니다.")
                    self.deposits.append((interest, self.balance))
    
                return money
            else:
                print("입금은 최소 1원 이상만 가능합니다.")
        except (ValueError, TypeError):
            print("올바른 금액을 입력하세요")
            
    def withdraw(self, money):
        try:
            money = int(money)
            if money > 0:
                if self.balance >= money:
                   self.balance -= money
                   self.withdraws.append(money)
                   return money
                else:
                    print("계좌 잔고 이상으로 출금할 수 없습니다.")
            else:
                print("출금은 1원 이상만 가능합니다.")
        except (ValueError, TypeError):
            print("올바른 금액을 입력하세요")
    
    def display_info(self):
        print(f"(은행이름: {self.bank}, 예금주: {self.name}, 계좌번호: {self.account_number},잔고: {self.balance:,}원)")
    
    def deposit_history(self):
        for i, (money, balance) in enumerate(self.deposits, 1):
            if (i-1) % 6 == 5:
                print(f"{i}회: 이자지급\t금액: {money:,}\t잔액: {balance:,}")
            else:
                print(f"{i}회: 입금\t금액: {money:,}\t잔액: {balance:,}")
                
    def withdraw_history(self):
        balance = self.balance + sum(self.withdraws)  # 출금 전의 잔액으로 시작
        for i, money in enumerate(self.withdraws, 1):
            balance -= money
            print(f"{i}회: 출금\t금액: {money:,}\t잔액: {balance:,}")



# 실행 코드
first_account = Account('차정은', 1000)
second_account = Account('박광석', 30000000)
third_account = Account('조웅제', 50000000)

print(f"\n생성된 계좌의 총 개수: {Account.account_count}")

account_list = [first_account, second_account, third_account]
for a in account_list:
    if a.balance >= 1000000:
        a.display_info()
        print()

my_account = Account('차정은', 1000)
for i in range(10):
    my_account.deposit(1000)
my_account.deposit(-1000)
my_account.withdraw(3000000)
my_account.withdraw(3000)

print()
my_account.deposit_history()
print('-' * 50)  # 구분선 출력
my_account.withdraw_history()
