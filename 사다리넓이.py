# 사각형 넓이를 구하는 클래스 완성!
class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if self.square == 1:
            print('직사각형 함수는 rect()입니다.')

        elif self.square == 2:
            print('평행사변형 함수는 par()입니다.')
        
        elif self.square == 3:
            print('사다리꼴 함수는 trape()입니다.')
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area) + '입니다.'
        return result

    def par(self):
        base, height = map(int, input('밑변, 높이를 입력하세요. 예시 : 밑변,높이\n >>>').split(','))
        area = base * height
        result = '평행사변형의 넓이는 : ' + str(area) + '입니다.'
        return result

    def trape(self):
        upper, lower, height = map(int, input('윗변, 아랫변, 높이를 입력하세요. 예시 : 윗변, 아랫변, 높이\n >>>').split(','))
        area = (upper + lower) * height / 2
        result = '사다리꼴의 넓이는 : ' + str(area) + '입니다.'
        return result

a = Square()  