# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 오병철
- 리뷰어 : 김대환


# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 코드가 잘 작동합니다.
    ```
    계산기 프로그램
    첫 번째 정수를 입력하세요: 3
    두 번째 정수를 입력하세요: 4
    연산자를 입력하세요 (+, -, *, /, **): -
    결과: -1
    계산을 계속하시겠습니까? (y/n): n
    계산기를 종료합니다.
    ```
    - 잘 된 점 (선택 입력값에 대한 예외처리가 잘 되었고 재실행가능하도록 잘 마무리가 되었습니다.)
    ```
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
    ```


- [ ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    
    - 코드라인에서 주석이 빠져있습니다.
    - 각 모듈에 대한 기능설명(intro)을 docstring으로 요약해주셔도 좋을 것 같습니다.

        
- []  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    
    - 버그과정이 없었던 것 같습니다.

- [x]  **4. 회고를 잘 작성했나요?**
    
    - 상세하게 작성되었습니다. 
    - 조금 더 요약해서 작성하면 좋을 것 같습니다.

- [x]  **5. 코드가 간결하고 효율적인가요?**

    - 간결했던 부분
    ```
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
    ```

    - 개선을 건의드리는 부분:main함수에 맥락이 다른 기능들이 통합돼 있어 
      기능적으로 [변수지정]과 [연산에 대한 예외처리]는 calculate()에 넣어주면 어떨까합니다.^^
    ```
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
    ```


# 회고(김대환)

```
1. 연산에 대한 결과값을 수식으로 출력하면 더 좋을 것 같습니다.^^
    ```
    print(f"계산결과: {num1} {operator} {num2} = {result}")
    ```
2. 1번이 적용된다면, 수식 순서에 맞게 입력값을 받는 것도 좋을 것 같습니다.^^
    -현재 순서
    ```
    num1 = get_integer("첫 번째 정수를 입력하세요: ")
    num2 = get_integer("두 번째 정수를 입력하세요: ")
    operator = get_operator()
    ``` 

3. calculate() 함수와 main() 함수의 경계선이 명확해지면 함수를 정의하기 더 좋을 것 같습니다.^^
    
```


