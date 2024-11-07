
'''정수 계산기를 실행하는 프로그램 모듈입니다.'''

import math

#1 입력값 ≠ 정수 → ValueError 처리
def integer_input(prompt):
    while True: #정수를 입력할 때까지 반복
        try:
            input_num = int(input(prompt))
            return input_num
        except ValueError: #2 잘못된 입력 → 예외처리
            print("잘못된 입력입니다. 정수를 입력해주세요.") 



# 연산식 정의
def calculator():
    num1 = integer_input("첫번째 정수를 입력하세요: ")


    '''연산자 입력에 관한 예외 처리 과정 = while, break, else로 구성'''
    while True:
        operator = input("연산자를 입력하세요(+, -, *, /, **): ")
        if operator in ['+','-','*','/','**']:
            break
        else:
            print("지원하지 않는 연산자입니다.") #4 지원하지 않는 연산자 예외처리
            
    num2 = integer_input("두번째 정수를 입력하세요: ")


    '''계산 결과 반환 과정 = try, if, elif, else로 구성'''
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '**':
            result = math.pow(num1, num2) #5 math.pow 함수모듈 사용
        
        print(f"계산결과: {num1} {operator} {num2} = {result}")
        return result

    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.") #3 나눗셈에서 0으로 나눌 수 없는 경우 예외처리
        return None
        




# 계산 실행 

while True:
    result = calculator()
    if result is None:
        print("계산기를 종료합니다.")
        break
    continue_input = input("계속하시겠습니까? (y/n): ")
    if continue_input not in ['y','n']:
        print("잘못된 입력입니다. y 또는 n을 입력해주세요.")
    elif continue_input == 'n':
        print("계산기를 종료합니다.")
        break


'''
$$$주요 디버깅 과정$$$
1. 연산자 예외처리
2. 계산 result 반환 과정
3. 계산 결과문 출력 과정
4. 계속 여부 입력 과정


$$$김대환(코더) 회고$$$
1. 연산자예외처리 과정에서 예외처리 조건의 'return값 설정으로 인한 버그'가 원인파악과정에서 소요시간이 길었다.
2. 결과문 출력 과정이 스킵되는 원인이 출력문 위치 수정으로 calculate() 전체적인 구조 수정이 필요했다.
3. 구조 수정 과정에서 제로디비젼에 대한 return값을 none으로 설정하면 해결되었는데 이부분에 대한 follow-up 과정이 필요했다.
4. Quest 03까지 진행해오면서 성장한 자신을 발견하고 뿌듯함을 느꼈다.   
'''
