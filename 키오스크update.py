#키오스크 프로그램

# 커피 메뉴와 가격
coffee = ['americano', 'latte', 'mocha'] 
c_price = [2000, 3000, 3000]

# 논커피 메뉴와 가격
non_coffee = ['yuza_tea', 'green_tea', 'choco_latte']
n_price = [2500, 2500, 3000]

# 전체 메뉴와 가격 
menu = coffee + non_coffee
price = c_price + n_price

# Kiosk 클래스 생성 
class Kiosk:
    def __init__(self):
        self.menu = menu
        self.price = price

    # 메뉴 출력 메서드
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i+1, self.menu[i], ' : ', self.price[i], '원')

    # 주문 메서드
    def menu_select(self):
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트
        
        # 메뉴 선택 입력값 예외 처리
        while True:
            try:
                n = int(input('음료 번호를 입력하세요 : '))
                if 1 <= n <= len(self.menu):
                    break
                print("없는 메뉴입니다. 다시 주문해 주세요.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
        
        self.order_price.append(self.price[n-1])
        self.price_sum = self.price[n-1]
        print(self.menu[n-1], ' : ', self.price_sum , '원')

        # 온도 선택 예외 처리
        while True:
            try:
                t = int(input('HOT음료는 1을, ICE 음료는 2를 입력하세요 : '))
                if t == 1:
                    self.temp = "HOT"
                    break
                elif t == 2:
                    self.temp = "ICE"
                    break
                print("1과 2 중 하나를 입력해주세요.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
              
        self.order_menu.append(self.temp + ' ' + self.menu[n-1])
        print(self.temp, self.order_menu[0], ' : ', self.price_sum, '원')

        # 추가 주문 
        while True:
            try:
                print()
                n = int(input('추가 주문은 음료 번호를, 지불은 0을 누르세요 : '))
                if n == 0:
                    print("\n주문이 완료되었습니다.")
                    print('*'*30)
                    [print(f"{menu} {self.order_menu.count(menu)}잔") for menu in set(self.order_menu)]
                    print('*'*30)
                    print(f"총 결제 금액: {self.price_sum}원")
                    break
                elif 1 <= n <= len(self.menu):
                    # 추가 음료 온도 선택 입력값 예외 처리
                    while True:
                        try:
                            t = int(input('HOT음료는 1을, ICE 음료는 2를 입력하세요 : '))
                            if t == 1:
                                self.temp = "HOT"
                                break
                            elif t == 2:
                                self.temp = "ICE"
                                break
                            print("1과 2 중 하나를 입력해주세요.")
                        except ValueError:
                            print("올바른 숫자를 입력해주세요.")
                    
                    self.order_menu.append(self.temp + ' ' + self.menu[n-1])
                    self.order_price.append(self.price[n-1])
                    self.price_sum += self.price[n-1]
                    print('추가 주문 음료', self.temp, self.menu[n-1], ' : ', self.price[n-1], '원\n', '합계 : ', self.price_sum, '원')
                else:
                    print("없는 메뉴입니다. 다시 선택해주세요.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")

    # 결제수단 메서드
    def pay(self):
        while True:
            try:
                payment = int(input('결제 수단을 선택하세요. 현금은 1을, 카드는 2를 입력하세요 : '))
                if payment == 1:
                    print('직원을 호출하겠습니다.')
                    break
                elif payment == 2:
                    print('IC칩 방향에 맞게 카드를 꽂아주세요.')
                    break
                else:
                    print('다시 결제를 진행해주세요.')
            except ValueError:
                print('다시 결제를 진행해주세요.')

# 프로그램 실행
a = Kiosk()
print('\n메뉴판')
print('*'*30)
a.menu_print()
print('*'*30)
a.menu_select()
a.pay()