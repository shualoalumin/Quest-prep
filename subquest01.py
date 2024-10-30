def coffee_machine():
    print("=== 커피 자판기 ===")
    print("1. 아메리카노 (3000원)")
    print("2. 라떼 (3500원)")
    
    money = int(input("돈을 넣어주세요: "))
    choice = int(input("메뉴를 선택하세요 (1 또는 2): "))
    
    if choice == 1:
        if money >= 3000:
            change = money - 3000
            print(f"아메리카노가 나왔습니다. 잔돈은 {change}원입니다.")
        else:
            print("잔액이 부족합니다.")
    elif choice == 2:
        if money >= 3500:
            change = money - 3500
            print(f"라떼가 나왔습니다. 잔돈은 {change}원입니다.")
        else:
            print("잔액이 부족합니다.")

# 실행 예시
# === 커피 자판기 ===
# 1. 아메리카노 (3000원)
# 2. 라떼 (3500원)
# 돈을 넣어주세요: 5000
# 메뉴를 선택하세요 (1 또는 2): 1
# 아메리카노가 나왔습니다. 잔돈은 2000원입니다.
