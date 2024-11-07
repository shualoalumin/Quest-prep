# [QUEST 04] 파이썬을 사용하여 간단한 계산기 프로그램 만들기

# 사용자로부터 두 개의 정수와 연산자(+,-,*,/,**)를 입력받아 계산 결과를 출력하는 프로그램을 만들어주세요

# 조건
# 사용자가 입력한 값이 정수가 아닌 경우 ValueError를 처리하여 적절한 오류 메시지를 출력해야 합니다
# 정수가 입력될 때 까지 잘못된 입력입니다. 정수를 입력해주세요."를 출력하며 다시 입력받기를 시도합니다.
# 나눗셈 연산 시 두 번째 정수가 0인 경우 ZeroDivisionError를 처리하여 적절한 오류 메시지를 출력합니다.
# 사용자가 지원하지 않는 연산자를 입력한 경우 적절한 오류 메시지를 출력합니다.
# math 모듈을 사용하여 제곱 연산(**)을 지원합니다.
# 계산기를 통해 계속 계산을 할 것인지 입력받습니다.

import math

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해주세요.")

def get_operator():
    while True:
        operator = input("연산자를 입력하세요 (+, -, *, /, **): ")
        if operator in ('+', '-', '*', '/', '**'):
            return operator
        else:
            print("지원하지 않는 연산자입니다. 다시 입력해주세요.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return num1 / num2
    elif operator == '**':
        return math.pow(num1, num2)

def main():
    while True:
        print("\n계산기 프로그램")

        num1 = get_integer("첫 번째 정수를 입력하세요: ")
        num2 = get_integer("두 번째 정수를 입력하세요: ")
        operator = get_operator()

        try:
            result = calculate(num1, num2, operator)
            print(f"결과: {result}")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print("예상치 못한 오류가 발생했습니다.", e)

        while True:
            again = input("계산을 계속하시겠습니까? (y/n): ").strip().lower()

            if again == 'y':
              break
            elif again == 'n':
              print("계산기를 종료합니다.")
              return
            else:
              print("잘못된 입력입니다. y또는 n을 입력해주세요.")

if __name__ == "__main__":
    main()

''' 작성자 오병철의 회고
먼저, 사용자 입력을 처리하는 부분에 신경을 많이 썼습니다.
get_integer_input 함수를 따로 만들어 정수 입력을 받고 예외 처리를 하도록 했는데, 이렇게 하면 코드의 재사용성도 높아지고 main 함수가 더 깔끔해질 것 같았습니다.
calculate 함수에서는 다양한 연산을 처리하도록 했습니다. 특히 0으로 나누는 경우와 지원하지 않는 연산자를 사용하는 경우에 대한 예외 처리를 추가했는데,
이런 세세한 부분까지 신경 쓰는 것이 사용자 경험을 향상시키는 데 중요하다고 생각했습니다.
math 모듈을 import해서 제곱 연산을 지원하도록 한 것도 재미있는 시도였습니다. 기본적인 사칙연산 외에 추가 기능을 넣어보니 프로그램이 더 풍성해진 것 같아 뿌듯했습니다.
while 루프를 사용해 계산기를 계속 사용할 수 있게 한 것도 좋은 아이디어였다고 생각합니다. 사용자가 원하는 만큼 계산을 반복할 수 있어 편리할 것 같습니다.
전체적으로 이 프로그램을 작성하면서 예외 처리의 중요성을 다시 한 번 깨달았습니다. 사용자의 입력은 예측할 수 없기 때문에, 가능한 모든 경우의 수를 고려해 프로그램이 안정적으로 동작하도록 하는 것이 중요하다는 걸 배웠습니다.
앞으로는 이 프로그램을 더 발전시켜 복잡한 수식도 처리할 수 있게 하거나, GUI를 추가해 더 사용자 친화적으로 만들어보고 싶습니다.
이번 경험을 통해 프로그래밍의 재미를 다시 한 번 느낄 수 있었고, 앞으로도 이런 프로젝트를 계속 해나가고 싶습니다.
'''