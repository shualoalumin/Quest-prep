def counter(func):
    count = 0  # 호출 횟수를 저장할 변수 count 초기화

    # 데코레이터 함수 정의 
    """(docstring)중요! 키워드 인자 처리로 함수 재사용성 확보
    (docstring)함수가 실행될 때 마다 함수 이름과 실행 횟수를 출력하는 데코레이터"""

    def deco(*args, **kwargs): 
        nonlocal count  # 외부 변수 count를 참조
        count += 1  # 호출할 때마다 count 누적 증가
        result = func(*args, **kwargs) 
        print(f"{func.__name__} 실행횟수: {count}") # 실행마다 함수 이름과 실행횟수 출력
        return result

    return deco

# 테스트 코드
@counter
def say_hello():
    print("Hello Aiffel!")

for i in range(5):
    say_hello()

'''
* 디버깅 과정 : 
    *args와 **kwargs의 기능 : 
    *args와 **kwargs 없이도 데코레이터를 만들 수는 있지만 모든 함수에 적용이 되지 않는다. 
    *args와 **kwargs를 사용하면 "인수의 개수나 형식에 관계없이" 데코레이터를 적용할 수 있다.


* 김대환(코더) 회고:
위 데코레이터의 내부함수(클로저)는 실행횟수를 기억하고 있기 때문에
사용하면 함수의 실행 횟수를 추적하고 출력할 수 있고,
데코레이터를 활용해 다른 테스트에서도 해당 함수의 재사용성을 확보할 수 있다.
'''