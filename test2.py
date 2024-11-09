# 실습퀴즈4. 클래스 3  
# 모두의연구소를 소개하는 클래스를 만들어 보세요.

class Modulabs:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def describe(self):
        return f"{self.name}은 {self.value}."

class FlippedSchool(Modulabs): 
    def __init__(self, name, value):
        super().__init__(name, value)

    def describe(self):
        return f"{super().describe()}"

class Aiffel(Modulabs): 
    def __init__(self, name, value):
        super().__init__(name, value)

    def describe(self):
        return f"{super().describe()}"

class Lab(Modulabs): 
    def __init__(self, name, value):
        super().__init__(name, value)

    def describe(self):
        return f"{super().describe()}"

class Modu:
    def __init__(self, name, modulabs):
        self.name = name
        self.modulabs = modulabs

    def describe(self):
        modulabs_descriptions = [lab.describe() for lab in self.modulabs]
        return f"{self.name}에는 다음과 같은 프로그램들이 있습니다 :\n" + "\n".join(modulabs_descriptions)
    
    
# 결과 확인
modulabs1 = Modulabs("모두연", "지식을 공유하며 경험을 통해 배우는 열린 연구소")
modulabs2 = FlippedSchool("풀잎스쿨", "함께 성장하는 플립 러닝 기반 스터디 모임")
modulabs3 = Aiffel("아이펠", "함께 탐험하며 성장하는 AI 학교")
modulabs4 = Lab("LAB","연구하며 논문도 쓸 수 있는 연구 모임")

modu = Modu("모두연", [modulabs1, modulabs2, modulabs3, modulabs4])
print(modu.describe())