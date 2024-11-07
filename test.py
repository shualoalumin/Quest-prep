# 연산자함수 테스트

import math

def operator_input():
        operator = input("연산자를 입력하세요(+,-,*,/,**): ")
        if operator in ['+','-','*','/','**']:
            return operator

        else:
            print("지원하지 않는 연산자입니다.")
