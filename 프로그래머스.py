while True:
    try:
        str = input("문자열을 입력하세요: ").replace(" ", "")
        
        if not 1 <= len(str) <= 1000000:
            raise ValueError("길이가 1~1,000,000 범위를 벗어났습니다.")
        
        print(f"결과: {str}")
        break
        
    except ValueError as e:
        print(f"오류: {e}")