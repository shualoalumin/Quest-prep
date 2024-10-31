# 회문 확인 프로그램

def isPalindrome():
  # 1. 문자열을 입력받고, 출력합니다.
  input_word = input('입력값:\n')
  print()

  # 2. 문자열을 뒤집는 과정입니다.
  output_word = ""
  num = len(input_word)
  while num > 0 :
    output_word = output_word + input_word[num - 1]
    num = num - 1

  # 3. 뒤집힌 문자열 출력합니다.
  print('출력값:')
  print('뒤집힌 단어:', output_word)

	# 4. 두 문자열 비교하고 결과를 출력합니다.
  if input_word == output_word:
      print('입력된 단어는 회문입니다.')
  else:
      print('입력된 단어는 회문이 아닙니다.')

if __name__ == "__main__":
  isPalindrome()