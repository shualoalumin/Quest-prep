# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 
- 리뷰어 : 김대환


# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 
    ```
    Q1.
        최솟값: 3
        최댓값: 12
    
    Q2.
        Hello Aiffel!
        say_hello 실행횟수: 1
        Hello Aiffel!
        say_hello 실행횟수: 2
        Hello Aiffel!
        say_hello 실행횟수: 3
        Hello Aiffel!
        say_hello 실행횟수: 4
        Hello Aiffel!
        say_hello 실행횟수: 5
    ```

- [ ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    
    - 주석과 doc string이 빠져있습니다. 
    ```
    def counter(fn):
        def printCounter(i):
            print("Hello Aiffel!")
            fn(i)
        return printCounter

    @counter
    def say_hello(i):
        print("say_hello 실행횟수:", i + 1)

    for i in range(5):
        say_hello(i)   
    ```

        
- [ ]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    
    - 디버깅 과정이 빠져있습니다. 
      오류 : 
      - 2번 문제에 입력값이 달라져 있습니다. 
      - 내부함수에서 누적함수를 적용하지 않고 테스트 함수에서 누적함수를 적용했습니다. 
        ```
        @counter
        def say_hello(i):
            print("say_hello 실행횟수:", i + 1)
        ```

      - 내부함수에서 nonlocal 키워드를 사용하지 않았습니다.             
        ```
          def printCounter(i):
            print("Hello Aiffel!")
            fn(i)
        return printCounter
        ```


- [ ]  **4. 회고를 잘 작성했나요?**
    
    - 회고는 빠져있습니다. 

- [ ]  **5. 코드가 간결하고 효율적인가요?**
    - 데코레이터에서 누적값을 적용하지 않아 재사용가능한 모듈화가 아닙니다. 

    ```
    def counter(fn):
        def printCounter(i):
            print("Hello Aiffel!")
            fn(i)
        return printCounter
    ```

# 회고(김대환)

# 내부함수 제안
```
def deco(*args, **kwargs): '''키워드 인자를 처리해 주시면 다른 함수와 다른 인자값에도 적용할 수 있습니다.'''
        nonlocal count  # nonlocal 키워드를 사용해 외부 변수 count를 참조하고
        count += 1  # 호출할 때마다 count 누적 증가되어 내부함수가 기억합니다.
        result = func(*args, **kwargs)
        print(f"{func.__name__} 실행횟수: {count}") # 함수 이름과 실행횟수 출력을 내부함수에서 처리합니다.
        return result 

    return deco

```


