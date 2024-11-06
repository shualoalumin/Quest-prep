{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "def counter(func):\n",
    "    count = 0  # 호출 횟수를 저장할 변수 초기화\n",
    "\n",
    "    def wrapper(*args, **kwargs):\n",
    "        nonlocal count  # 외부 함수의 count 변수를 참조\n",
    "        count += 1  # 호출할 때마다 count 증가\n",
    "        result = func(*args, **kwargs)  # 원래 함수 실행\n",
    "        print(f\"{func.__name__} 실행횟수: {count}\")  # 함수 이름과 실행 횟수 출력\n",
    "        return result\n",
    "\n",
    "    return wrapper  # 내부 함수 반환하여 데코레이터 기능 부여\n",
    "\n",
    "\n",
    "@counter\n",
    "def say_hello():\n",
    "    print(\"Hello Aiffel!\")\n",
    "\n",
    "for i in range(5):\n",
    "    say_hello()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
