# JOSH CAFE 키오스크 프로그램입니다.

# 커피 메뉴와 가격
coffee = ['Americano', 'Latte', 'Mocha'] 
c_price = [2000, 3000, 3000]
# 논커피 메뉴와 가격
non_coffee = ['Yuza_Tea', 'Green_Tea', 'Choco_Latte']
n_price = [2500, 2500, 3000]

# 전체 메뉴와 가격 
menu = coffee + non_coffee
price = c_price + n_price

# Kiosk(키오스크) 클래스 생성 
class Kiosk:
    def __init__(self):
        self.menu = menu
        self.price = price

    # 메뉴판 메서드 추가
    def menu_print(self):
        for i in range(len(self.menu)):
            print(f"{i+1:>2}. {self.menu[i]:<12} : {format(self.price[i], ','):>7}원")

    # 주문 메서드 추가
    def menu_select(self):
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트
        
        # 첫 메뉴 선택
        while True:
            try:
                n = int(input('주문하실 메뉴번호를 입력하세요 : '))
                if 1 <= n <= len(self.menu):
                    self.order_price.append(self.price[n-1])
                    self.price_sum = self.price[n-1]
                    break
                else:
                    print("없는 메뉴입니다. 다시 입력해 주세요.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")

        # 첫 음료 온도 선택
        while True:
            try:
                t = int(input('HOT은 1 , ICE는 2 를 입력하세요 : '))
                if t == 1:
                    self.temp = "HOT"
                    break
                elif t == 2:
                    self.temp = "ICE"
                    break
                else:
                    print("1 과 2 중 하나를 입력해주세요.\n")
            except ValueError:
                print("올바른 숫자를 입력해주세요.\n")
              
        self.order_menu.append(self.temp + ' ' + self.menu[n-1])
    
        print('\n<주문 내역>')
        print('-' * 30)
        print(f"{self.order_menu[0]:<15} : {format(self.order_price[0], ','):>10}원")
        print('-' * 30)
        total_width = 30  # 전체 너비
        price_str = format(self.price_sum, ',')
        space_width = total_width - len("총 1잔") - len("합계:") - len(price_str) - len("원")
        print(f"총 1잔{' '*(25-len('총 1잔') - len('합계:') - len(str(format(self.price_sum, ','))) - 1)}합계:{format(self.price_sum, ',')}원")
        

        # 추가 주문 또는 결제
        while True:
            try:
                n = int(input('\n>>> 추가 주문은 메뉴번호를 누르시고, 결제를 원하시면 0 을 누르세요 : '))
                if n > 0 and n < len(self.menu)+1:
                    # 추가음료 온도선택
                    while True:
                        try:
                            t = int(input('HOT은 1 , ICE는 2 를 입력하세요 : '))
                            if t == 1:
                                self.temp = "HOT"
                                break
                            elif t == 2:
                                self.temp = "ICE"
                                break
                            else:
                                print("1 과 2 중 하나를 입력해주세요.\n")
                        except ValueError:
                            print("올바른 숫자를 입력해주세요.\n")
            
                    self.order_menu.append(self.temp + ' ' + self.menu[n-1])
                    self.order_price.append(self.price[n-1])
                    self.price_sum += self.price[n-1]
                
                    print('\n<주문 내역>')
                    print('-' * 30)
                    for i in range(len(self.order_menu)):
                        print(f"{self.order_menu[i]:<15} : {format(self.order_price[i], ','):>10}원")
                    print('-' * 30)
                    total_width = 25  # 전체 너비
                    price_str = format(self.price_sum, ',')
                    space_width = total_width - len(f"총 {len(self.order_menu)}잔") - len("합계:") - len(price_str) - len("원")
                    print(f"총 {len(self.order_menu)}잔{' '*space_width}합계:{price_str}원")
                
                elif n == 0:
                    print("\n결제 전 주문내역을 확인하세요.")
                
                    '''<주문목록 확인>을 포함시켰고, 메뉴판과 함께 가독성 개선을 위한 외곽 수정''' 
                    print('*'*30)
                    # 중복감안한 주문목록 리스트 생성 후 각 메뉴 수량 계산 >>> 리스트컴프리헨션 사용했습니다. 
                    [print(f"{menu} {self.order_menu.count(menu)} 잔") for menu in set(self.order_menu)]
                    print('*' * 30)
                    print(f"총 결제 금액: {format(self.price_sum, ',')}원")
                    break
                else:
                    print("올바른 메뉴 번호를 입력해주세요.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")

    # 결제 메서드 추가
    def pay(self):
        while True:
            try:
                payment = int(input('\n결제 수단을 선택하세요. 현금은 1을, 카드는 2를 입력하세요 : '))
                if payment == 1:
                    print('\n직원을 호출하겠습니다.')
                    break
                elif payment == 2:
                    print('\n>>>IC칩 방향에 맞게 카드를 꽂아주세요.')
                    break
                else:
                    print('다시 결제를 진행해주세요.')
            except ValueError:
                print('다시 결제를 진행해주세요.')
        
        '''
        >>> pay() 예외처리 관련 UPDATE :
            앞에서 메뉴선택과 온도선택에서 사용한 if-else방식이 아닌,
            while True와 try-except로 예외처리 했습니다.
        
        >>> 이유:
            노드의 if-else 방식으로 할 경우, 
            
            입력값에
                1. 문자 or 기호 포함
                2. 실수값 입력
                3. 입력값 없이 enter만 입력
            
            위 3가지 중 하나가 해당하면
            에러 메세지가 뜸과 동시에 클래스를 다시 실행야 합니다. 
            
            (예시) 
             5개 음료주문과정에서, 5번째 음료 주문시
             위 3가지 중 하나에 해당하면 다시 첫번째 메뉴입력으로 돌아가야함 >>>고객불편제공
        
        >>> 회고:
            예외처리시 예상되는 실제적 상황과 변수를 고려해볼 수 있는 과정이었습니다.
        '''

    # 주문표 메서드
    def table(self):
        while True:
            try:
                show_table = input('\n주문표를 출력하시겠습니까? (Y/N): ').upper()
                if show_table == 'Y':
                    # 외곽
                    print('\n⟝' + '-' * 11 + ' 주문표 ' + '-' * 11 + '⟞')
                    for i in range(5):
                        print('|' + ' ' * 31 + '|')

                    # 주문 상품명 : 해당 금액
                    for i in range(len(self.order_menu)):
                        print(self.order_menu[i], ' : ', format(self.order_price[i], ','))

                    print('= 합계 금액 :', format(sum(self.order_price), ','))

                    # 외곽
                    for i in range(5):
                        print('|' + ' ' * 31 + '|')
                    print('⟝' + '-' * 30 + '⟞')
                    print('\n주문하신 음료가 준비 중입니다. 잠시만 기다려주세요.')
                    break
                elif show_table == 'N':
                    print('\n주문하신 음료가 준비 중입니다. 잠시만 기다려주세요.')
                    break
                else:
                    print('Y 또는 N을 입력해주세요.')
            except ValueError:
                print('Y 또는 N을 입력해주세요.')

   
#키오스크 실행       
a = Kiosk()
print('''
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
|     Welcome to Cafe.JOSH    |
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
''')
print('MENU'.center(30))
print('*'*30)
a.menu_print()
print('*'*30)
a.menu_select()
a.pay()
a.table()