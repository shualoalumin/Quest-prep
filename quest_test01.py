#Avengers Vocab 만들기!

import re
from collections import Counter


# 텍스트 전처리를 위한 함수

def preprocess_text():
    # Avengers.txt 파일 불러오기
    with open('Avengers.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # 소문자 변환
    text = text.lower()

    # 기호제거
    text = re.sub(r'[^a-z\s]', '', text)

    # 단어 단위로 분리
    words = text.split()
    return words

def make_vocab():
    # 1. 텍스트 전처리 실행
    words = preprocess_text()

    # 2. 단어별 빈도수를 딕셔너리 형태로 저장
    word_count = Counter(words)

    # 3. 빈도수 기준 내림차순 정렬 후 + 정렬된 단어에 인덱스 부여
    sorted_words = word_count.most_common()

    vocab = {}
    for idx, (word, _) in enumerate(sorted_words):     # 인덱싱
        vocab[word] = idx

    return word_count, vocab



    #4. 텍스트를 input()으로 입력받아서 정수를 return하는 함수 정의

def encoder():
    # vocab 딕셔너리 생성
    _, vocab = make_vocab()

    # 문장 입력받기
    text = input()

    # 입력 문장 전처리
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()

    # 정수 인덱스로 변환
    return [vocab.get(word, -1) for word in words]

if __name__ == "__main__":
    # 딕셔너리 출력 테스트
    dic, vocab = make_vocab()
    print(dic)
    print(vocab)

    # encoder 테스트
    result = encoder()
    print(result)




    # 회고 :
    # 각 항목마다 좀더 파이써닉 한 방법이 있고
    # 그것들을 통해 전체적인 코딩이 간결해지는 과정을 확인할 수 있었습니다.
