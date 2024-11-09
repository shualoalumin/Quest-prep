# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("동물이 소리를 냅니다")

# 자식 클래스        
class Dog(Animal):  # Animal 클래스를 상속
    def __init__(self, name, breed):
        super().__init__(name)  # 부모 클래스의 __init__ 호출
        self.breed = breed
    
    def make_sound(self):  # 메서드 오버라이딩
        print("멍멍!")
        
    def fetch(self):  # 새로운 메서드 추가
        print(f"{self.name}이(가) 공을 가져옵니다")

# 사용 예시
my_dog = Dog("바둑이", "진돗개")
my_dog.make_sound()  # 출력: 멍멍!
my_dog.fetch()  # 출력: 바둑이이(가) 공을 가져옵니다