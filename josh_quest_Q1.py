def find_min_max(numbers):
    # min_value와 max_value 변수를 초기화
    min_value = float('inf')
    max_value = float('-inf')

    def update_min_max(num):
        nonlocal min_value, max_value
        # 만약 num 값이 min_value보다 작다면 min_value를 num 값으로 변경
        if num < min_value:
            min_value = num
        # 만약 num 값이 max_value보다 크다면 max_value를 num 값으로 변경
        if num > max_value:
            max_value = num

        return min_value, max_value 
    
    # numbers 리스트의 모든 값을 순환하며 최댓값과 최솟값 업데이트
    for num in numbers:
        update_min_max(num)

    # 최솟값을 반환하는 내부함수
    def get_min():
        return min_value

    # 최댓값을 반환하는 내부함수
    def get_max():
        return max_value

    # 외부함수는 내부함수(get_min()과 get_max())를 반환
    return get_min, get_max 



# 테스트 코드
numbers = [10, 5, 8, 12, 3, 7]
find_min, find_max = find_min_max(numbers)

print("최솟값:", find_min())  # 출력: 3
print("최댓값:", find_max())  # 출력: 12




'''
* 변수 초기화 과정 : 
    max_value = float('-inf') : 음의 무한대로 초기화 하는 의미
    가장 작은 값으로 초기화해 두면 최대값을 찾을 때 어떤 수가 와도 최댓값 갱신 보장

    반대로, 
    min_value = float('inf') : 양의 무한대로 초기화 하는 의미
    가장 큰 값으로 초기화해 두면 최솟값을 찾을 때 어떤 수가 와도 최솟값 갱신 보장


* 클로저를 통한 변수 노출 방지
    위의 min_value, max_value 가 nonlocal로 지정되고
    마지막에 get_min, get_max 함수를 반환함으로써 클로저를 구현함
    이렇게 하면 외부에서는 내부함수만 접근할 수 있고
    내부함수 내에서만 min_value, max_value 변수에 접근하므로 보완성 확보


김대환(코더) 회고:
변수를 외부에 노출하지 않는다의 의미에 대해 이해한 과정. 
변수를 외부에서 접근할 수 없도록 한다는 것은 변수의 값이 외부에서 
잘못 수정되는 것을 방지할 수 있고 개발 과정에서 오류를 줄일 수 있다.


디버깅 과정 : 
    변수 초기화 부분이 최솟값과 최대값을 찾는 과정에 선행되어야 함
    즉, 최솟값과 최대값을 찾는 과정에서 변수 초기화 부분이 먼저 실행되어야 함
'''